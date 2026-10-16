# LinkedIn banner

- `linkedin-banner.png`: the banner on LinkedIn since October 16, 2026 (3168 x 792, twice LinkedIn's 1584 x 396).
- `linkedin-banner.html`: the SVG source. Render it with headless Chrome at 1584 x 396 and device scale factor 2.
- `gen.py`: the generator for this banner and the options tried before it (stars and hills are generated from fixed seeds).
- `previous-banner-toronto-800x200.jpg`: the Toronto skyline banner it replaced, saved at the only size LinkedIn served.

Style: inspired by Space Dandy's scenery (night sky, nebula, sparkle stars, rolling alien hills, crescent moon top right) with no characters or text. Colours: sky #0b1031 to #28205e to #2f6f8f to #53c6b8, hills #2a4f86, #18305f and #0b1435.

Render command:

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --force-device-scale-factor=2 --window-size=1584,396 --screenshot=linkedin-banner.png "file://$PWD/linkedin-banner.html"
```
