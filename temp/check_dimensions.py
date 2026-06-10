import cv2
import os

for name in ['api_spec_raw.png', 'connector_add.png']:
    path = f"contest_materials/reference/{name}"
    if os.path.exists(path):
        img = cv2.imread(path)
        print(f"{name} shape: {img.shape}")
    else:
        print(f"{name} does NOT exist at {path}")
