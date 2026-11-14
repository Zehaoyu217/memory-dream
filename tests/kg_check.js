#!/usr/bin/env node
// Headless check of the knowledge-graph page (_dream/knowledge-graph.html): node tests/kg_check.js <knowledge-graph.html>
// Needs Playwright with Chromium. Prints one JSON line per check; exits 1 on any page error or failed check.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const file = path.resolve(process.argv[2] || 'memory/_dream/knowledge-graph.html');
  const browser = await chromium.launch();
  const page = await (await browser.newContext({ viewport: { width: 1440, height: 900 } })).newPage(); const errors = [];
  page.on('pageerror', e => errors.push(String(e))); page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
  let ok = true; const out = (name, pass, extra) => { ok = ok && pass; console.log(JSON.stringify({ check: name, pass, ...extra })); };
  await page.goto('file://' + file); await page.waitForTimeout(4500);   // the entrance is over
  const data = await page.evaluate(() => ({ things: JSON.parse(document.getElementById('data-things').textContent),
                                            links: JSON.parse(document.getElementById('data-links').textContent).length }));
  const inked = await page.evaluate(() => { const c = document.querySelector('#graph canvas'), d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data; let n = 0; for (let i = 3; i < d.length; i += 64) if (d[i]) n++; return n; });
  out('graph drawn', data.things.length > 0 && data.links > 0 && inked > 200, { things: data.things.length, links: data.links, inked });
  const legend = await page.evaluate(() => document.querySelectorAll('#legend button').length);
  out('legend lists the groups', legend > 0, { legend });
  await page.keyboard.press('/'); await page.keyboard.type(data.things[0].label.slice(0, 12)); await page.waitForTimeout(200);
  await page.keyboard.press('Enter'); await page.waitForTimeout(1500);
  const panel = await page.evaluate(() => ({ open: document.getElementById('detail').classList.contains('open'),
                                             name: (document.querySelector('#detail h2') || {}).textContent || '', rows: document.querySelectorAll('#detail li').length }));
  out('search picks a thing; the panel shows its links', panel.open && panel.rows > 0, panel);
  const looks = [], black = {};
  for (const look of ['star', 'gala', 'moon', 'fanfare', 'noir', 'paper']) {   // each look, picked in the header, with a thing chosen
    await page.locator(`#masthead .looks button[data-look="${look}"]`).click(); await page.waitForTimeout(700);
    looks.push(await page.evaluate(() => document.documentElement.dataset.theme));
    black[look] = await page.evaluate(() => {   // a stroke or fill left without its colour draws pure black (0,0,0): no look has
      const c = document.querySelector('#graph canvas'), d = c.getContext('2d').getImageData(0, 0, c.width, c.height).data;   // any; noir's
      let n = 0; for (let i = 0; i < d.length; i += 16) if (d[i + 3] > 200 && d[i] + d[i + 1] + d[i + 2] < 12) n++; return n;   // halos are near-black on purpose
    });
  }
  out('the six looks switch', looks.join() === 'star,gala,moon,fanfare,noir,paper', { looks });
  out('no look draws stray black', Object.values(black).every(n => n < 20), { black });
  await page.keyboard.press('Escape'); await page.waitForTimeout(300);
  out('no page errors', errors.length === 0, { errors });
  await browser.close();
  process.exit(ok ? 0 : 1);
})();
