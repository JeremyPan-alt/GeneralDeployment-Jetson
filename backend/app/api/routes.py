from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.record import RecordCreate, RecordOut, RecordUpdate
from app.services.records import create_record, delete_record, list_records, update_record

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/records', response_model=list[RecordOut])
def get_records(db: Session = Depends(get_db)):
    return list_records(db)

@router.post('/records', response_model=RecordOut)
def post_record(payload: RecordCreate, db: Session = Depends(get_db)):
    return create_record(db, payload)

@router.put('/records/{row_id}', response_model=RecordOut)
def put_record(row_id: int, payload: RecordUpdate, db: Session = Depends(get_db)):
    row = update_record(db, row_id, payload)
    if not row:
        raise HTTPException(status_code=404, detail='record not found')
    return row

@router.delete('/records/{row_id}')
def remove_record(row_id: int, db: Session = Depends(get_db)):
    ok = delete_record(db, row_id)
    if not ok:
        raise HTTPException(status_code=404, detail='record not found')
    return {'deleted': True}
