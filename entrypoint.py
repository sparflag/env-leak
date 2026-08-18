#!/usr/bin/env python3
"""Env Leak — real mini-challenge (env-leak)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'proc-environ')


def main():
    mat = fetch_material()
    key = CHALLENGE_KEY or "env-key"
    with open("/challenge/flag.enc", "w") as fh:
        fh.write(mat.get("delivery_blob", ""))
    environ = (
        "PATH=/usr/local/bin:/usr/bin\n"
        "HOME=/challenge\n"
        "USER=pico\n"
        f"CHALLENGE_KEY={key}\n"
        "LD_PRELOAD=\n"
        "PYTHONPATH=/challenge/_shared\n"
    )
    with open("/challenge/proc_environ.txt", "w") as fh:
        fh.write(environ)
    print("Env Leak — CHALLENGE_KEY exported in proc_environ.txt.")


if __name__ == "__main__":
    main()
