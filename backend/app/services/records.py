from sqlalchemy.orm import Session
from app.models.record import DetectionRecord
from app.schemas.record import RecordCreate, RecordUpdate

def list_records(db: Session):
    return db.query(DetectionRecord).order_by(DetectionRecord.id.desc()).all()

def create_record(db: Session, payload: RecordCreate):
    row = DetectionRecord(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

def update_record(db: Session, row_id: int, payload: RecordUpdate):
    row = db.query(DetectionRecord).filter(DetectionRecord.id == row_id).first()
    if not row:
        return None
    for key, value in payload.model_dump(exclude_none=True).items():
        setattr(row, key, value)
    db.commit()
    db.refresh(row)
    return row

def delete_record(db: Session, row_id: int):
    row = db.query(DetectionRecord).filter(DetectionRecord.id == row_id).first()
    if not row:
        return False
    db.delete(row)
    db.commit()
    return True
