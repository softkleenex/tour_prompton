import csv

for name in ['api_spec_raw_ocr', 'connector_add_ocr']:
    path = f"scripts/{name}.tsv"
    print(f"=== {name} ===")
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
            if len(text) >= 6: # 6글자 이상인 것 다 출력해서 눈으로 확인
                print(f"'{text}' at L:{row[idx_left]} T:{row[idx_top]} W:{row[idx_width]} H:{row[idx_height]}")
