# Adobe-India-Hackathon-round-2
# Adobe India Hackathon Round 2 – Connecting the Dots

This project extracts structured outlines (H1, H2, H3) from a PDF and generates a valid JSON output.

## 💡 Features
- Accepts a PDF file up to 50 pages
- Extracts:
  - Title
  - Headings: H1, H2, H3 (with level and page number)
- Outputs a JSON file like:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    ...
  ]
}
