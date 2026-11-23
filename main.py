"""Make the AI Judge Laugh: Office Jokes.

Writes one one-line joke about office life to entry.txt.
The joke is the whole entry: no title, no commentary, nothing else.
"""

import os

JOKE = "We have a no-meeting Friday — it's just a calendar invite called 'Focus Time' with 14 people in it."

MAX_CHARS = 199


def _validate(text: str) -> None:
    # The gate: UTF-8 text of 1-199 characters, not only white space, one line.
    if not 1 <= len(text) <= MAX_CHARS or not text.strip():
        raise ValueError("joke must be 1-199 characters, not only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be exactly one line")


def main() -> None:
    """Write the one-line joke to entry.txt, byte-identical every run."""
    _validate(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    # Write the joke and nothing else: no title, and no trailing newline,
    # so the entry stays exactly one line of 1-199 characters.
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
