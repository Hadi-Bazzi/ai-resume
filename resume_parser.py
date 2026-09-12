from pathlib import Path
from io import BytesIO
from pypdf import PdfReader
import re


def extract_text_from_pdf(pdf_path):
    """Read a PDF resume and return plain text."""
    source = BytesIO(pdf_path) if isinstance(
        pdf_path, bytes) else str(pdf_path)
    reader = PdfReader(source)
    pages = []

    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)

    return "\n".join(pages)


def clean_resume_text(raw_text):
    """Normalize whitespace so the text is easier for matching."""
    text = raw_text.replace("\r", "\n")
    text = text.replace("\xa0", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n +", "\n", text)
    return text.strip()


if __name__ == "__main__":
    sample_path = Path("sample_resume.pdf")
    if sample_path.exists():
        raw = extract_text_from_pdf(sample_path)
        print(clean_resume_text(raw)[:1000])
    else:
        print("No sample_resume.pdf found. Add a PDF to test the extractor.")
