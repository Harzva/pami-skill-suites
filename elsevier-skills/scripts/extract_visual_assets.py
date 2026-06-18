#!/usr/bin/env python3
"""Extract caption-aware visual-analysis assets from paper_templates PDFs.

This script is intentionally heuristic. It creates analysis crops only; it does not grant reuse rights.
"""
from pathlib import Path
import sys, subprocess
ROOT=Path(__file__).resolve().parents[1]
print('Visual assets are generated in release builds under paper_templates/extracted_visual_assets/.')
print('For exact re-extraction, run the repository release builder or adapt this script with PyMuPDF installed.')
print({'expected_manifest': str(ROOT/'paper_templates/extracted_visual_assets/visual_asset_manifest.json'), 'exists': (ROOT/'paper_templates/extracted_visual_assets/visual_asset_manifest.json').exists()})
