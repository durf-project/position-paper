// SVG -> PNG with Chromium (Playwright), for the Word export: node svg2png.mjs in.svg out.png
import fs from 'fs';
import path from 'path';
let chromium;
for (const p of ['playwright', '/opt/node-tools/node_modules/playwright/index.mjs']) {
  try { ({ chromium } = await import(p)); break; } catch (e) { /* try the next */ }
}
if (!chromium) { console.error('Playwright not found'); process.exit(1); }
const [svg, out] = process.argv.slice(2);
const b = await chromium.launch(fs.existsSync('/opt/pw-browsers/chromium') ? { executablePath: '/opt/pw-browsers/chromium' } : {});
const p = await b.newPage({ deviceScaleFactor: 2 });
await p.goto('file://' + path.resolve(svg));
const box = await p.evaluate(() => { const s = document.querySelector('svg'); const r = s.getBoundingClientRect(); return { width: Math.ceil(r.width), height: Math.ceil(r.height) }; });
await p.setViewportSize({ width: Math.max(box.width, 100), height: Math.max(box.height, 100) });
await p.locator('svg').screenshot({ path: out, omitBackground: false });
await b.close();
