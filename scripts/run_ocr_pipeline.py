import os
import subprocess
import unicodedata

# Native OCR binary
ocr_bin = "./ocr_mac"

folders = [
    {
        "dir": "contest_materials/01_프롬프톤_운영_OT_자료",
        "output": "01_운영_OT_추출텍스트.txt"
    },
    {
        "dir": "contest_materials/02_엔노이아_사용_OT_자료",
        "output": "02_엔노이아_사용_OT_추출텍스트.txt"
    }
]

print("Starting native OCR pipeline...")

for folder in folders:
    # Normalize folder path to NFC for safe loading on Mac
    nfc_dir = unicodedata.normalize('NFC', folder["dir"])
    nfd_dir = unicodedata.normalize('NFD', folder["dir"])
    
    target_dir = nfc_dir if os.path.exists(nfc_dir) else nfd_dir
    
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue
        
    print(f"\nProcessing folder: {target_dir}")
    
    # List and sort images
    images = [f for f in os.listdir(target_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    images.sort() # Sort to keep chronological slide order
    
    full_extracted_text = []
    
    for idx, img_name in enumerate(images):
        img_path = os.path.join(target_dir, img_name)
        print(f"[{idx+1}/{len(images)}] OCR Processing: {img_name}")
        
        # Call Apple Vision OCR compiled binary
        try:
            result = subprocess.run(
                [ocr_bin, img_path],
                capture_output=True,
                text=True,
                check=True
            )
            extracted = result.stdout.strip()
            
            full_extracted_text.append(f"\n\n=== Slide {idx+1} ({img_name}) ===")
            full_extracted_text.append(extracted)
        except subprocess.CalledProcessError as e:
            print(f"Error processing {img_name}: {e.stderr}")
            full_extracted_text.append(f"\n\n=== Slide {idx+1} ({img_name}) [ERROR] ===")
            
    # Save the output
    output_path = folder["output"]
    with open(output_path, "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(full_extracted_text))
    print(f"SUCCESS: Saved extracted text into {output_path}")

print("\nOCR Pipeline completed.")
