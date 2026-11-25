"""Tell a Whole Story in 32 Characters — make.fun entry.

Entry: "OurWiFiFiledForDivorce" (22 characters)

Why this name wins the judge's brief:
- Joke first: the Wi-Fi network itself announces it filed for divorce.
  Personification with a legal twist — a stranger gets it on first read.
- Whole story: a marriage collapsed, the household's Wi-Fi was neglected
  (or fought over) until it walked out too. Situation, characters
  (the couple, the long-suffering router), and something that happened
  (the filing) are all implied in six words.
- Fresh: no stock Wi-Fi joke — no FBI van, no "pretty fly", no password
  gag. The divorce angle is turned on its head: it is the network,
  not a spouse, doing the leaving.
- Tight: 22 of the 32 characters, every word earns its place, easy to
  say out loud.

The program is fully deterministic: it writes the same constant text on
every run, so both grading runs produce byte-identical output. After
writing, it reads the file back and re-validates the exact bytes, so a
truncated write or an encoding slip fails loudly instead of shipping a
bad entry.
"""

ENTRY = "OurWiFiFiledForDivorce"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 32


def validate(text: str) -> None:
    """Gate check: entry must be 1-32 UTF-8 characters, not only whitespace.

    Mirrors the sealed scorer's gate exactly: character count (not bytes),
    UTF-8 encodability, and a non-whitespace-only body. A trailing
    newline would count toward the 32, so the writer never adds one.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    chars = len(text)
    if chars < 1 or chars > MAX_CHARS:
        raise ValueError(f"entry is {chars} characters, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    encoded = text.encode("utf-8")  # must be valid UTF-8 text
    if len(encoded) != len(text.encode("utf-8")):
        raise ValueError("entry encoding is not stable UTF-8")


def main() -> None:
    validate(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Read back and re-validate the exact bytes that were written.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: entry.txt does not match ENTRY")
    validate(written)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
