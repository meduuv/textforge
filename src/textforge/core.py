def normalize(text: str) -> str:
    """Normalize whitespace without changing word content."""
    return " ".join(text.split())

def wrap(text: str, width: int) -> list[str]:
    """Wrap text at a maximum width."""
    if width <= 0: raise ValueError("width must be positive")
    words=normalize(text).split()
    lines=[]; current=""
    for word in words:
        if current and len(current)+1+len(word)>width:
            lines.append(current); current=word
        elif current: current += " "+word
        else: current=word
    if current: lines.append(current)
    return lines
