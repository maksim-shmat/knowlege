"""Mistical difference import os and without import os."""

1. Add imporrt os

2. BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
2a. BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

3. STATICFILES_DIRS = [BASE_DIR/'staticfiles',]
3a. STATICFILE_DIRS = (os.path.join(BASE_DIR, 'staticfiles'),)
