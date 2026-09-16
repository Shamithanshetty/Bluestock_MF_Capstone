
"""
Master pipeline for the Bluestock Mutual Fund Analytics project.

This script runs the main Python scripts used in the project.
"""

import subprocess
import sys


def run_script(script_name):
    """
    Run a Python script from the scripts directory.

    Parameters
    ----------
    script_name : str
        Name of the Python script to execute.
    """
    print(f"\nRunning {script_name}...")
    subprocess.run(
        [sys.executable, f"scripts/{script_name}"],
        check=True
    )


def main():
    """
    Execute the project pipeline.
    """
    run_script("data_ingestion.py")
    run_script("live_nav_fetch.py")
    run_script("fetch_5_nav.py")
    run_script("recommender.py")


if __name__ == "__main__":
    main()

