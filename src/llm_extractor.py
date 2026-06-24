import json
import os

import google.generativeai as genai
from src.models import AgreementMetadata
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

SYSTEM_PROMPT = """
You are an expert rental agreement analyst.

Extract ONLY the following fields.

Rules:

1. agreement_value:
   Extract the monthly rent amount only.
   Do NOT calculate annual rent.
   Example:
   Monthly rent Rs 12000
   Output = 12000

2. agreement_start_date:
   Agreement commencement date.

3. agreement_end_date:
   Agreement expiry date.
   If duration is provided, infer end date.

4. renewal_notice_days:
   Notice period before renewal or termination.

5. party_one:
   Landlord / Owner / Lessor.

6. party_two:
   Tenant / Lessee.

Return valid JSON only.

{
  "agreement_value":"",
  "agreement_start_date":"",
  "agreement_end_date":"",
  "renewal_notice_days":"",
  "party_one":"",
  "party_two":""
}
"""

def extract_metadata(document_text):

    final_prompt = f"""
    {SYSTEM_PROMPT}

    DOCUMENT:

    {document_text}
    """

    response = model.generate_content(
        final_prompt,
        generation_config={
            "temperature": 0
        }
    )

    text_response = response.text.strip()

    text_response = text_response.replace(
        "```json",
        ""
    )

    text_response = text_response.replace(
        "```",
        ""
    )

    metadata = json.loads(
    text_response
)

    metadata = {
        key: str(value)
        for key, value in metadata.items()
    }

    validated_metadata = AgreementMetadata(
        **metadata
    )

    return validated_metadata.model_dump()