from datetime import datetime
from pydantic import BaseModel

class RecordBase(BaseModel):
    detected_object: str
    ocr_text: str = ''
    status: str = 'pending'
    note: str = ''

class RecordCreate(RecordBase):
    pass

class RecordUpdate(BaseModel):
    detected_object: str | None = None
    ocr_text: str | None = None
    status: str | None = None
    note: str | None = None

class RecordOut(RecordBase):
    id: int
    camera_a_ts: datetime
    source: str

    class Config:
        from_attributes = True
