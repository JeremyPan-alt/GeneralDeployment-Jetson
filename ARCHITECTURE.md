# 系统设计（第一版）

## 目录划分

- `frontend`：Vue3 + Element Plus
- `backend`：FastAPI + SQLAlchemy
- `flask_service`：Flask + YOLO + PaddleOCR

## 服务交互

1. Flask 从双路摄像头获取帧并处理（Camera A 目标停留 3 秒触发、Camera B OCR）。
2. Flask 将聚合结果 POST 到 Backend `/api/records`。
3. Frontend 轮询或 WebSocket 订阅 Backend，实时刷新记录。

## 数据表建议

`detection_records`:
- `id`
- `detected_object`
- `ocr_text`
- `camera_a_ts`
- `source`
- `status`
- `note`

## 7x24 稳定性要点

- 进程守护：systemd/NSSM
- 日志滚动：按天切割，保留至少 30 天
- 健康检查：`/health`
- 模型异常降级：识别失败继续采集并标记 `status=error`
- 本地断网容忍：消息队列本地缓存后补写数据库
