import sys
import os

# Ensure the current directory is in Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from cli import main

if __name__ == "__main__":
    main()