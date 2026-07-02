"""Command-line entry point for the learning lab."""

from __future__ import annotations

import argparse

from learning_lab.collections_basics import count_words
from learning_lab.numbers import add_tax, average
from learning_lab.text_tools import slugify


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a small Python lesson.")
    parser.add_argument(
        "lesson",
        choices=["numbers", "collections", "text"],
        help="lesson to run",
    )
    return parser


def run_lesson(lesson: str) -> str:
    if lesson == "numbers":
        total = add_tax(25, 0.06)
        return f"$25.00 with tax is ${total:.2f}; average score is {average([85, 90, 95]):.1f}."
    if lesson == "collections":
        return f"Word counts: {count_words(['Python', 'tests', 'python'])}"
    if lesson == "text":
        return f"Slug: {slugify('Learning Python, One Step at a Time')}"
    raise ValueError(f"unknown lesson: {lesson}")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print(run_lesson(args.lesson))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
