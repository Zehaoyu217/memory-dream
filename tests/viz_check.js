#!/usr/bin/env node
// Headless check of a generated viewer page (bundle P8, BUILD-GUIDE §5.9): node tests/viz_check.js <graph.html>
// Needs Playwright with Chromium. Prints one JSON line per check; exits 1 on any page error or failed check.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const file = path.resolve(process.argv[2] || 'memory/_dream/graph.html');
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage(); const errors = [];
  page.on('pageerror', e => errors.push(String(e))); page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  let ok = true; const out = (name, pass, extra) => { ok = ok && pass; console.log(JSON.stringify({ check: name, pass, ...extra })); };
  const t0 = Date.now();
  await page.goto('file://' + file); await page.waitForTimeout(600);
  const g = JSON.parse(await page.evaluate(() => document.getElementById('data-graph').textContent));
  // ---- P8a timeline ----
  const time = await page.evaluate(() => ({ nodes: document.querySelectorAll('#lanes .node').length, edges: document.querySelectorAll('#lanes .edge').length, legends: document.querySelectorAll('#lanes .legend').length, toggles: document.querySelectorAll('#lanes .legend button.lg').length }));
  const nonLog = (g.notes || []).filter(n => n.updated && !(n.path.includes('/') ? n.path.split('/')[0] : '') .startsWith('log')).length;
  out('timeline drawn', time.nodes === nonLog && time.legends === 2 && time.toggles > 2, { ...time, expectedNodes: nonLog, ms: Date.now() - t0 });
  const linked = (g.notes || []).find(n => (g.edges || []).some(e => (e.src === n.path || e.dst === n.path) && e.rel !== 'refs') && n.updated && !n.path.startsWith('log/'));   // mentions stay hidden until asked for
  if (linked) {
    await page.evaluate(p => { location.hash = '#note=' + encodeURIComponent(p); }, linked.path); await page.waitForTimeout(500);
    const pk = await page.evaluate(() => ({ picked: document.querySelectorAll('#lanes .node.picked').length, hot: document.querySelectorAll('#lanes .edge.hot:not(.off)').length, arrow: !![...document.querySelectorAll('#lanes .edge.hot')].length && getComputedStyle(document.querySelector('#lanes .edge.hot')).markerEnd !== 'none', dim: document.querySelectorAll('#lanes .node.dim').length, lane: document.querySelectorAll('#lanes .bands rect.picked').length, lines: document.querySelectorAll('#lanes .row-line, #lanes .grid line:not(.y):not(.tick)').length, tree: !document.querySelector('#lanes .tree-panel').hidden }));
    out('timeline pick pops, lights its curves with arrows, dims the rest, washes its lane; no lines between lanes', pk.picked === 1 && pk.hot > 0 && pk.arrow && pk.dim > 0 && pk.lane === 1 && pk.lines === 0, pk);
    const hid = await page.evaluate(() => { const b = document.querySelector('#lanes .legend.nodes button.lg'); b.click(); const n = document.querySelectorAll('#lanes .node.off').length; const e = document.querySelectorAll('#lanes .edge.off').length; b.click(); return { nodesHidden: n, edgesHidden: e }; });
    out('timeline legend toggle hides a kind and its curves', hid.nodesHidden > 0, hid);
    const md = await page.evaluate(() => { const g = JSON.parse(document.getElementById('data-graph').textContent); const p = decodeURIComponent(location.hash.slice(6)); const want = new Set(g.entities.filter(e => e.mentions.some(m => m.path === p)).map(e => e.id)); const got = new Set([...document.querySelectorAll('#pick .paper .ent')].map(c => c.dataset.id)); return { md: !!document.querySelector('#pick .md'), technical: !!document.querySelector('#pick details.agent, #pick pre:not(.md pre)'), mentions: want.size, marked: [...want].filter(id => got.has(id)).length, inText: document.querySelectorAll('#pick .md .ent').length, rawIds: /\b[a-z]+-[a-z]+-v\d\b/.test(document.querySelector('#pick .paper').textContent) }; });
    out('note rendered as markdown, every mention marked in it, no technical block, no raw ids', md.md && !md.technical && md.marked === md.mentions, md);
    await page.evaluate(() => { location.hash = ''; history.replaceState(null, '', location.pathname); }); await page.waitForTimeout(200);
  }
  // ---- P8b connections ----
  const t1 = Date.now();
  await page.evaluate(() => window.__memoryGraph.setView('graph')); await page.waitForTimeout(1800);
  const graph = await page.evaluate(() => { const st = window.__memoryGraph.state; return { entities: st.nodes.length, arrows: st.edges.length, gnodes: document.querySelectorAll('#lanes .gnode').length, gedges: document.querySelectorAll('#lanes .gedge').length, legendRows: document.querySelectorAll('#lanes .legend').length, k: +window.__memoryGraph.cam.k.toFixed(3), zones: st.zones.length, zoneRects: document.querySelectorAll('#lanes .gzone').length, zoneNames: document.querySelectorAll('#lanes .gview .zhead div').length, inZone: st.nodes.every(e => { const z = st.zoneOf[e.id], p = st.pos[e.id]; return p.x >= z.x && p.x <= z.x + z.w; }) }; });
  out('graph view: one zone per family, every thing inside its zone', graph.gnodes === graph.entities && graph.gedges === graph.arrows && graph.legendRows === 2 && graph.zones > 0 && graph.zoneRects === graph.zones && graph.zoneNames === graph.zones && graph.inZone, { ...graph, ms: Date.now() - t1 });
  if (graph.entities) {
    const hidden = await page.evaluate(() => { const b = document.querySelector('#lanes .legend.nodes button.lg'); b.click(); const n = document.querySelectorAll('#lanes .gnode.off').length; b.click(); return n; });
    out('graph legend toggle hides a family', hidden > 0, { hidden });
    const pickedZone = await page.evaluate(() => { const G = window.__memoryGraph; const e = G.state.nodes[0]; location.hash = '#entity=' + encodeURIComponent(e.id); return new Promise(r => setTimeout(() => r({ id: e.id, zone: document.querySelectorAll('#lanes .gzone.picked').length, name: document.querySelectorAll('#lanes .gview .zhead div.picked').length, kept: document.querySelectorAll('#lanes .glabel.keep').length, hot: document.querySelectorAll('#lanes .gedge.hot').length }), 400)); });
    out('picking a thing washes its zone and names its neighbours', pickedZone.zone === 1 && pickedZone.name === 1 && pickedZone.kept > 0, pickedZone);
    await page.evaluate(() => { location.hash = ''; history.replaceState(null, '', location.pathname); }); await page.waitForTimeout(200);
    const far = await page.evaluate(() => { const G = window.__memoryGraph; G.zoomAt(0.15 / G.cam.k, 400, 300); const a = document.querySelector('#lanes .glabels').classList.contains('far'); G.zoomAt(1.5 / G.cam.k, 400, 300); const b = document.querySelector('#lanes .glabels').classList.contains('far'); return { zoomedOut: a, zoomedIn: b }; });
    out('names go when zoomed out past reading distance and return when zoomed in', far.zoomedOut && !far.zoomedIn, far);
    const svg = await page.$('#lanes .gview svg'); const bb = await svg.boundingBox();
    const before = await page.evaluate(() => [window.__memoryGraph.cam.x, window.__memoryGraph.cam.y]);
    await page.mouse.move(bb.x + 16, bb.y + 16); await page.mouse.down(); await page.mouse.move(bb.x + 116, bb.y + 76, { steps: 5 }); await page.mouse.up();
    const after = await page.evaluate(() => [window.__memoryGraph.cam.x, window.__memoryGraph.cam.y]);
    out('drag the background pans', Math.round(after[0] - before[0]) === 100 && Math.round(after[1] - before[1]) === 60, { dx: Math.round(after[0] - before[0]), dy: Math.round(after[1] - before[1]) });
    const k0 = await page.evaluate(() => window.__memoryGraph.cam.k); await page.mouse.move(bb.x + bb.width / 2, bb.y + bb.height / 2); await page.mouse.wheel(0, -300); await page.waitForTimeout(100);
    const k1 = await page.evaluate(() => window.__memoryGraph.cam.k);
    out('wheel zooms', k1 > k0, { from: +k0.toFixed(3), to: +k1.toFixed(3) });
    await page.evaluate(() => { const G = window.__memoryGraph; G.fitAll(); G.zoomAt(Math.max(1, 1.2 / G.cam.k), (document.querySelector('#lanes .gview').clientWidth || 800) / 2, (document.querySelector('#lanes .gview').clientHeight || 500) / 2); }); await page.waitForTimeout(250);
    const target = await page.evaluate(() => { const G = window.__memoryGraph; const v = document.querySelector('#lanes .gview'); const W = v.clientWidth, H = v.clientHeight; for (const e of G.state.nodes) { const p = G.state.pos[e.id], sx = p.x * G.cam.k + G.cam.x, sy = p.y * G.cam.k + G.cam.y; if (sx > 30 && sy > 40 && sx < W - 60 && sy < H - 40) return { id: e.id, sx, sy, p }; } return null; });
    if (target) {
      await page.mouse.move(bb.x + target.sx, bb.y + target.sy); await page.waitForTimeout(150);
      const fish = await page.evaluate(() => [...document.querySelectorAll('.gnode .shape')].filter(s => s.style.transform).length);
      out('fisheye grows nodes near the cursor', fish > 0, { magnified: fish });
      await page.mouse.down(); await page.mouse.move(bb.x + target.sx + 50, bb.y + target.sy + 25, { steps: 4 }); await page.mouse.up();
      const p1 = await page.evaluate(id => window.__memoryGraph.state.pos[id], target.id);
      out('drag a node moves it', Math.abs(p1.x - target.p.x) > 5, { id: target.id, dx: Math.round(p1.x - target.p.x), dy: Math.round(p1.y - target.p.y) });
    }
  }
  out('no page errors', errors.length === 0, { errors });
  await browser.close();
  process.exit(ok ? 0 : 1);
})();
