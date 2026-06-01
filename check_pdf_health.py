import pypdf
import os

pdf_files = [
    "contest_materials/01_프롬프톤_운영_OT_자료.pdf",
    "contest_materials/02_엔노이아_사용_OT_자료.pdf"
]

print("Checking PDF integrity...")

for pdf_path in pdf_files:
    if not os.path.exists(pdf_path):
        print(f"ERROR: File does not exist at {pdf_path}")
        continue
        
    file_size = os.path.getsize(pdf_path)
    print(f"\nFile: {os.path.basename(pdf_path)} ({file_size} bytes)")
    
    try:
        reader = pypdf.PdfReader(pdf_path)
        pages_count = len(reader.pages)
        print(f"-> SUCCESS: Valid PDF! Total Pages: {pages_count}")
        # Try reading metadata or first page text preview
        if pages_count > 0:
            first_page = reader.pages[0]
            text = first_page.extract_text()
            preview = text.strip()[:100].replace('\n', ' ') if text else "No extractable text"
            print(f"-> Preview: {preview}...")
    except Exception as e:
        print(f"-> ERROR: Damaged or invalid PDF file. Details: {e}")
        # Let's check if it's actually an HTML error page inside
        try:
            with open(pdf_path, 'r', encoding='utf-8', errors='ignore') as f:
                head = f.read(200)
                if "<html" in head.lower() or "<!doctype" in head.lower():
                    print("-> Warning: This file seems to be an HTML page, not a true PDF. Might be a Google Drive download barrier.")
        except Exception:
            pass
