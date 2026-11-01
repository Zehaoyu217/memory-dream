#!/usr/bin/env node
// Headless check of a generated viewer page (BUILD-GUIDE §5.9, bundle P8): node tests/viz_check.js <graph.html>
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
  await page.goto('file://' + file); await page.waitForTimeout(600);
  const time = await page.evaluate(() => ({ nodes: document.querySelectorAll('#lanes .node').length, edges: document.querySelectorAll('#lanes .edge').length, legends: document.querySelectorAll('#lanes .legend').length, toggles: document.querySelectorAll('#lanes .legend button.lg').length }));
  out('time view', time.nodes > 0 && time.legends === 2 && time.toggles > 2, time);
  const g = JSON.parse(await page.evaluate(() => document.getElementById('data-graph').textContent));
  const withList = (g.notes || []).find(n => (n.text || []).some(l => /^\s*[-*]\s/.test(l))) || (g.notes || [])[0];
  if (withList) {
    await page.evaluate(p => { location.hash = '#note=' + encodeURIComponent(p); }, withList.path); await page.waitForTimeout(500);
    const md = await page.evaluate(() => ({ md: !!document.querySelector('#pick .md'), items: document.querySelectorAll('#pick .md li, #pick .md p').length, agentCollapsed: !document.querySelector('#pick details.agent').open, pre: (document.querySelector('#pick pre') || {}).textContent.slice(0, 2) }));
    out('note rendered as markdown, agent view collapsed', md.md && md.items > 0 && md.agentCollapsed && md.pre === '▸ ', md);
  }
  await page.evaluate(() => window.__memoryGraph.setView('graph')); await page.waitForTimeout(1800);
  const graph = await page.evaluate(() => { const st = window.__memoryGraph.state; return { entities: st.nodes.length, arrows: st.edges.length, gnodes: document.querySelectorAll('#lanes .gnode').length, gedges: document.querySelectorAll('#lanes .gedge').length, legendRows: document.querySelectorAll('#lanes .legend').length }; });
  out('graph view', graph.gnodes === graph.entities && graph.gedges === graph.arrows && graph.legendRows === 2, graph);
  if (graph.entities) {
    const hidden = await page.evaluate(() => { const b = document.querySelector('#lanes .legend.nodes button.lg'); b.click(); const n = document.querySelectorAll('#lanes .gnode.off').length; b.click(); return n; });
    out('legend toggle hides a family', hidden > 0, { hidden });
  }
  out('no page errors', errors.length === 0, { errors });
  await browser.close();
  process.exit(ok ? 0 : 1);
})();
