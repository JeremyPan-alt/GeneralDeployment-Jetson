# Windows 7x24 运行建议

1. 安装 Python 3.10+/Node.js 20+
2. 使用 NSSM 为以下命令创建服务：
   - `uvicorn app.main:app --host 0.0.0.0 --port 8000`
   - `python run.py`（flask_service）
   - 前端建议 `npm run build` 后由 nginx/IIS 托管
3. 配置服务自动重启、崩溃日志滚动、开机自启。
