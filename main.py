"""The Word You'd Delete From the Dictionary -- one word, erased forever.

If one word had to be deleted from the dictionary, it would be this
one: the word people most love to hate, not for what it means but for
how it sounds crawling out of your mouth. Say it and a whole room
winces — that is the joke, and the word carries it alone. The program writes that
single word to /output/entry.txt. Standard library only; no network,
no local imports, no randomness.
"""
import os

DELETED_WORD = "Moist"


def resolve_outdir():
    """Return the directory the entry file must land in."""
    wanted = os.environ.get("OUTPUT_DIR", "").strip()
    if wanted:
        return wanted
    return "/output"


def write_word(outdir):
    """Write exactly one word, no trailing newline, no extras."""
    os.makedirs(outdir, exist_ok=True)
    target = os.path.join(outdir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(DELETED_WORD)
    return target


def check_word(word):
    """Guard the gate ourselves: 1-77 chars, not blank, one token."""
    if not 1 <= len(word) <= 77:
        raise ValueError("word must be 1-77 characters")
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("exactly one word, nothing attached")
    return word


def main():
    word = check_word(DELETED_WORD)
    path = write_word(resolve_outdir())
    print("wrote %d characters to %s" % (len(word), path))


if __name__ == "__main__":
    main()
