const { chromium } = require('playwright');
const path = require('path');
const OUT_DIR = path.resolve('.impeccable/mocks');

const PAGES = ['/login', '/register', '/password/forgot', '/404', '/maintenance'];

(async () => {
  const browser = await chromium.launch();
  try {
    const desktop = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
    const mobile = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });

    for (const [name, ctx] of [['desktop', desktop], ['mobile', mobile]]) {
      for (const url of PAGES) {
        const page = await ctx.newPage();
        await page.route('**/favicon.ico', route => route.abort());
        await page.goto('http://127.0.0.1:8000' + url, { waitUntil: 'networkidle' });
        await page.waitForTimeout(400);
        const slug = url.replace(/\//g, '_').replace(/^_/, '') || 'root';
        const full = path.join(OUT_DIR, `page-${name}-${slug}-full.png`);
        await page.screenshot({ path: full, fullPage: true });
        console.log('shot', full);
        await page.close();
      }
    }
  } finally {
    await browser.close();
  }
})();
