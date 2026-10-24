from src.agent import memory


def test_memory_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(memory, "CHAT_FILE", tmp_path / "chat.jsonl")
    monkeypatch.setattr(memory, "MAP_FILE", tmp_path / "map.json")

    memory.save_map({"last_map": "工廠"})
    assert memory.load_map() == {"last_map": "工廠"}

    memory.append_chat("你好", "hi")
    memory.append_chat("move kitchen", "ok")
    assert memory.load_chat() == [
        {"user": "你好", "agent": "hi"},
        {"user": "move kitchen", "agent": "ok"},
    ]
    assert memory.load_chat(limit=1) == [{"user": "move kitchen", "agent": "ok"}]


def test_corrupted_map(tmp_path, monkeypatch):
    bad = tmp_path / "map.json"
    bad.write_text("{not json", encoding="utf-8")
    monkeypatch.setattr(memory, "MAP_FILE", bad)
    assert memory.load_map() == {}
