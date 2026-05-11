from pathlib import Path
from pypdf import PdfReader

BASE = Path(r"C:\Users\ADMIN\Desktop\new\DSBDA")

PDFS = {
    "DSBDAL.pdf": "DSBDAL.txt",
    "DSBDA MMCOE.pdf": "DSBDA_MMCOE.txt",
}

for pdf_name, txt_name in PDFS.items():
    pdf_path = BASE / pdf_name
    txt_path = BASE / txt_name
    reader = PdfReader(str(pdf_path))
    text_parts = []
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text() or ""
        text_parts.append(f"\n\n===== PAGE {i + 1} =====\n{page_text}")
    txt_path.write_text("\n".join(text_parts), encoding="utf-8")
    print(f"Extracted {pdf_name} -> {txt_name} ({len(reader.pages)} pages)")
