import re
from datetime import datetime


def clean_name(name):

    name = str(name)

    # Remove titles

    name = re.sub(
        r"^(mr\.?|mrs\.?|ms\.?|sri)\s+",
        "",
        name,
        flags=re.IGNORECASE
    )

    # Remove punctuation

    name = re.sub(
        r"[^\w\s]",
        "",
        name
    )

    return (
        name
        .strip()
        .upper()
    )


def normalize_notice(value):

    value = str(value)

    value = re.sub(
        r"[^0-9]",
        "",
        value
    )

    return value


def normalize_date(date_str):

    date_str = str(date_str).strip()

    formats = [

        "%d.%m.%Y",

        "%Y-%m-%d",

        "%d/%m/%Y",

        "%d-%m-%Y",

        "%d %B %Y",

        "%d %b %Y"
    ]

    for fmt in formats:

        try:

            return datetime.strptime(
                date_str,
                fmt
            ).strftime("%Y-%m-%d")

        except:
            continue

    return date_str