# GeneralDeployment-Jetson

面向 **Jetson Orin Nano Super / Windows** 的 7x24 小时目标检测系统骨架工程，拆分为三个子项目：

- `frontend/`：Vue3 可视化前端（登录、图片检测、视频检测、检测记录、手动调整）。
- `backend/`：业务后端（账号、记录 CRUD、实时订阅、权限与审计）。
- `flask_service/`：模型执行服务（YOLO + PaddleOCR，双摄像头联动逻辑）。

## 核心业务流程

1. 摄像头 A：ROI 内目标停留超过 3 秒后触发目标识别。
2. 摄像头 B：并行执行 OCR。
3. 将“目标检测 + OCR”合并写入同一条记录。
4. 前端实时展示记录，并支持手动新增 / 修改 / 删除。

## 启动顺序（开发）

```bash
# 1) 后端
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# 2) Flask 模型服务
cd ../flask_service
pip install -r requirements.txt
python run.py

# 3) 前端
cd ../frontend
npm install
npm run dev
```

## 7x24 运行建议

- Jetson：使用 `systemd` 管理后端、flask_service、前端静态服务。
- Windows：使用 NSSM 或任务计划程序守护 Python/Node 进程。
- 生产库建议使用 PostgreSQL（开发默认 SQLite）。

详见 `deploy/` 目录模板。
