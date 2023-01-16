import re
from typing import Optional, NewType
from pydantic import BaseModel, validator


Field_type = NewType("FIELD_TYPE", str)


class MyModel(BaseModel):
    atr_1: Optional[str]
    atr_2: Optional[str]
    atr_3: Optional[str]
    atr_4: Optional[str]
    atr_5: Optional[str]
    atr_6: Optional[str]
    atr_7: Optional[str]
    atr_8: Optional[str]
    atr_9: Optional[str]
    atr_10: Optional[str]

    @validator('atr_1', 'atr_2', 'atr_3', 'atr_4', 'atr_5', 'atr_6', 'atr_7', 'atr_8', 'atr_9', 'atr_10')
    def validation(cls, v):
        test = {
            "date": r'^\d{4}\-\d\d\-\d\d$',
            "phone": r'^(\+7| 7)[ ][\s]*\d{3}[\s]\d{3}[\s ]\d{2}[\s ]\d{2}',
            "email": r'^[aA-zZ0-9]+@[a-z]+[.]{1}[a-z]+',
            "text": r'^(([аА-яЯaA-zZ]+([, .!?]+)))+'
        }

        for key, r in test.items():
            if re.match(r, v):
                return key
        return Field_type.__name__
