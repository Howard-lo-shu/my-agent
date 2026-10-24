import logging
from logging.handlers import RotatingFileHandler

from src.utils import config


def get_logger(name):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    # 只寫檔案，不輸出到終端機，避免干擾 CLI 對話
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    handler = RotatingFileHandler(
        config.LOG_DIR / "agent.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8"
    )
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(config.LOG_LEVEL)
    return logger
