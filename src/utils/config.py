import os
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[2]


def _load_dotenv(path):
    # 簡易 .env 讀取：KEY=VALUE，# 開頭為註解，不覆蓋已存在的環境變數
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


_load_dotenv(PROJECT_DIR / ".env")

MCP_URL = os.getenv("MCP_URL", "http://127.0.0.1:8000")
MCP_TIMEOUT = float(os.getenv("MCP_TIMEOUT", "5"))
DATA_DIR = Path(os.getenv("AGENT_DATA_DIR", PROJECT_DIR / "data"))
LOG_DIR = Path(os.getenv("AGENT_LOG_DIR", PROJECT_DIR / "logs"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
