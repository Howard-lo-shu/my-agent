from src.agent.executor import execute
from src.agent.memory import append_chat, load_map
from src.utils.logger import get_logger

logger = get_logger(__name__)

MOVE_WORDS = {"move", "go"}
FILLER_WORDS = {"to", "the", "a"}
EXIT_WORDS = {"exit", "quit", "bye"}


def decide_action(user_input, map_memory):
    words = user_input.lower().split()

    if not words:
        return ("empty", None)

    # ===== 離開 =====
    if words[0] in EXIT_WORDS:
        return ("exit", None)

    # ===== 移動指令 =====
    if words[0] in MOVE_WORDS:
        targets = [w for w in words[1:] if w not in FILLER_WORDS]
        if not targets:
            return ("error", "Where should I go? e.g. 'move kitchen'")
        return ("move", targets[0])

    # ===== 查狀態 =====
    if "status" in words:
        return ("status", None)

    # ===== 記錄地圖 =====
    if words[:2] == ["remember", "map"]:
        if len(words) < 3:
            return ("error", "Which map? e.g. 'remember map factory_v1'")
        return ("remember_map", words[2])

    # ===== 查詢地圖 =====
    if "map" in words:
        return ("memory", map_memory.get("last_map", "No map"))

    return ("chat", None)


def run():
    map_memory = load_map()

    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        action, value = decide_action(user, map_memory)

        if action == "empty":
            continue
        if action == "exit":
            break

        reply = execute(action, value, map_memory)
        logger.info("action=%s value=%r reply=%r", action, value, reply)

        print("Agent:", reply)
        append_chat(user, reply)

    print("Agent: Bye!")
