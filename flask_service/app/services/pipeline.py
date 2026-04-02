"""模型流水线骨架：
- Camera A: ROI 进入并停留 >= 3 秒后执行 YOLO 检测
- Camera B: 并发 OCR
- 结果聚合后推送 backend
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class DetectionResult:
    detected_object: str
    ocr_text: str
    status: str
    note: str


def process_event(camera_a_frame, camera_b_frame) -> DetectionResult:
    # TODO: 接入 ultralytics YOLO 推理和区域停留计时器。
    # TODO: 接入 PaddleOCR 推理。
    # 这里先返回占位数据，方便前后端联调。
    return DetectionResult(
        detected_object='person',
        ocr_text='DEMO-OCR-001',
        status='pending_review',
        note=f'aggregated_at={datetime.utcnow().isoformat()}'
    )
