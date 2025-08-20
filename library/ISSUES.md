# Backlog

## 1) Title: Add type hints and docstrings to public methods

**Labels:** enhancement, good first issue

**Body:**
Add concise docstrings (Google or NumPy style) to `Library` and `Book` methods and ensure all public methods have type hints.

**Acceptance Criteria:**
- Docstrings for `add_book`, `borrow_book`, `return_book`, `list_books`, `__init__`
- `mypy` passes with no errors (if configured later)

---

## 2) Title: Add search by author

**Labels:** enhancement, good first issue

**Body:**
Implement `search_by_author(author: str) -> list[Book]` (case-insensitive).

**Acceptance Criteria:**
- Returns matching books
- Unit tests cover multiple matches + no matches

---

## 3) Title: Prevent duplicate titles (optional flag)

**Labels:** enhancement

**Body:**
Add an optional flag to `Library.__init__(allow_duplicates: bool = True)` to control whether duplicate titles are allowed.

**Acceptance Criteria:**
- When `allow_duplicates=False`, adding same title raises `ValueError`
- Tests included

---

## 4) Title: Borrow should return which copy if duplicates exist

**Labels:** enhancement

**Body:**
When multiple identical titles exist, `borrow_book` should borrow the first available and return its index or identifier.

**Acceptance Criteria:**
- Return value changed to `(bool, int | None)` or similar minimal breaking change with tests
- README updated

---

## 5) Title: Add remove_book(title) API

**Labels:** enhancement, good first issue

**Body:**
Implement `remove_book(title: str) -> int` that removes all books with that title and returns how many were removed.

**Acceptance Criteria:**
- Works case-insensitive
- Tests for 0, 1, many removals

---

## 6) Title: Export library to JSON

**Labels:** enhancement

**Body:**
Add `to_json(path: str) -> None` that writes all books to disk.

**Acceptance Criteria:**
- JSON schema: `[{"title": "...", "author": "...", "is_available": true}]`
- Round-trip test with import

---

## 7) Title: Import library from JSON

**Labels:** enhancement

**Body:**
Add `from_json(path: str) -> None` to load books into the current library (append).

**Acceptance Criteria:**
- Handles empty/invalid files gracefully
- Tests for happy path and invalid JSON

---

## 8) Title: CLI: add, list, borrow, return

**Labels:** enhancement

**Body:**
Create a simple CLI using `argparse` with subcommands: `add`, `list`, `borrow`, `return`.

**Acceptance Criteria:**
- `python library.py add --title "Dune" --author "Frank Herbert"`
- `python library.py list` shows books
- Borrow/return by `--title`

---

## 9) Title: Make list_books return data as well as print

**Labels:** enhancement, refactor

**Body:**
Refactor `list_books()` to return a `list[str]` of lines while still printing (or create `get_books_str()` and keep print-only).

**Acceptance Criteria:**
- Backward compatibility maintained
- Tests assert return type/content

---

## 10) Title: Add __repr__ for Book for better debugging

**Labels:** enhancement, good first issue

**Body:**
Implement `__repr__` to show `Book(title='..', author='..', is_available=True)`.

**Acceptance Criteria:**
- `repr(Book(...))` matches format
- Small unit test

---

## 11) Title: Case-insensitive borrow/return should ignore leading/trailing spaces

**Labels:** bug, good first issue

**Body:**
Currently case-insensitive, but leading/trailing spaces should be stripped.

**Acceptance Criteria:**
- `"  dune  "` works same as `"Dune"`
- Tests added

---

## 12) Title: Add ISBN field (optional)

**Labels:** enhancement

**Body:**
Extend `Book` with optional `isbn: str | None = None`. Update `add_book` to accept it (keyword-only).

**Acceptance Criteria:**
- `add_book(title, author, isbn=None)`
- Printed string shows ISBN if present

---

## 13) Title: Sort listing by title

**Labels:** enhancement

**Body:**
Add `list_books_sorted(by: str = "title")` that prints sorted output by `title` or `author`.

**Acceptance Criteria:**
- Sorting stable and case-insensitive
- Tests for both keys

---

## 14) Title: Unit test suite with pytest

**Labels:** testing

**Body:**
Create `tests/` with pytest covering key paths: add/borrow/return/list, edge cases, duplicates flag.

**Acceptance Criteria:**
- ≥15 assertions
- CI-ready structure

---

## 15) Title: Pre-commit hooks (ruff + black)

**Labels:** tooling

**Body:**
Add pre-commit with `ruff` and `black` for lint/format.

**Acceptance Criteria:**
- `.pre-commit-config.yaml` present
- `pre-commit run --all-files` passes

---

## 16) Title: GitHub Actions: run tests on push/PR

**Labels:** CI

**Body:**
Add a simple workflow to run `pytest` on Python 3.10–3.12.

**Acceptance Criteria:**
- `/.github/workflows/ci.yml` added
- Badge in README

---

## 17) Title: Graceful messages for borrow/return failures

**Labels:** enhancement, UX

**Body:**
Provide helper that returns reason when borrow/return fails (e.g., "not found", "already borrowed").

**Acceptance Criteria:**
- New method `borrow_book_verbose(title) -> tuple[bool, str]`
- Tests for messages

---

## 18) Title: Add count of available vs borrowed

**Labels:** enhancement

**Body:**
Add `stats()` to return dict with counts: `{"total": n, "available": a, "borrowed": b}`.

**Acceptance Criteria:**
- Tested on empty, mixed libraries
- README updated

---

## 19) Title: Support partial title search

**Labels:** enhancement

**Body:**
Add `search_by_title(query: str) -> list[Book]` that matches substrings (case-insensitive).

**Acceptance Criteria:**
- Returns all partial matches
- Tests for multiple results

---

## 20) Title: Example data seeder script

**Labels:** documentation, enhancement, good first issue

**Body:**
Provide `seed.py` that populates a library with 8–10 famous books for demos.

**Acceptance Criteria:**
- Script runs without args
- README: how to run
