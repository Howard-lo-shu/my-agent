import argparse


def main():
    parser = argparse.ArgumentParser(description="AI Agent Demo")
    parser.add_argument("mode", nargs="?", choices=["cli", "server"], default="cli",
                        help="cli: 啟動對話 agent（預設）；server: 啟動工具伺服器")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    if args.mode == "server":
        import uvicorn
        uvicorn.run("src.api.app:app", host=args.host, port=args.port)
    else:
        from src.agent.agent import run
        run()


if __name__ == "__main__":
    main()
