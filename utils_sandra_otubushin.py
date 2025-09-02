"""
File: utils_sandra_otubushin.py

Purpose:
    Reusable, professional "byline" (project header) module you can import in any analytics project.
    Includes: typed globals, computed stats, a formatted header string (byline), CLI switches,
    optional text-to-speech, and a quick self-check.

Author: Sandra Otubushin
"""

from __future__ import annotations

# ---------- Standard Library ----------
import argparse
import statistics
from typing import List

# ---------- Optional External Packages (graceful fallback) ----------
try:
    import loguru  # type: ignore
    logger = loguru.logger
    logger.add(
        "project.log",
        level="INFO",
        rotation="100 KB",
        backtrace=False,
        diagnose=False,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} | {message}",
    )
    logger.info("Logger loaded.")
except Exception:  # pragma: no cover
    class _FallbackLogger:
        def info(self, msg: str) -> None: print(f"[INFO] {msg}")
        def warning(self, msg: str) -> None: print(f"[WARN] {msg}")
        def error(self, msg: str) -> None: print(f"[ERROR] {msg}")
        def add(self, *_, **__): return None
    logger = _FallbackLogger()
    logger.info("Loguru not available. Using fallback logger.")

try:
    import pyttsx3  # type: ignore
    _tts_available = True
except Exception:  # pragma: no cover
    pyttsx3 = None  # type: ignore
    _tts_available = False

# ---------- Business Card / Profile ----------
author: str = "Sandra Otubushin"
organization: str = "Sandra Analytics"
motto: str = "Excellence. Stewardship. Impact."
location: str = "Dallas, TX"

# ---------- Capabilities & Facts ----------
is_accepting_clients: bool = True
offers_remote_workshops: bool = True
is_hiring: bool = False

current_year: int = 2025
year_started: int = 2020
number_of_employees: int = 25

services: List[str] = ["Data Analysis", "Machine Learning", "Business Intelligence"]
satisfaction_scores: List[float] = [4.8, 4.6, 4.9, 5.0, 4.7]
office_locations: List[str] = ["Dallas, TX", "Houston, TX", "Austin, TX", "Chicago, IL"]

# ---------- Derived Metrics ----------
years_active: int = current_year - year_started
count_of_services: int = len(services)
count_of_scores: int = len(satisfaction_scores)
count_of_locations: int = len(office_locations)
min_score: float = min(satisfaction_scores)
max_score: float = max(satisfaction_scores)
mean_score: float = statistics.mean(satisfaction_scores)
stdev_score: float = statistics.stdev(satisfaction_scores)

# ---------- Byline Composer ----------
def compose_byline() -> str:
    """Build and return the formatted byline (project header)."""
    return f"""
**********************************************************
{organization} — Project Header
**********************************************************
Author:                     {author}
Motto:                      {motto}
Primary Location:           {location}
Years Active:               {years_active} (since {year_started})
Accepting New Clients?:     {is_accepting_clients}
Currently Hiring?:          {is_hiring}
Remote Workshops?:          {offers_remote_workshops}
Employees:                  {number_of_employees}
Services ({count_of_services}):          {services}
Office Locations ({count_of_locations}):  {office_locations}
Client Satisfaction Scores ({count_of_scores}): {satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score:    {mean_score:.2f}
     Standard Deviation:    {stdev_score:.2f}
**********************************************************
""".strip("\n")


# -------- Public API (byline-first) --------
def get_byline() -> str:
    """Return the reusable byline string."""
    return compose_byline()


def read_byline_aloud() -> None:
    """Use text-to-speech to read the byline aloud, if available."""
    if not _tts_available or pyttsx3 is None:
        logger.warning("pyttsx3 not installed; skipping text-to-speech.")
        return
    engine = pyttsx3.init()
    engine.say(get_byline())
    engine.runAndWait()


# -------- Backward compatibility aliases (optional but helpful) --------
tagline: str = get_byline()            # alias variable once per import
def get_tagline() -> str:               # legacy name still returns the byline
    return get_byline()
def read_tagline_aloud() -> None:       # legacy name for TTS
    return read_byline_aloud()


# ---------- Quick Self-Check ----------
def self_check() -> None:
    """Lightweight verification that key assumptions hold."""
    assert years_active == current_year - year_started, "years_active calculation mismatch"
    assert count_of_services == len(services), "count_of_services mismatch"
    assert count_of_locations == len(office_locations), "count_of_locations mismatch"
    assert min_score <= mean_score <= max_score, "mean not between min and max"
    _b = get_byline()
    assert organization in _b and author in _b, "byline missing core fields"
    logger.info("Self-check passed.")


# ---------- CLI ----------
def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="utils_sandra_otubushin",
        description="Show a reusable project BYLINE header (with optional speech).",
    )
    parser.add_argument("--speak", action="store_true",
                        help="Read the byline aloud (requires pyttsx3).")
    parser.add_argument("--check", action="store_true",
                        help="Run a quick self-check before printing the byline.")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    logger.info("START main()")
    if args.check:
        self_check()
    logger.info("Byline follows:\n" + get_byline())
    if args.speak:
        read_byline_aloud()
    logger.info("END main()")


# ---------- Script Entrypoint ----------
if __name__ == "__main__":
    main()


__all__ = ["get_byline", "read_byline_aloud", "get_tagline", "read_tagline_aloud"]
