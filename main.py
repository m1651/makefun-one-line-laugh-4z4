"""One Line, One Laugh — make.fun bounty entry.

Writes a single funny line of text to ``entry.txt`` in the output
directory given by ``MAKEFUN_OUTPUT_DIR`` (default ``/output``).

The line: a GPS that has heard itself say "recalculating" so many
times it stops navigating and starts offering life advice instead.
"""

import os

ENTRY_LINE = (
    "My GPS has said 'recalculating' so often it now just sighs "
    "and asks if I've considered staying home forever."
)


def validate_entry(line: str) -> None:
    """Enforce the bounty gate: 1-140 chars incl. trailing newline,
    single line, not only whitespace."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    total = len(line) + 1  # trailing newline
    if not 1 <= total <= 140:
        raise ValueError(
            f"entry must be 1-140 chars including trailing newline, got {total}"
        )


def main() -> None:
    """Write the entry line to entry.txt with a trailing newline."""
    validate_entry(ENTRY_LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")
    # Round-trip verification: read back and confirm bytes match exactly.
    with open(path, "rb") as f:
        written = f.read()
    expected = (ENTRY_LINE + "\n").encode("utf-8")
    if written != expected:
        raise SystemExit(
            f"round-trip verification failed: entry.txt bytes do not match "
            f"expected output ({len(written)} bytes read, {len(expected)} expected)"
        )


if __name__ == "__main__":
    main()
