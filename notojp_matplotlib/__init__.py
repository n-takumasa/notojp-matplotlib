from __future__ import annotations

from pathlib import Path

import matplotlib
from matplotlib.font_manager import fontManager

FONTSDIR = "fonts"
FILE = "NotoSansCJKjp-Regular.otf"
FAMILY = "Noto Sans CJK JP"

fontManager.addfont(Path(__file__).parent / FONTSDIR / FILE)
matplotlib.rc("font", family=FAMILY)
