from src import tools
from src.utils import config


def test_unreachable_server(monkeypatch):
    monkeypatch.setattr(config, "MCP_URL", "http://127.0.0.1:9")
    assert tools.move("kitchen") == "[tool error] cannot reach MCP server at http://127.0.0.1:9"
    assert tools.status() == "[tool error] cannot reach MCP server at http://127.0.0.1:9"
