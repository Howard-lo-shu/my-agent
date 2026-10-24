import os
import tempfile

# 測試時把資料與 log 導向暫存目錄，避免污染 data/ 與 logs/
_tmp = tempfile.mkdtemp(prefix="agent_test_")
os.environ["AGENT_DATA_DIR"] = os.path.join(_tmp, "data")
os.environ["AGENT_LOG_DIR"] = os.path.join(_tmp, "logs")
