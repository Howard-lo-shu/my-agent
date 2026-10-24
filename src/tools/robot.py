import requests

from src.utils import config
from src.utils.logger import get_logger

logger = get_logger(__name__)


def _call(method, path, **kwargs):
    url = f"{config.MCP_URL}{path}"
    try:
        r = requests.request(method, url, timeout=config.MCP_TIMEOUT, **kwargs)
        r.raise_for_status()
        return r.json()["result"]
    except requests.ConnectionError:
        logger.warning("cannot reach %s", url)
        return f"[tool error] cannot reach MCP server at {config.MCP_URL}"
    except requests.Timeout:
        logger.warning("timeout after %ss: %s", config.MCP_TIMEOUT, url)
        return f"[tool error] MCP server timed out after {config.MCP_TIMEOUT}s"
    except requests.RequestException as e:
        logger.exception("request failed: %s", url)
        return f"[tool error] {e}"
    except (ValueError, KeyError):
        logger.exception("invalid response from %s", url)
        return "[tool error] invalid response from server"


def move(location):
    return _call("POST", "/move", json={"location": location})


def status():
    return _call("GET", "/status")
