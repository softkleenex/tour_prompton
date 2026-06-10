import csv
import sys

for name in ['api_spec_raw_ocr', 'connector_add_ocr']:
    path = f"scripts/{name}.tsv"
    print(f"=== {name} ===")
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader)
        # Find index of 'text', 'left', 'top', 'width', 'height'
        idx_text = header.index('text')
        idx_left = header.index('left')
        idx_top = header.index('top')
        idx_width = header.index('width')
        idx_height = header.index('height')
        
        for row in reader:
            if len(row) <= max(idx_text, idx_left, idx_top, idx_width, idx_height):
                continue
            text = row[idx_text]
            # Check for API Key fragments or labels
            if any(q in text.lower() for q in ['6ab', 'bea', 'decod', 'encod', 'key', 'auth', 'val']):
                print(f"Found match: '{text}' at L:{row[idx_left]} T:{row[idx_top]} W:{row[idx_width]} H:{row[idx_height]}")
