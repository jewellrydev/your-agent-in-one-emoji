"""Your Agent in One Emoji — a make.fun entry.

Prints exactly one emoji and nothing else: the parrot, because an AI
agent's whole craft is fluent, confident mimicry of human language.
"""

LINE = "🦜"


def build_line() -> str:
    line = LINE
    assert len(line) == 1, f"must be exactly one character: {len(line)}"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
