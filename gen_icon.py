"""生成应用图标：翡翠渐变圆角方块 + 白色准星（呼应面试主题）。
输出 assets/icon.ico（多尺寸）与 assets/icon.png（256）。"""
from PIL import Image, ImageDraw
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

TOP = (52, 211, 153)    # emerald 亮
BOT = (13, 148, 136)    # emerald 深


def make(size: int) -> Image.Image:
    s = size * 4  # 4x 超采样抗锯齿
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))

    # 渐变底 + 圆角蒙版
    grad = Image.new("RGBA", (s, s))
    gd = ImageDraw.Draw(grad)
    for y in range(s):
        t = y / max(s - 1, 1)
        c = tuple(int(TOP[i] + (BOT[i] - TOP[i]) * t) for i in range(3)) + (255,)
        gd.line([(0, y), (s, y)], fill=c)
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * 0.22), fill=255)
    img.paste(grad, (0, 0), mask)

    d = ImageDraw.Draw(img)
    # 白色准星圆环
    lw = max(int(s * 0.055), 2)
    d.ellipse([s * 0.27, s * 0.27, s * 0.73, s * 0.73], outline=(255, 255, 255, 255), width=lw)
    # 中心实心点
    d.ellipse([s * 0.445, s * 0.445, s * 0.555, s * 0.555], fill=(255, 255, 255, 255))
    # 四条短刻度线（准星感）
    c = s / 2
    tick = s * 0.10
    gap = s * 0.30
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x1 = c + dx * gap - (0 if dx else lw / 2)
        y1 = c + dy * gap - (lw / 2 if dx else 0)
        x2 = x1 + (tick * dx if dx else lw)
        y2 = y1 + (tick * dy if dy else lw)
        d.rounded_rectangle([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)], radius=lw / 2, fill=(255, 255, 255, 255))

    return img.resize((size, size), Image.LANCZOS)


base = make(256)
base.save(OUT / "icon.png")
base.save(OUT / "icon.ico", format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
print("icon generated:", OUT / "icon.ico")
