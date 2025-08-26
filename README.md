
# HEIC2JPG
✍️ Created by [**Dek**](https://github.com/hoanghero125)  
📜 Licensed under the [**MIT License**](https://github.com/hoanghero125/heic2jpg/blob/main/LICENSE)

A simple Python script to convert images from **HEIC/HEIF format** (commonly used by iPhones) into standard **JPG** format (Quality + Information preserved).  

*Note: This repo is designed for **local use (Windows)***.

**Google Collab**: [**`heic2jpeg`**](https://colab.research.google.com/drive/1UYbJgN37I_JhlLoeE0pRgOMv7_wJZ2gA?authuser=1#scrollTo=Khi7LWXK3SqR)

---

## 📂 Folder Structure
```

heic2jpeg/
├── converted_jpgs/         # Output folder for converted JPG files
├── source_heics/           # Place your HEIC files here
├── heic2jpeg.bat           # Double-click to run the converter (Windows)
├── script.py               # Core Python script used by the batch file
├── requirements.txt        # Dependencies
└── README.md
```

---

## ⚙️ Setup

1. Run **`heic2jpeg.bat`** for the first time.  
   - It will create the folder **`source_heics/`**.

2. Place your `.heic` / `.heif` files into the **`source_heics/`** folder.  

3. Run **`heic2jpeg.bat`** again.  
   - All `.heic` / `.heif` files will be converted to `.jpg`.  
   - The converted images will be saved in the **`converted_jpgs/`** folder.  

---

## 📦 Dependencies

Dependencies are listed in [**`requirements.txt`**](requirements.txt).

```
pillow
pillow-heif
```