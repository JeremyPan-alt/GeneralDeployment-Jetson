import os
import requests
from flask import Blueprint, jsonify, request
from app.services.pipeline import process_event

api = Blueprint('api', __name__)
BACKEND_URL = os.getenv('BACKEND_URL', 'http://127.0.0.1:8000/api')

@api.get('/health')
def health():
    return jsonify({'status': 'ok'})

@api.post('/infer/event')
def infer_event():
    payload = request.get_json(silent=True) or {}
    result = process_event(payload.get('cameraA'), payload.get('cameraB'))

    requests.post(
        f'{BACKEND_URL}/records',
        json={
            'detected_object': result.detected_object,
            'ocr_text': result.ocr_text,
            'status': result.status,
            'note': result.note,
        },
        timeout=5,
    )
    return jsonify({'accepted': True, 'result': result.__dict__})
