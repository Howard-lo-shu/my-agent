import json
import os

from src.utils import config

CHAT_FILE = config.DATA_DIR / "chat_memory.jsonl"
MAP_FILE = config.DATA_DIR / "map.json"
MAX_HISTORY = 100


def _load_json(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError:
        print(f"[memory] {path.name} is corrupted, starting fresh")
        return default


def _save_json(path, data):
    # 先寫暫存檔再替換，避免寫到一半中斷造成檔案損毀
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def load_chat(limit=MAX_HISTORY):
    if not CHAT_FILE.exists():
        return []
    history = []
    with open(CHAT_FILE, encoding="utf-8") as f:
        for line in f:
            try:
                history.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return history[-limit:]


def append_chat(user, agent):
    # JSONL：每輪只追加一行，不必重寫整份歷史
    CHAT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CHAT_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps({"user": user, "agent": agent}, ensure_ascii=False) + "\n")


def load_map():
    return _load_json(MAP_FILE, {})


def save_map(map_data):
    _save_json(MAP_FILE, map_data)
