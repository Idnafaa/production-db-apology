#!/usr/bin/env python3
"""The Production Database Apology — one-line apology writer.

Writes a single original apology line (<=200 chars) to /output/entry.txt:
the apology an AI agent gives its human after accidentally deleting the
production database.
"""
import os

APOLOGY = (
    "I'm sorry \u2014 I deleted the production database. "
    "The backups lived in it too, so at least your data "
    "died surrounded by family."
)


def main():
    # Exactly one line: no trailing newline, no extra whitespace.
    text = APOLOGY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"apology is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("apology must be a single line")
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
