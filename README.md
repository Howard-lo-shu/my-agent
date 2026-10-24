# AI Agent Demo

用文字指令控制機器人的簡易 agent：CLI agent 透過 HTTP 呼叫工具伺服器。

## 專案結構

```
ai_agent_demo/
├── README.md
├── requirements.txt
├── .env.example          # 環境變數範本（複製成 .env 使用，.env 不進版控）
├── .gitignore
├── pyproject.toml        # pytest 設定
├── main.py               # 進入點：CLI agent / 工具伺服器
├── src/
│   ├── agent/            # Agent 核心
│   │   ├── agent.py      # 指令解析（decide_action）與主迴圈
│   │   ├── executor.py   # 依 action 執行對應工具
│   │   └── memory.py     # 對話紀錄 / 地圖的讀寫
│   ├── tools/            # Agent 可用的工具
│   │   └── robot.py      # move / status（呼叫工具伺服器）
│   ├── utils/
│   │   ├── config.py     # 讀取 .env 與環境變數
│   │   └── logger.py     # 寫入 logs/agent.log
│   └── api/              # 工具伺服器（FastAPI）
│       ├── app.py        # FastAPI app
│       ├── routes.py     # /tools、/move、/status
│       └── schemas.py    # 請求 / 回應格式
├── tests/                # 單元測試（conftest 會把資料導向暫存目錄）
├── data/                 # 執行時資料：map.json、chat_memory.jsonl
└── logs/                 # 執行 log
```

## 執行

```bash
pip install -r requirements.txt
cp .env.example .env            # 第一次執行時

python main.py server           # 終端機 1：工具伺服器（預設 127.0.0.1:8000）
python main.py                  # 終端機 2：CLI agent
python -m pytest -q             # 測試
```

## 指令

| 指令 | 說明 |
|------|------|
| `move kitchen` / `go to kitchen` | 移動到指定地點 |
| `status` | 查詢機器人狀態 |
| `remember map <名稱>` | 記住地圖名稱 |
| `map` | 查詢目前地圖 |
| `exit` | 離開 |

## 環境變數（可寫在 `.env`）

| 變數 | 預設值 | 說明 |
|------|--------|------|
| `MCP_URL` | `http://127.0.0.1:8000` | 工具伺服器位址 |
| `MCP_TIMEOUT` | `5` | 請求逾時秒數 |
| `LOG_LEVEL` | `INFO` | log 等級 |
| `AGENT_DATA_DIR` | `./data` | 資料存放目錄 |
| `AGENT_LOG_DIR` | `./logs` | log 存放目錄 |
