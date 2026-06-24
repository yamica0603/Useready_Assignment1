from pydantic import BaseModel


class AgreementMetadata(BaseModel):

    agreement_value: str

    agreement_start_date: str

    agreement_end_date: str

    renewal_notice_days: str

    party_one: str

    party_two: str