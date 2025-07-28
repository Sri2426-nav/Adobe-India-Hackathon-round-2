import os
import fitz  # PyMuPDF
import json

# Define precise font sizes based on your document
FONT_THRESHOLDS = {
    "H1": 22,
    "H2": 16,
    "H3": 13.5
}

def determine_heading_level(font_size):
    if font_size >= FONT_THRESHOLDS["H1"]:
        return "H1"
    elif font_size >= FONT_THRESHOLDS["H2"]:
        return "H2"
    elif font_size >= FONT_THRESHOLDS["H3"]:
        return "H3"
    else:
        return None

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.basename(pdf_path).replace(".pdf", "").title()
    outline = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    line_text = ""
                    max_font_size = 0
                    for span in line["spans"]:
                        line_text += span["text"]
                        if span["size"] > max_font_size:
                            max_font_size = span["size"]

                    line_text = line_text.strip()
                    if not line_text:
                        continue

                    level = determine_heading_level(max_font_size)
                    if level:
                        outline.append({
                            "level": level,
                            "text": line_text,
                            "page": page_num + 1
                        })

    return {
        "title": title,
        "outline": outline
    }

# --- Main Execution ---
input_dir = "input"
output_dir = "output"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if file.endswith(".pdf"):
        pdf_path = os.path.join(input_dir, file)
        result = extract_headings(pdf_path)

        output_file = os.path.join(output_dir, file.replace(".pdf", ".json"))
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"✅ Processed {file} → {output_file}")
