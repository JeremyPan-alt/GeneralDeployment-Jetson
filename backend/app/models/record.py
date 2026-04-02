from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func
from app.db.session import Base

class DetectionRecord(Base):
    __tablename__ = 'detection_records'

    id = Column(Integer, primary_key=True, index=True)
    detected_object = Column(String(128), nullable=False)
    ocr_text = Column(String(255), default='')
    camera_a_ts = Column(DateTime(timezone=True), server_default=func.now())
    source = Column(String(32), default='camera_pair')
    status = Column(String(32), default='pending')
    note = Column(Text, default='')
