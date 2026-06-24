import os

from src.docx_parser import extract_docx_text
from src.ocr_engine import extract_image_text
from src.llm_extractor import extract_metadata


def process_document(file_path):

    extension = os.path.splitext(
        file_path
    )[1].lower()

    if extension == ".docx":

        text = extract_docx_text(
            file_path
        )

    else:

        text = extract_image_text(
            file_path
        )

#   debug
    print("Extracted Text:")
    print(text[:1000])    

    metadata = extract_metadata(
        text
    )

    return {
        "text": text,
        "metadata": metadata
    }