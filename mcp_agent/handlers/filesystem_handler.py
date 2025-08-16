def filesystem_handler(path: str):
    try:
        with open(path, "r") as f:
            data = f.read()
        return {"tool": "filesystem", "result": data}
    except Exception as e:
        return {"tool": "filesystem", "error": str(e)}
