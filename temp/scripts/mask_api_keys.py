import cv2
import csv
import os

def mask_image(img_name, tsv_name):
    img_path = f"contest_materials/reference/{img_name}"
    tsv_path = f"scripts/{tsv_name}.tsv"
    
    if not os.path.exists(img_path) or not os.path.exists(tsv_path):
        print(f"Skipping {img_name} due to missing files")
        return
        
    img = cv2.imread(img_path)
    h, w, c = img.shape
    
    # Read TSV for bounding boxes
    boxes = []
    with open(tsv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader)
        idx_text = header.index('text')
        idx_left = header.index('left')
        idx_top = header.index('top')
        idx_width = header.index('width')
        idx_height = header.index('height')
        
        for row in reader:
            if len(row) <= idx_text:
                continue
            boxes.append({
                'text': row[idx_text].strip(),
                'left': int(row[idx_left]),
                'top': int(row[idx_top]),
                'width': int(row[idx_width]),
                'height': int(row[idx_height])
            })
            
    # Search for 'serviceKey' or 'Key' or 'e3ad46' and mask
    masked_count = 0
    
    # 1. Manual check fallback for api_spec_raw.png
    if img_name == 'api_spec_raw.png':
        # Mask the specific detected serviceKey value block (L:269 T:852 W:243 H:19)
        # We add some padding for safety
        cv2.rectangle(img, (260, 842), (540, 878), (30, 30, 30), -1) # Dark grey box
        masked_count += 1
        print("Applied manual fallback mask on api_spec_raw.png")

    # 2. Dynamic check based on serviceKey word
    for box in boxes:
        text_lower = box['text'].lower()
        # If the word itself seems like a raw API key (starts with e3ad46... or 6ab6ed...)
        if any(key_start in text_lower for key_start in ['e3ad46', '6ab6ed']):
            x1, y1 = box['left'], box['top']
            x2, y2 = x1 + box['width'], y1 + box['height']
            cv2.rectangle(img, (x1 - 5, y1 - 5), (x2 + 5, y2 + 5), (30, 30, 30), -1)
            masked_count += 1
            print(f"Masked key word: '{box['text']}' at {x1}, {y1}")
            
    # Save back
    cv2.imwrite(img_path, img)
    print(f"Finished masking {img_name}. Applied {masked_count} masks.")

mask_image('api_spec_raw.png', 'api_spec_raw_ocr')
mask_image('connector_add.png', 'connector_add_ocr')
