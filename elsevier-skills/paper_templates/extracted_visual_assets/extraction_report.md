# Visual Asset Extraction Report

- Release: v1.8.0
- Publisher: Elsevier
- Generated on: 2026-06-14
- Papers scanned: 6
- Assets extracted: 18
- Counts: `{'main_figure': 6, 'motivation_figure': 6, 'beautiful_table': 6}`

## Method

The extractor scans OA/template corpus PDFs, detects captions containing figure/table markers, and renders nearby page regions to PNG files. Main figure selection uses the first detected figure caption; motivation figure selection prefers captions with overview/framework/architecture/pipeline/method/proposed keywords; table selection prefers an early table with a descriptive caption.

## Limitation

The crops are heuristic and may contain surrounding text. This is intentional for analysis because captions and nearby context help evaluate visual communication patterns. For exact boundaries, manually re-crop from the original PDF.
