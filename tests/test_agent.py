import pytest

from src.agent import executor
from src.agent.agent import decide_action
from src.agent.executor import execute


@pytest.mark.parametrize("text, expected", [
    ("move kitchen", ("move", "kitchen")),
    ("go to the kitchen please", ("move", "kitchen")),
    ("Go Kitchen", ("move", "kitchen")),
    ("move", ("error", "Where should I go? e.g. 'move kitchen'")),
    ("good morning", ("chat", None)),
    ("google it", ("chat", None)),
    ("status", ("status", None)),
    ("remember map factory_v2", ("remember_map", "factory_v2")),
    ("remember map", ("error", "Which map? e.g. 'remember map factory_v1'")),
    ("map", ("memory", "factory_v1")),
    ("exit", ("exit", None)),
    ("   ", ("empty", None)),
])
def test_decide_action(text, expected):
    assert decide_action(text, {"last_map": "factory_v1"}) == expected


def test_map_without_memory():
    assert decide_action("map", {}) == ("memory", "No map")


def test_execute_remember_map(monkeypatch):
    saved = {}
    monkeypatch.setattr(executor, "save_map", saved.update)
    map_memory = {}
    assert execute("remember_map", "factory_v2", map_memory) == "Map stored: factory_v2"
    assert map_memory == saved == {"last_map": "factory_v2"}
