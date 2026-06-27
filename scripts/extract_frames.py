"""Extract 150 evenly spaced frames from source video as WebP."""
import cv2
from pathlib import Path

VIDEO = Path(r"C:\Users\Alotyn\Downloads\Based_on_image_png_create_a.mp4")
OUT = Path(__file__).resolve().parent.parent / "public" / "frames"
FRAME_COUNT = 150

OUT.mkdir(parents=True, exist_ok=True)

cap = cv2.VideoCapture(str(VIDEO))
if not cap.isOpened():
    raise SystemExit(f"Cannot open video: {VIDEO}")

total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Video: {total} frames, {fps:.2f} fps, {width}x{height}")

indices = [int(i * (total - 1) / (FRAME_COUNT - 1)) for i in range(FRAME_COUNT)]

for i, frame_idx in enumerate(indices, start=1):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ok, frame = cap.read()
    if not ok:
        raise SystemExit(f"Failed to read frame {frame_idx}")
    out_path = OUT / f"frame_{i:03d}.webp"
    cv2.imwrite(str(out_path), frame, [cv2.IMWRITE_WEBP_QUALITY, 88])
    if i % 25 == 0 or i == FRAME_COUNT:
        print(f"Saved {i}/{FRAME_COUNT}")

cap.release()
print("Done.")
