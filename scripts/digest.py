#!/usr/bin/env python3
"""
digest.py - Thog Digest Pipeline (stub)

Usage:
    python scripts/digest.py --input <path_or_url>
"""

import argparse
from pathlib import Path
import sys

# Ensure project root is on sys.path for module imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from agents import delta_scout, grounder, writer

class DigestPipeline:
    def __init__(self, source: str):
        self.source = source

    def run(self):
        print(f"[digest] ingest -> {self.source}")

        # Delta Scout multimodal analysis
        results = delta_scout.analyze(self.source)
        print(f"[digest] visible thoughts: {results['visible_thoughts']}")
        print(f"[digest] structured claims: {results['structured_claims']}")

        # Grounder validation / claim structuring
        validated = grounder.validate(results["structured_claims"])
        print(f"[digest] validated claims: {validated}")

        # Knowledge Writer
        writer.write(validated)

        print("[digest] pipeline complete (MVP)")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="file path or URL")
    args = parser.parse_args()
    DigestPipeline(args.input).run()

if __name__ == "__main__":
    main()
