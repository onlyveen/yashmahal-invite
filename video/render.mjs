import { chromium } from 'playwright';
import { spawn } from 'child_process';
const HS = process.env.HS; // optional: path to a Chromium/headless_shell binary
const mode = process.argv[2];
const b = await chromium.launch({ ...(HS ? { executablePath: HS } : {}), args:['--force-color-profile=srgb','--font-render-hinting=none'] });
const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
p.on('console', m => console.log('page:', m.text())); p.on('pageerror', e => console.log('ERR', e.message));
await p.goto('file://' + process.cwd() + '/index.html');
await p.evaluate(() => window.ready);
const stage = await p.$('#stage');
if (mode === 'stills') {
  for (const t of process.argv.slice(3).map(Number)) {
    await p.evaluate(t => window.renderAt(t), t);
    await stage.screenshot({ path: `stills/t${String(t).padStart(5,'0')}.png` });
  }
} else {
  const fps = 30, dur = await p.evaluate(() => window.DURATION);
  const N = Math.round(dur * fps);
  const ff = spawn('ffmpeg', ['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-c:v','mjpeg','-i','-',
    '-f','lavfi','-i','anullsrc=r=44100:cl=stereo',
    '-c:v','libx264','-preset','slow','-crf','20','-maxrate','6M','-bufsize','12M','-pix_fmt','yuv420p','-profile:v','high','-level','4.1',
    '-c:a','aac','-b:a','96k','-shortest','-movflags','+faststart', process.argv[3]], { stdio: ['pipe','inherit','inherit'] });
  const t0 = Date.now();
  for (let i = 0; i < N; i++) {
    await p.evaluate(t => window.renderAt(t), i / fps);
    const buf = await stage.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 150 === 0) console.log(`frame ${i}/${N} ${((Date.now()-t0)/1000).toFixed(0)}s`);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r));
}
await b.close();
