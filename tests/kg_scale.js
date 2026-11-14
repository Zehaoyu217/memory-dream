#!/usr/bin/env node
// Headless check of the knowledge-graph page at scale: node tests/kg_scale.js <page.html>, for a page built from
// demo/knowledge-graph/make_big.py (20,000 things, 45,000 links). The page must answer at once and settle in the
// background: no task holds the main thread long, every island settles, search finds the most linked thing and its
// panel opens, a thing can be dragged, nothing errs. Needs Playwright with Chromium; one JSON line per check; exits 1
// on any failure. The budgets are loose (a CI runner draws on the CPU): they catch a layout that blocks the page again.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const file = path.resolve(process.argv[2] || 'big.html');
  const browser = await chromium.launch();
  const page = await (await browser.newContext({ viewport: { width: 1440, height: 900 } })).newPage(); const errors = [];
  page.on('pageerror', e => errors.push(String(e))); page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  await page.addInitScript(() => {                     // the longest the main thread is held, from the first script on
    window.__long = [];
    new PerformanceObserver(l => l.getEntries().forEach(e => window.__long.push(Math.round(e.duration)))).observe({ type: 'longtask', buffered: true });
  });
  let ok = true; const out = (name, pass, extra) => { ok = ok && pass; console.log(JSON.stringify({ check: name, pass, ...extra })); };
  await page.goto('file://' + file, { timeout: 120000 });
  const data = await page.evaluate(() => {
    const things = JSON.parse(document.getElementById('data-things').textContent), links = JSON.parse(document.getElementById('data-links').textContent);
    const deg = things.map(() => 0); links.forEach(l => { deg[l.s]++; deg[l.t]++; });
    const top = deg.indexOf(Math.max(...deg));
    return { things: things.length, links: links.length, hub: things[top].label, hubLinks: deg[top] };
  });
  const settled = await page.waitForSelector('#graph[data-settled]', { state: 'attached', timeout: 60000 }).then(() => true, () => false);
  const settledMs = settled ? await page.evaluate(() => +document.getElementById('graph').dataset.settled) : null;
  const longest = await page.evaluate(() => Math.max(0, ...window.__long));
  out('the page answers while it settles', longest < 2500, { things: data.things, links: data.links, longestTaskMs: longest });
  out('every island settles', settled && settledMs < 20000, { settledMs });
  if (!settled) { out('no page errors', errors.length === 0, { errors }); await browser.close(); process.exit(1); }
  await page.waitForTimeout(2500);                     // the last islands bloom
  await page.keyboard.press('/'); await page.keyboard.type(data.hub); await page.waitForTimeout(300);
  await page.keyboard.press('Enter'); await page.waitForTimeout(1500);
  const panel = await page.evaluate(() => ({ open: document.getElementById('detail').classList.contains('open'),
                                             name: (document.querySelector('#detail h2') || {}).textContent || '', rows: document.querySelectorAll('#detail li').length }));
  out('search finds the most linked thing; its panel opens', panel.open && panel.name === data.hub && panel.rows > 0, { ...panel, links: data.hubLinks });
  await page.keyboard.press('Escape'); await page.waitForTimeout(1600);
  let at = null;                                       // a thing under the pointer (its tooltip names it), near the middle
  for (let r = 0; r < 260 && !at; r += 9) for (let a = 0; a < 6.28 && !at; a += 0.5) {
    const x = Math.round(880 + r * Math.cos(a)), y = Math.round(470 + r * Math.sin(a));
    await page.mouse.move(x, y);
    if (await page.evaluate(() => !!document.querySelector('#graph .tip.on b'))) at = [x, y];
  }
  let moved = false;
  if (at) {
    const shot = () => page.screenshot({ clip: { x: at[0] - 90, y: at[1] - 90, width: 180, height: 180 } });
    const before = await shot();
    await page.mouse.down(); for (let s = 1; s <= 12; s++) await page.mouse.move(at[0] + 6 * s, at[1] + 3 * s); await page.mouse.up();
    await page.waitForTimeout(600);
    moved = !before.equals(await shot());
  }
  out('a thing can be dragged', !!at && moved, { at, moved });
  // tags: the legend colours by each column in turn, opens a value into the level under it, and search lights a value
  await page.mouse.move(700, 880);
  const chips = page.locator('#legend .cols button'), n = await chips.count(), cols = [];
  const before = await page.evaluate(() => window.__long.length);
  for (let c = 0; c < n; c++) {
    await chips.nth(c).click(); await page.waitForTimeout(700);
    cols.push(await page.evaluate(() => [...document.querySelectorAll('#legend .row .name')].slice(0, 2).map(e => e.textContent).join(', ')));
  }
  const switchMs = await page.evaluate(b => Math.max(0, ...window.__long.slice(b)), before);
  out('the legend colours by each tag column', n > 1 && new Set(cols).size === n && switchMs < 1500, { columns: n, firstRows: cols, longestTaskMs: switchMs });
  await chips.nth(0).click(); await page.waitForTimeout(700);
  await page.locator('#legend .row .open:not(.none)').first().click(); await page.waitForTimeout(300);
  const sub = await page.evaluate(() => [...document.querySelectorAll('#legend .row.sub .name')].map(e => e.textContent));
  if (sub.length) { await page.locator('#legend .row.sub .tag').first().hover(); await page.waitForTimeout(400); await page.mouse.move(700, 880); }
  out('a legend value opens into the level under it', sub.length > 0, { under: sub.slice(0, 4) });
  await page.keyboard.press('/'); await page.keyboard.type(sub[0] || 'a'); await page.waitForTimeout(300);
  const hit = await page.evaluate(() => { const li = document.querySelector('#search li'); return li ? { tag: !!li.querySelector('.ring'), text: li.textContent } : null; });
  await page.keyboard.press('Enter'); await page.waitForTimeout(600);
  const lit = await page.evaluate(() => document.querySelector('#search .box').classList.contains('lit'));
  out('search finds a tag value and lights its things', !!hit && hit.tag && lit, { hit, lit });
  await page.keyboard.press('Escape'); await page.waitForTimeout(300);
  // a text tag (a definition): no colour chip of its own; search finds a thing by its words; the panel shows them
  const text = await page.evaluate(() => {
    const cols = JSON.parse(document.getElementById('data-columns').textContent), c = cols.find(x => x.text); if (!c) return null;
    const things = JSON.parse(document.getElementById('data-things').textContent), t = things.find(x => x.tags && x.tags[c.key]);
    return { key: c.key, name: c.name, label: t.label, words: String(t.tags[c.key]).split(' ').slice(-4).join(' '), chip: [...document.querySelectorAll('#legend .cols button')].some(b => b.textContent === c.name) };
  });
  if (text) {
    await page.keyboard.press('/'); await page.keyboard.type(text.words); await page.waitForTimeout(400);
    const first = await page.evaluate(() => { const li = document.querySelector('#search li'); return li ? { tag: !!li.querySelector('.ring'), name: li.querySelector('.name').textContent } : null; });
    await page.keyboard.press('Enter'); await page.waitForTimeout(1500);
    const shown = await page.evaluate(() => [...document.querySelectorAll('#detail .texts p')].map(p => p.textContent));
    out('a text tag is searched with its thing and shown in its panel', !text.chip && !!first && !first.tag && shown.some(p => p.includes(text.words)), { column: text.name, search: text.words, first, shown: shown.slice(0, 1) });
    await page.keyboard.press('Escape');
  } else out('a text tag is searched with its thing and shown in its panel', false, { error: 'no text column in the page' });
  // a time tag: its chip colours by year, the years in the order of time
  await page.waitForTimeout(400);
  const timeChip = await page.evaluate(() => { const cols = JSON.parse(document.getElementById('data-columns').textContent), c = cols.find(x => x.time); return c ? c.name : null; });
  if (timeChip) {
    await page.locator('#legend .cols button').filter({ hasText: timeChip }).click(); await page.waitForTimeout(800);
    const years = await page.evaluate(() => [...document.querySelectorAll('#legend .row:not(.sub) .name')].map(e => e.textContent).filter(t => /^\d{4}$/.test(t)));
    out('a time tag reads in the order of time', years.length > 1 && years.join() === years.slice().sort().join(), { column: timeChip, years });
    await page.locator('#legend .cols button').first().click(); await page.waitForTimeout(700);
  } else out('a time tag reads in the order of time', false, { error: 'no time column in the page' });
  // a link's tags: found in search, its links lit; shown on each link row; a link with no direction in its own group
  const lt = await page.evaluate(() => { const m = JSON.parse(document.getElementById('data-meta').textContent), c = (m.link_columns || []).find(x => !x.text && !x.number && !x.time);
    if (!c) return null; const v = Object.entries(m.link_values[c.key]).sort((a, b) => a[1] - b[1])[0]; return { name: c.name, value: v[0], n: v[1] }; });
  if (lt) {
    await page.keyboard.press('/'); await page.keyboard.type(lt.value); await page.waitForTimeout(400);
    const linkHit = page.locator('#search li button').filter({ hasText: / links?$/ }).first(), found = await linkHit.count();
    if (found) { await linkHit.click(); await page.waitForTimeout(700); }
    const litLinks = await page.evaluate(() => document.querySelector('#search .box').classList.contains('lit'));
    out('a link tag found in search lights its links', found > 0 && litLinks, { column: lt.name, value: lt.value, links: lt.n });
    await page.keyboard.press('Escape'); await page.mouse.click(700, 880); await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  } else out('a link tag found in search lights its links', false, { error: 'no link tag in the page' });
  const both = await page.evaluate(() => { const ts = JSON.parse(document.getElementById('data-things').textContent), ls = JSON.parse(document.getElementById('data-links').textContent);
    const l = ls.find(x => x.dir === 0); return l ? ts[l.s].label : null; });
  if (both) {
    await page.keyboard.press('/'); await page.keyboard.type(both); await page.waitForTimeout(400);
    const row = page.locator('#search li button').filter({ hasNot: page.locator('.ring') }).first();
    if (await row.count()) await row.click(); else await page.keyboard.press('Enter');
    await page.waitForTimeout(1500);
    const p = await page.evaluate(() => ({ groups: [...document.querySelectorAll('#detail h3')].map(h => h.textContent.trim()), tags: [...document.querySelectorAll('#detail .ltags')].map(e => e.textContent) }));
    out('a link with no direction sits in its own ↔ group', p.groups.some(g => g.startsWith('↔')), { thing: both, groups: p.groups.slice(0, 4) });
    out("a link's tags show on its row", p.tags.length > 0 && p.tags.every(t => t.length > 0), { first: p.tags.slice(0, 2) });
    await page.keyboard.press('Escape');
  } else out('a link with no direction sits in its own ↔ group', false, { error: 'no link without a direction' });
  out('no page errors', errors.length === 0, { errors });
  await browser.close();
  process.exit(ok ? 0 : 1);
})();
