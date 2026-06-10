import csv

path = "scripts/connector_add_ocr.tsv"
with open(path, 'r', encoding='utf-8') as f:
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
        text = row[idx_text].strip()
        if text:
            print(f"'{text}' at L:{row[idx_left]} T:{row[idx_top]} W:{row[idx_width]} H:{row[idx_height]}")
