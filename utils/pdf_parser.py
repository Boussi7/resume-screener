from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path: str) -> str:
    return extract_text(pdf_path)