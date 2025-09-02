"""
sandra_otubushin_project_setup.py
Author: Sandra Otubushin
Course: Data Analytics Fundamentals
Module 2 - Project Setup

This script is the main driver for my project setup.
It includes a byline() function plus a simple, well-organized scaffold.
"""

# =====================================================
# 1) Imports
# =====================================================
from datetime import datetime
import platform
import pathlib
import os
# (optional) import your Module 1 utils if/when needed:
# from utils_sandra_otubushin import some_helper  # noqa: F401


# =====================================================
# 2) Constants / Paths
# =====================================================
PROJECT_ROOT = pathlib.Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"


# =====================================================
# 3) Helper Functions
# =====================================================
def byline(
    author: str = "Sandra Otubushin",
    course: str = "Data Analytics Fundamentals",
    module: str = "Module 2 – Project Setup",
) -> str:
    """
    Return a single-line project byline with useful context.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    py_ver = platform.python_version()
    file_name = pathlib.Path(__file__).name
    return f"{author} | {course} | {module} | {file_name} | {now} | Python {py_ver}"


def say_hello() -> None:
    """Tiny example function."""
    print("Hello from your project setup script!")


def show_environment_info() -> None:
    """Display minimal environment info to verify things are wired up."""
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Current working dir: {os.getcwd()}")
    print(f"Python: {platform.python_version()}")


def ensure_folders() -> None:
    """Create common folders if they don't exist yet."""
    for p in (DATA_DIR, RESULTS_DIR):
        p.mkdir(parents=True, exist_ok=True)


# =====================================================
# 4) Main Execution
# =====================================================
if __name__ == "__main__":
    print("=== Project Byline ===")
    print(byline())

    print("\n=== Setup Checks ===")
    say_hello()
    show_environment_info()

    print("\n=== Creating Folders (if missing) ===")
    ensure_folders()
    print(f"Ensured folders: {DATA_DIR.name}, {RESULTS_DIR.name}")

    print("\n=== Done ===")
