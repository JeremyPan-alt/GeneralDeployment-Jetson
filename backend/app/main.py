from fastapi import FastAPI
from app.api.routes import router
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Jetson Detection Backend')
app.include_router(router, prefix='/api')

@app.get('/health')
def health_check():
    return {'status': 'ok'}
