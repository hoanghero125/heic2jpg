import sys, subprocess, importlib, time
from pathlib import Path

def ensure_requirements():
    try:
        importlib.import_module("PIL")
        importlib.import_module("pillow_heif")
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

ensure_requirements()

from PIL import Image, ImageOps
import pillow_heif
pillow_heif.register_heif_opener()

input_dir = Path("source_heics")
output_dir = Path("converted_jpgs")

def main():
    if not input_dir.exists():
        input_dir.mkdir()
        print(f"[i] Created {input_dir}. Put HEIC files inside and run again.")
        return
    output_dir.mkdir(exist_ok=True)

    heics = [p for p in input_dir.iterdir() if p.suffix.lower() in (".heic", ".heif")]
    if not heics:
        print(f"[!] No HEIC/HEIF files found in {input_dir.resolve()}")
        return

    print(f"[i] Found {len(heics)} file(s). Start converting...")
    ok = fail = 0
    t0 = time.time()
    for src in heics:
        dst = output_dir / (src.stem + ".jpg")
        try:
            with Image.open(src) as im:
                im = ImageOps.exif_transpose(im)
                exif = im.info.get("exif")
                icc = im.info.get("icc_profile")
                im = im.convert("RGB")
                im.save(
                    dst,
                    "JPEG",
                    quality=100,
                    subsampling=0,  
                    optimize=True,   
                    exif=exif,
                    icc_profile=icc
                )
            print(f"✅ {src.name} -> {dst.name}")
            ok += 1
        except Exception as e:
            print(f"❌ {src.name} failed: {e}")
            fail += 1

    dt = time.time() - t0
    print(f"[done] {ok} converted, {fail} failed in {dt:.1f}s")
    print(f"[out]  {output_dir.resolve()}")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")