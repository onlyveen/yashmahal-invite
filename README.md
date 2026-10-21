# Yash Mahal · Gruhapravesham invite

Scroll-through web invitation and video invite for the Gruhapravesham of **Yash Mahal**,
Sunday, 22 November 2026, hosted by Smt. Tejashwini A. & Sri Purushotham S. Raju.

- **Website:** `index.html` is a single self-contained page. Open it directly or serve it with GitHub Pages.
  As you scroll, the door opens, then the blessings, hosts, programme (with a live muhurtha countdown
  and Google Calendar link), venue (Maps link + QR), contacts and closing card appear.
- **Video:** `assets/yash-mahal-invite.mp4` (1080×1920, 45 s, WhatsApp-ready, silent).
- **Link preview:** `assets/og-image.jpg` is the WhatsApp/social preview card.

## Layout

```
index.html            built website (do not edit by hand)
site/src.html         website source (markup, styles, scroll animation)
site/build.py         inlines the artwork from art/ and writes ../index.html
video/src.html        video scenes (GSAP timeline)
video/build.py        inlines artwork -> video/index.html
video/render.mjs      frame-accurate render with Playwright + ffmpeg
art/                  line art traced from the printed card, QR code, paper texture
assets/               rendered video and preview image
```

## Rebuild

Website:

```sh
cd site && python3 build.py
```

Video (needs Node 18+, Python 3 and ffmpeg):

```sh
cd video
npm install
npx playwright install chromium
npm run render        # writes video/out/yash-mahal-invite.mp4
```

The site loads GSAP 3.12.5 from cdnjs and its fonts (Great Vibes, Lora, Cinzel) from Google Fonts.
