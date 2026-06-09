import sys
import os

try:
    from PIL import Image, ImageDraw
    print("PIL is available")
except ImportError:
    print("PIL is NOT available")
    sys.exit(1)

try:
    import pytesseract
    print("pytesseract is available")
except ImportError:
    print("pytesseract is NOT available")

try:
    import cv2
    import numpy as np
    print("opencv is available")
except ImportError:
    print("opencv is NOT available")
