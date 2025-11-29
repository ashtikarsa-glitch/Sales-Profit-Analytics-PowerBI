# scripts/generate_banner.py
# Generates a black-grey gradient banner with white Calibri text (font size 28).
# Usage: python scripts/generate_banner.py
# If Calibri is not installed on your system, place a Calibri .ttf file
# (e.g. "calibri.ttf") in the same folder and update FONT_PATH below.

from PIL import Image, ImageDraw, ImageFont
import os

# Output path
OUT_DIR = "assets"
OUT_FILE = "banner.png"
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, OUT_FILE)

# Banner dimensions (wide for GitHub READMEs)
WIDTH = 1600
HEIGHT = 420

# Text settings
TITLE = "SALES & PROFIT ANALYTICS DASHBOARD"
SUBTITLE = "MICROSOFT POWER BI - BUSINESS INTELLIGENCE PROJECT"

# Requested font and size
FONT_NAME = "Calibri"            # name for clarity; we try to load .ttf below
FONT_PATH_CANDIDATES = [
    "/usr/share/fonts/truetype/msttcorefonts/Calibri.ttf",  # typical linux location (if ms corefonts installed)
    "/usr/share/fonts/truetype/calibri/calibri.ttf",
    "./calibri.ttf",                                       # local ttf (place file in repo)
    "C:\\Windows\\Fonts\\calibri.ttf",                     # windows path
]
TITLE_SIZE = 28  # as requested
SUBTITLE_SIZE = 20

# Build gradient background (black -> dark grey)
def create_gradient(width, height, top_color=(20,20,20), bottom_color=(60,60,60)):
    base = Image.new('RGB', (width, height), top_color)
    top_r, top_g, top_b = top_color
    bot_r, bot_g, bot_b = bottom_color
    for y in range(height):
        t = y / (height - 1)
        r = int(top_r + (bot_r - top_r) * t)
        g = int(top_g + (bot_g - top_g) * t)
        b = int(top_b + (bot_b - top_b) * t)
        for x in range(width):
            base.putpixel((x, y), (r, g, b))
    return base

# Try to load Calibri from candidates, otherwise fallback to a default font
def load_font(candidates, size):
    for p in candidates:
        if os.path.isfile(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    # fallback
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)  # common on many systems
    except Exception:
        return ImageFont.load_default()

def draw_centered_text(draw, text, font, image_width, y_pos, fill=(255,255,255)):
    # Get bounding box and center the text
    bbox = draw.textbbox((0,0), text, font=font)
    text_w = bbox[2] - bbox[0]
    x = (image_width - text_w) / 2
    draw.text((x, y_pos), text, font=font, fill=fill)

def main():
    # Create background
    bg = create_gradient(WIDTH, HEIGHT, top_color=(10,10,10), bottom_color=(50,50,50))
    draw = ImageDraw.Draw(bg)

    # Load fonts
    title_font = load_font(FONT_PATH_CANDIDATES, TITLE_SIZE)
    subtitle_font = load_font(FONT_PATH_CANDIDATES, SUBTITLE_SIZE)

    # Compute vertical positions (simple layout)
    # Center title roughly in upper half and subtitle below it
    title_bbox = draw.textbbox((0,0), TITLE, font=title_font)
    title_h = title_bbox[3] - title_bbox[1]
    subtitle_bbox = draw.textbbox((0,0), SUBTITLE, font=subtitle_font)
    subtitle_h = subtitle_bbox[3] - subtitle_bbox[1]

    total_text_height = title_h + 12 + subtitle_h
    start_y = (HEIGHT - total_text_height) / 2

    # Draw text (white)
    draw_centered_text(draw, TITLE, title_font, WIDTH, start_y, fill=(255,255,255))
    draw_centered_text(draw, SUBTITLE, subtitle_font, WIDTH, start_y + title_h + 12, fill=(230,230,230))

    # Save result
    bg.save(OUT_PATH, format="PNG")
    print(f"Banner saved to: {OUT_PATH}")

if __name__ == "__main__":
    main()
