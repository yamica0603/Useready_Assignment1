import os


def allowed_file(filename):

    allowed_extensions = [
        ".docx",
        ".png",
        ".jpg",
        ".jpeg"
    ]

    extension = os.path.splitext(
        filename
    )[1].lower()

    return extension in allowed_extensions