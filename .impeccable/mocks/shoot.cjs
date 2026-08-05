const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const HTML = path.resolve('.impeccable/mocks/render.html');
const CSS = path.resolve('resources/css/app.css');
const OUT_DIR = path.resolve('.impeccable/mocks');

const css = fs.readFileSync(CSS, 'utf8');

(async () => {
  const browser = await chromium.launch();
  try {
    const desktop = await browser.newContext({
      viewport: { width: 1440, height: 900 },
      deviceScaleFactor: 2,
    });
    const mobile = await browser.newContext({
      viewport: { width: 390, height: 844 },
      deviceScaleFactor: 2,
    });

    for (const [name, ctx] of [['desktop', desktop], ['mobile', mobile]]) {
      const page = await ctx.newPage();
      await page.route('**/static/css/app.css', route => {
        route.fulfill({ status: 200, contentType: 'text/css', body: css });
      });
      await page.route('**/favicon.ico', route => route.abort());
      await page.goto('file:///' + HTML.replace(/\\/g, '/'));
      await page.waitForLoadState('networkidle');
      await page.waitForTimeout(500);

      const full = path.join(OUT_DIR, `welcome-${name}-full.png`);
      const above = path.join(OUT_DIR, `welcome-${name}-above.png`);
      await page.screenshot({ path: full, fullPage: true });
      await page.screenshot({ path: above, fullPage: false });
      console.log('shot', full);
      console.log('shot', above);
      await page.close();
    }
  } finally {
    await browser.close();
  }
})();
