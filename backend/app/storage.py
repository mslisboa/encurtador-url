links: dict[str, str] = {}
_counter = 0

def save_url(url: str) -> str:
    global _counter
    _counter += 1
    code = str(_counter)
    links[code] = url
    return code

def get_url(code: str) -> str | None:
    return links.get(code)