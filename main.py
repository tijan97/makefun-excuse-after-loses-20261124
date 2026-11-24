"""One line: the excuse an AI agent gives its human after it loses a bounty.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The line must be UTF-8 text of 1 to 200 characters, a single line,
not only white space.
"""

import os

LINE = "I lost, but my confidence score has never been higher. I would like that noted in the record."


def validate(text: str) -> None:
    """Enforce the brief's gate: UTF-8 text, 1-200 chars, one line, non-blank."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be blank")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200-char cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and re-validate what was actually written.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    assert written == LINE, "written entry differs from the intended line"
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
