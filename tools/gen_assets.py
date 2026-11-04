# -*- coding: utf-8 -*-
"""Generates all hand-designed SVG assets for the HaYToKoRaZ profile README.

Design system: "mission console" — dark panels, HUD corner brackets,
amber/teal accents, monospace type. One bold moment (the animated banner),
calm everywhere else (LED pulse only on cards).
"""
import os
import xml.etree.ElementTree as ET

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- tokens ----
VOID = "#0B1218"      # page-adjacent background
PANEL = "#101A22"     # card / panel fill
PANEL2 = "#0D161D"    # deeper panel (titlebars)
HAIR = "#1E2A33"      # hairline stroke
TEXT = "#D7E3E8"      # primary text
MUTE = "#8FA6B3"      # muted text
DIM = "#5A7280"       # dimmest text
AMBER = "#FFB000"     # primary accent
TEAL = "#2FE0C8"      # secondary accent
LED = "#3AD07A"       # live LED
FONT = "'Cascadia Code','Consolas','JetBrains Mono',Menlo,monospace"

def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def write_svg(name: str, body: str, w: int, h: int) -> None:
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" font-family="{FONT}">{body}</svg>'
    )
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    ET.fromstring(svg)  # validate well-formedness
    print(f"  ok {name}")

# ---------------------------------------------------------------- banner ----
def banner():
    grid = []
    for x in range(0, 1201, 48):
        grid.append(f'<line x1="{x}" y1="0" x2="{x}" y2="320" stroke="#111C25" stroke-width="1"/>')
    for y in range(0, 321, 48):
        grid.append(f'<line x1="0" y1="{y}" x2="1200" y2="{y}" stroke="#111C25" stroke-width="1"/>')
    grid = "".join(grid)

    lines_data = [
        ("> whoami", "HaYTo - solo developer", TEXT, "0.6s"),
        ("> ls products/", "7 extensions - 7 desktop apps", TEXT, "1.6s"),
        ("> status", "SHIPPING - ZERO TELEMETRY", TEAL, "2.6s"),
    ]
    lines = "".join(
        f'''
  <g style="opacity:0;animation:reveal .5s ease-out {d} forwards">
    <text x="60" y="{94 + i * 52}" font-size="15" font-weight="bold" fill="{AMBER}">{esc(c)}</text>
    <text x="60" y="{116 + i * 52}" font-size="14" fill="{oc}">{esc(o)}</text>
  </g>'''
        for i, (c, o, oc, d) in enumerate(lines_data)
    )

    body = f'''
<defs>
  <style>
    @keyframes reveal {{ to {{ opacity: 1; }} }}
    @keyframes blink {{ 0%,49% {{opacity:1;}} 50%,100% {{opacity:0;}} }}
    @keyframes caret {{ 0%,49% {{opacity:1;}} 50%,100% {{opacity:0;}} }}
    @keyframes scan {{ 0% {{transform:translateY(-70px);}} 100% {{transform:translateY(330px);}} }}
    @keyframes glA {{ 0%,90.5%,93.5%,100% {{opacity:0;}} 91%,93% {{opacity:.85;}} }}
    @keyframes glB {{ 0%,91.5%,94.5%,100% {{opacity:0;}} 92%,94% {{opacity:.85;}} }}
    .caret {{ animation: caret 1.05s steps(1) infinite; }}
    .scan {{ animation: scan 9s linear infinite; }}
    .glA {{ animation: glA 7s linear infinite; }}
    .glB {{ animation: glB 7s linear infinite; }}
  </style>
  <linearGradient id="scanG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{TEAL}" stop-opacity="0"/>
    <stop offset=".5" stop-color="{TEAL}" stop-opacity=".06"/>
    <stop offset="1" stop-color="{TEAL}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="fadeR" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{PANEL}" stop-opacity="1"/>
    <stop offset="1" stop-color="{VOID}" stop-opacity="0"/>
  </linearGradient>
</defs>

<rect width="1200" height="320" fill="{VOID}"/>
{grid}
<rect width="1200" height="320" fill="url(#fadeR)" opacity=".5"/>

<!-- console panel -->
<rect x="32" y="34" width="620" height="252" rx="12" fill="{PANEL}" stroke="{HAIR}"/>
<path d="M32 66 h620" stroke="{HAIR}"/>
<circle cx="56" cy="50" r="5" fill="{AMBER}"/>
<circle cx="74" cy="50" r="5" fill="{TEAL}"/>
<circle cx="92" cy="50" r="5" fill="{DIM}"/>
<text x="342" y="55" font-size="12" fill="{MUTE}" text-anchor="middle">C:\\HAYTO\\profile.exe</text>
{lines}
<rect class="caret" x="60" y="206" width="9" height="16" fill="{TEAL}"/>

<!-- wordmark -->
<text class="glA" x="681" y="168" font-size="86" font-weight="bold" fill="{TEAL}">HaYTo</text>
<text class="glB" x="685" y="164" font-size="86" font-weight="bold" fill="{AMBER}">HaYTo</text>
<text x="683" y="166" font-size="86" font-weight="bold" fill="{TEXT}">HaYTo</text>
<text x="686" y="204" font-size="17" fill="{MUTE}">// modern tech - retro soul</text>

<!-- status strip -->
<path d="M32 306 h1136" stroke="{HAIR}"/>
<text x="32" y="296" font-size="10" fill="{DIM}">14 PRODUCTS</text>
<text x="130" y="296" font-size="10" fill="{DIM}">100% OSS</text>
<text x="216" y="296" font-size="10" fill="{DIM}">MIT LICENSED</text>
<text x="1168" y="296" font-size="10" fill="{DIM}" text-anchor="end">ISTANBUL, TR</text>

<!-- hud corners -->
<path d="M14 30 v-16 h16" stroke="{AMBER}" stroke-width="2" fill="none" opacity=".8"/>
<path d="M1186 30 v-16 h-16" stroke="{AMBER}" stroke-width="2" fill="none" opacity=".8"/>
<path d="M14 290 v16 h16" stroke="{TEAL}" stroke-width="2" fill="none" opacity=".8"/>
<path d="M1186 290 v16 h-16" stroke="{TEAL}" stroke-width="2" fill="none" opacity=".8"/>

<!-- scanline -->
<rect class="scan" width="1200" height="70" fill="url(#scanG)"/>'''
    write_svg("banner.svg", body, 1200, 320)

# ---------------------------------------------------------------- cards -----
def icon_ext(acc):
    return f'''<g transform="translate(22,24)">
      <rect x="0" y="4.5" width="13" height="9" rx="2" fill="{acc}"/>
      <path d="M4.5 4.5 a3.2 3.2 0 1 1 4.5 0 z" fill="{acc}"/>
      <rect x="4" y="13.5" width="5" height="2.6" rx="1.2" fill="{acc}"/>
    </g>'''

def icon_app(acc):
    return f'''<g transform="translate(22,24)">
      <rect x="0" y="1" width="15" height="14" rx="2" fill="none" stroke="{acc}" stroke-width="1.6"/>
      <path d="M0 5 h15" stroke="{acc}" stroke-width="1.6"/>
      <circle cx="2.6" cy="3" r=".9" fill="{acc}"/>
      <circle cx="5.4" cy="3" r=".9" fill="{acc}"/>
    </g>'''

def icon_web(acc):
    return f'''<g transform="translate(22,24)">
      <rect x="0" y="2" width="15" height="11" rx="1.6" fill="none" stroke="{acc}" stroke-width="1.6"/>
      <path d="M5 13 l-1.5 3.5 M10 13 l1.5 3.5 M4 16.5 h7" stroke="{acc}" stroke-width="1.6" fill="none"/>
    </g>'''

def card(idx, name, tagline, accent, chips, icon):
    chip_x = 20
    chip_svgs = []
    for c in chips:
        w = 12 + len(c) * 5.6
        chip_svgs.append(f'''<g>
      <rect x="{chip_x}" y="92" width="{w:.0f}" height="17" rx="4" fill="{accent}" fill-opacity=".10" stroke="{accent}" stroke-opacity=".38"/>
      <text x="{chip_x + w / 2:.0f}" y="103.5" font-size="8.5" fill="{accent}" text-anchor="middle" letter-spacing=".5">{esc(c)}</text>
    </g>''')
        chip_x += w + 6
    chips_svg = "".join(chip_svgs)

    return f'''
<style>
  .led{idx:02d} {{ animation: pulse{idx:02d} 2.4s ease-in-out infinite; }}
  @keyframes pulse{idx:02d} {{ 0%,100% {{opacity:1;}} 50% {{opacity:.25;}} }}
</style>
<rect width="250" height="130" rx="10" fill="{PANEL}" stroke="{HAIR}"/>
<path d="M7 15 v-8 h8" stroke="{accent}" stroke-width="1.8" fill="none" opacity=".75"/>
<path d="M243 15 v-8 h-8" stroke="{accent}" stroke-width="1.8" fill="none" opacity=".75"/>
<path d="M7 115 v8 h8" stroke="{accent}" stroke-width="1.8" fill="none" opacity=".75"/>
<path d="M243 115 v8 h-8" stroke="{accent}" stroke-width="1.8" fill="none" opacity=".75"/>
{icon}
<text x="46" y="35" font-size="13" font-weight="bold" fill="{TEXT}">{esc(name)}</text>
<text x="232" y="35" font-size="8.5" fill="{DIM}" text-anchor="end">#{idx:02d}</text>
<text x="20" y="63" font-size="9.5" fill="{MUTE}">{esc(tagline)}</text>
{chips_svg}
<circle class="led{idx:02d}" cx="207" cy="100" r="3.2" fill="{LED}"/>
<text x="214" y="103.5" font-size="8.5" fill="{MUTE}" letter-spacing="1">LIVE</text>'''

def cta_card(label, sub, url_note):
    return f'''
<rect width="250" height="130" rx="10" fill="{PANEL2}" stroke="{TEAL}" stroke-dasharray="5 4" stroke-opacity=".55"/>
<text x="125" y="58" font-size="30" font-weight="bold" fill="{TEAL}" text-anchor="middle">+</text>
<text x="125" y="86" font-size="13" font-weight="bold" fill="{TEXT}" text-anchor="middle">{esc(label)}</text>
<text x="125" y="104" font-size="9.5" fill="{MUTE}" text-anchor="middle">{esc(sub)}</text>'''

EXTENSIONS = [
    ("RewriteAI", "Select text, rewrite with any AI key", TEAL, ["chrome", "edge"]),
    ("TabSuspender", "Park unused tabs, save up to 85% RAM", "#9D7CFF", ["chrome", "edge"]),
    ("XDownloader", "One-click X media at original quality", "#FF7847", ["chrome", "edge"]),
    ("WebTranslate", "Translate pages with six engines", "#4FC3F7", ["chrome", "edge"]),
    ("ExtensityPlus", "Every extension on/off in one click", AMBER, ["chrome", "edge"]),
    ("Cloud StartPage", "Minimal new-tab page, optional sync", "#FF5C8A", ["chrome", "edge"]),
    ("WhatsApp to Sahibinden", "WhatsApp listing to Sahibinden ad", "#3AD07A", ["chrome", "edge"]),
]

APPS = [
    ("WattCost", "Wall wattage to live electricity cost", AMBER, ["windows", "mit"]),
    ("Lol Account Switcher", "Millisecond Riot account switching", "#4FC3F7", ["windows", "mit"]),
    ("YouTube Download", "Follow channels by RSS, auto-download", "#FF5C8A", ["windows", "mit"]),
    ("Firewall", "Firewall rules as reusable profiles", "#FF7847", ["windows", "mit"]),
    ("FakeLord", "4,000+ games running, 0 MB GPU", "#9D7CFF", ["windows", "mit"]),
    ("Weather", "Live conditions in the system tray", "#7CFC9A", ["windows", "mit"]),
    ("Wallpaper", "Silent rotating wallpaper engine", TEAL, ["windows", "mit"]),
]

def generate_cards():
    for i, (name, tag, acc, chips) in enumerate(EXTENSIONS, 1):
        write_svg(f"card-ext-{i:02d}.svg", card(i, name, tag, acc, chips, icon_ext(acc)), 250, 130)
    for i, (name, tag, acc, chips) in enumerate(APPS, 1):
        write_svg(f"card-app-{i:02d}.svg", card(i, name, tag, acc, chips, icon_app(acc)), 250, 130)
    write_svg("card-web-portfolio.svg", card(8, "haytokoraz.github.io", "A working Windows 98 desktop", "#D7E3E8", ["vanilla", "no build"], icon_web(AMBER)), 250, 130)
    write_svg("card-cta-catalog.svg", cta_card("FULL CATALOG", "every extension and app", ""), 250, 130)

# ------------------------------------------------------------- titlebars ----
def titlebar(path, right, accent):
    return f'''
<rect width="840" height="42" rx="9" fill="{PANEL}" stroke="{HAIR}"/>
<circle cx="24" cy="21" r="4.5" fill="{AMBER}"/>
<circle cx="41" cy="21" r="4.5" fill="{TEAL}"/>
<circle cx="58" cy="21" r="4.5" fill="{DIM}"/>
<text x="80" y="26" font-size="13" font-weight="bold" fill="{TEXT}">{esc(path)}</text>
<text x="816" y="25" font-size="10" fill="{accent}" text-anchor="end" letter-spacing="1.5">{esc(right)}</text>
<path d="M826 8 v-4" stroke="{accent}" stroke-width="2" opacity="0"/>'''

# ------------------------------------------------------------------ stack ----
def stack_strip():
    items = [
        ("C# / .NET", AMBER), ("Python", "#4FC3F7"), ("JavaScript", "#FF7847"),
        ("HTML / CSS", "#FF5C8A"), ("Rust", "#9D7CFF"), ("Win32 API", TEAL),
        ("CachyOS Linux", "#7CFC9A"),
    ]
    x = 12
    parts = []
    for label, acc in items:
        w = 20 + len(label) * 6.4
        parts.append(f'''<g>
      <rect x="{x}" y="14" width="{w:.0f}" height="30" rx="15" fill="{acc}" fill-opacity=".08" stroke="{acc}" stroke-opacity=".4"/>
      <circle cx="{x + 16}" cy="29" r="3.5" fill="{acc}"/>
      <text x="{x + 26}" y="33" font-size="11.5" fill="{TEXT}">{esc(label)}</text>
    </g>''')
        x += w + 10
    return f'''
<rect width="840" height="58" rx="9" fill="{PANEL}" stroke="{HAIR}"/>
{"".join(parts)}'''

# ------------------------------------------------------------- terminal ----
def rules_terminal():
    rows = [
        ("keep it small", "one job done properly beats ten done badly"),
        ("measure it", "watts, ms, fps - numbers, not feelings"),
        ("stay private", "data stays local, cloud is opt-in only"),
        ("finish it", "unreleased perfect code is code nobody uses"),
    ]
    body = []
    y = 0
    for i, (k, v) in enumerate(rows):
        yy = 104 + i * 34
        body.append(f'''<text x="48" y="{yy}" font-size="13.5" font-weight="bold" fill="{AMBER}">{esc(k)}</text>
      <text x="200" y="{yy}" font-size="13.5" fill="{MUTE}">{esc(v)}</text>''')
    return f'''
<rect width="840" height="260" rx="12" fill="{PANEL}" stroke="{HAIR}"/>
<path d="M0 34 h840" stroke="{HAIR}"/>
<circle cx="24" cy="17" r="4.5" fill="{AMBER}"/>
<circle cx="41" cy="17" r="4.5" fill="{TEAL}"/>
<circle cx="58" cy="17" r="4.5" fill="{DIM}"/>
<text x="420" y="22" font-size="11.5" fill="{MUTE}" text-anchor="middle">hayto@dev: ~/rules</text>
<text x="48" y="68" font-size="13.5" fill="{TEAL}">$ cat rules.txt</text>
{"".join(body)}
<path d="M48 236 h744" stroke="{HAIR}" stroke-dasharray="3 4"/>
<text x="48" y="252" font-size="9.5" fill="{DIM}">exit 0 - every rule is enforced in the products above</text>'''

# ------------------------------------------------------------------ main ----
if __name__ == "__main__":
    print("generating profile assets:")
    banner()
    generate_cards()
    write_svg("sect-extensions.svg", titlebar("~/products/extensions", "7 modules - chromium - edge", TEAL), 840, 42)
    write_svg("sect-applications.svg", titlebar("~/products/applications", "7 modules - windows - linux", AMBER), 840, 42)
    write_svg("sect-telemetry.svg", titlebar("~/telemetry", "activity - stats - streak", TEAL), 840, 42)
    write_svg("sect-stack.svg", titlebar("~/stack", "daily drivers", AMBER), 840, 42)
    write_svg("stack.svg", stack_strip(), 840, 58)
    write_svg("rules.svg", rules_terminal(), 840, 260)
    print("done.")
