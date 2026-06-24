from paddleocr import PaddleOCR

# Initialize OCR model
ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en"
)


def extract_image_text(image_path):

    result = ocr.ocr(image_path)

    print("\n========== RAW OCR RESULT ==========\n")
    print(result)
    print("\n===================================\n")

    extracted_text = ""

    try:

        # Format 1
        if isinstance(result, list):

            for item in result:

                # New PaddleOCR versions
                if isinstance(item, dict):

                    if "rec_texts" in item:

                        extracted_text += "\n".join(
                            item["rec_texts"]
                        )

                # Older PaddleOCR versions
                elif isinstance(item, list):

                    for line in item:

                        try:

                            text = line[1][0]

                            extracted_text += (
                                text + "\n"
                            )

                        except Exception:
                            pass

    except Exception as e:

        print("OCR Parsing Error:")
        print(e)

    print("\n========== EXTRACTED TEXT ==========\n")
    print(extracted_text[:2000])
    print("\n===================================\n")

    return extracted_text