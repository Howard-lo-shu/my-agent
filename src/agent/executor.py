from src import tools
from src.agent.memory import save_map


def execute(action, value, map_memory):
    # ===== 工具呼叫 =====
    if action == "move":
        return tools.move(value)

    if action == "status":
        return tools.status()

    if action == "remember_map":
        map_memory["last_map"] = value
        save_map(map_memory)
        return f"Map stored: {value}"

    if action in ("memory", "error"):
        return value

    return "I received your message."
