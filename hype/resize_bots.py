#!/usr/bin/env python3
import os
from PIL import Image

TARGET_WIDTH = 750
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SELF_NAME = os.path.basename(__file__)

for fname in sorted(os.listdir(SCRIPT_DIR)):
    if fname == SELF_NAME:
        continue
    path = os.path.join(SCRIPT_DIR, fname)
    if not os.path.isfile(path):
        continue

    name, ext = os.path.splitext(fname)
    if ext.lower() not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"):
        continue

    try:
        img = Image.open(path)
        img.load()
    except Exception as e:
        print(f"skip {fname}: {e}")
        continue

    if img.mode not in ("RGBA", "RGB"):
        img = img.convert("RGBA")

    w, h = img.size
    new_h = round(h * (TARGET_WIDTH / w))
    img = img.resize((TARGET_WIDTH, new_h), Image.LANCZOS)

    out_path = os.path.join(SCRIPT_DIR, name + ".png")
    img.save(out_path, "PNG")

    if os.path.abspath(path) != os.path.abspath(out_path):
        os.remove(path)

    print(f"{fname} -> {name}.png ({TARGET_WIDTH}x{new_h})")

print("done")
