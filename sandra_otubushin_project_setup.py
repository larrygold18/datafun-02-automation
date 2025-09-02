"""
sandra_otubushin_project_setup.py
Author: Sandra Otubushin
Course: Data Analytics Fundamentals
Module 2 – Project Setup

Purpose
-------
This script is the main driver for the Module 2 project.
It demonstrates clean organization (Step 3) and implementation (Step 4):
- Planning/organization with comments and sections
- Functions that use branching, repetition, and REQUIRED comprehensions
- A clear main() driver that calls the functions with good arguments
- Conditional execution guard so main() only runs when executed directly
"""

# =====================================================
# 1) IMPORTS (keep these tidy and at the top)
# =====================================================
from __future__ import annotations
from datetime import datetime
import pathlib
import platform
import os
from typing import Iterable, List, Dict, Tuple, Set

# Optional: import your Module 1 helpers if you want to use them
# from utils_sandra_otubushin import some_helper  # noqa: F401


# =====================================================
# 2) CONSTANTS & PATHS (project-level configuration)
# =====================================================
PROJECT_ROOT: pathlib.Path = pathlib.Path(__file__).parent
DATA_DIR: pathlib.Path = PROJECT_ROOT / "data"
RESULTS_DIR: pathlib.Path = PROJECT_ROOT / "results"


# =====================================================
# 3) ORGANIZATION: SMALL, FOCUSED HELPER FUNCTIONS
#    (Plan with comments; fill in implementations.)
# =====================================================

def byline(
    author: str = "Sandra Otubushin",
    course: str = "Data Analytics Fundamentals",
    module: str = "Module 2 – Project Setup",
) -> str:
    """
    Return a single-line byline with context and environment info.
    """
    return (
        f"{author} | {course} | {module} | "
        f"{pathlib.Path(__file__).name} | "
        f"{datetime.now():%Y-%m-%d %H:%M} | Python {platform.python_version()}"
    )


def ensure_folders() -> None:
    """
    Create common project folders if missing (idempotent).
    """
    for p in (DATA_DIR, RESULTS_DIR):
        p.mkdir(parents=True, exist_ok=True)


# ---------- STRING / LIST DRILLS (REQUIRED comprehensions where noted) ----------

def normalize_names(names: Iterable[str | None]) -> List[str]:
    """
    REQUIRED: list comprehension
    Strip, lowercase, and drop empty/None values from a sequence of names.
    """
    return [n.strip().lower() for n in names if n and n.strip()]


def title_case_words(words: Iterable[str]) -> List[str]:
    """
    REQUIRED: list comprehension
    Title-case each word in the iterable.
    """
    return [w.title() for w in words]


def reverse_each_word(text: str) -> str:
    """
    REQUIRED: list comprehension + join
    Reverse each word but keep original order in the sentence.
    """
    return " ".join([w[::-1] for w in text.split()])


# ---------- BRANCHING EXERCISES ----------

def classify_score(score: float) -> str:
    """
    Return a letter grade using branching.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def bucket_ages(ages: Iterable[int]) -> Dict[str, int]:
    """
    Loop + branching: count ages into buckets.
    """
    buckets = {"child": 0, "teen": 0, "adult": 0, "senior": 0}
    for a in ages:
        if a < 13:
            buckets["child"] += 1
        elif a < 20:
            buckets["teen"] += 1
        elif a < 65:
            buckets["adult"] += 1
        else:
            buckets["senior"] += 1
    return buckets


# ---------- NUMERIC LISTS / REQUIRED COMPREHENSIONS ----------

def square_evens(nums: Iterable[int]) -> List[int]:
    """
    REQUIRED: list comprehension with filter
    Return squares of even numbers only.
    """
    return [n * n for n in nums if n % 2 == 0]


def cubes_or_square(nums: Iterable[int]) -> List[int]:
    """
    REQUIRED: list comprehension with inline conditional expression
    Cube positives; square non-positives.
    """
    return [n ** 3 if n > 0 else n ** 2 for n in nums]


def word_lengths(words: Iterable[str]) -> Dict[str, int]:
    """
    REQUIRED: dict comprehension
    Map each word to its length.
    """
    return {w: len(w) for w in words}


def unique_initials(words: Iterable[str]) -> Set[str]:
    """
    REQUIRED: set comprehension
    Collect unique first letters (lowercased) from non-empty strings.
    """
    return {w[0].lower() for w in words if isinstance(w, str) and w}


def flatten(nested: Iterable[Iterable[int]]) -> List[int]:
    """
    REQUIRED: nested list comprehension
    Flatten a 2D list of ints into a 1D list.
    """
    return [x for row in nested for x in row]


# ---------- SMALL ALGORITHMS (repetition, basic logic) ----------

def factorial(n: int) -> int:
    """
    Iterative factorial using a loop (n! for n >= 0).
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def fibonacci(n: int) -> List[int]:
    """
    Return first n Fibonacci numbers using a loop.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def is_prime(x: int) -> bool:
    """
    Simple primality test for x >= 2.
    """
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0:
        return False
    k = 3
    while k * k <= x:
        if x % k == 0:
            return False
        k += 2
    return True


def filter_primes(nums: Iterable[int]) -> List[int]:
    """
    REQUIRED: list comprehension using a predicate function (is_prime).
    Return only primes from a list of integers.
    """
    return [n for n in nums if is_prime(n)]


def summarize(numbers: Iterable[float]) -> Tuple[int, float, float]:
    """
    Return (count, min, max) as a tuple; handle empty gracefully.
    """
    numbers = list(numbers)
    if not numbers:
        return (0, 0.0, 0.0)
    return (len(numbers), float(min(numbers)), float(max(numbers)))


# =====================================================
# 4) TODO — INSTRUCTOR-REQUIRED / CH3–CH4 SPECIFIC FUNCS
#     Add exact drill functions here if your rubric requires them.
#     Mark 'REQUIRED: list comprehension' in docstrings where needed.
# =====================================================
# Example placeholder you can adapt:
# def filter_and_title(names: Iterable[str]) -> List[str]:
#     """REQUIRED: list comp — keep alphabetic names and Title Case them."""
#     return [n.title() for n in names if n and n.replace(" ", "").isalpha()]


# =====================================================
# 5) MAIN DRIVER (calls your functions with good arguments)
# =====================================================
def main() -> None:
    # ---- Intro & environment ----
    print("=== Project Byline ===")
    print(byline())

    print("\n=== Ensure Project Folders ===")
    ensure_folders()
    print(f"Data dir:    {DATA_DIR} (exists={DATA_DIR.exists()})")
    print(f"Results dir: {RESULTS_DIR} (exists={RESULTS_DIR.exists()})")

    # ---- Strings / lists ----
    print("\n=== Normalize Names (REQUIRED list comp) ===")
    raw_names = ["  Alice ", "", "BOB", None, "  cHaRlie  "]
    print(normalize_names(raw_names))

    print("\n=== Title Case Words (REQUIRED list comp) ===")
    print(title_case_words(["alpha", "beTA", "GAMMA"]))

    print("\n=== Reverse Each Word (REQUIRED list comp + join) ===")
    print(reverse_each_word("data fun forever"))

    # ---- Branching ----
    print("\n=== Classify Scores (branching) ===")
    for s in (95, 84, 72, 68, 50):
        print(f"{s} -> {classify_score(s)}")

    print("\n=== Bucket Ages (loop + branching) ===")
    print(bucket_ages([3, 12, 15, 19, 24, 42, 67, 80]))

    # ---- Numeric / comprehensions ----
    print("\n=== Square Evens (REQUIRED list comp with filter) ===")
    print(square_evens([1, 2, 3, 4, 5, 6]))

    print("\n=== Cubes or Square (REQUIRED inline conditional) ===")
    print(cubes_or_square([-3, -1, 0, 1, 2, 3]))

    print("\n=== Word Lengths (REQUIRED dict comp) ===")
    print(word_lengths(["alpha", "beta", "gamma"]))

    print("\n=== Unique Initials (REQUIRED set comp) ===")
    print(unique_initials(["Alice", "bob", "ALAN", ""]))  # -> {'a', 'b'}

    print("\n=== Flatten 2D (REQUIRED nested comp) ===")
    print(flatten([[1, 2], [3, 4, 5], [6]]))

    # ---- Algorithms ----
    print("\n=== Factorial (loop) ===")
    print("6! =", factorial(6))

    print("\n=== Fibonacci (loop) ===")
    print(fibonacci(10))

    print("\n=== Prime Filter (REQUIRED list comp using predicate) ===")
    print(filter_primes(list(range(2, 40))))

    # ---- Multiple returns ----
    print("\n=== Summarize (tuple return) ===")
    print(summarize([10, 2, 30, 7]))

    # ---- TODO: Instructor-specific calls (uncomment when you add them) ----
    # print(filter_and_title(["sandra", "otubushin", "123", "a-b"]))


# =====================================================
# 6) CONDITIONAL EXECUTION GUARD
#    (Only run main() when this file is executed directly)
# =====================================================
if __name__ == "__main__":
    main()
