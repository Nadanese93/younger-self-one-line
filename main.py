import os

ENTRY = "The permission slip you forged for the field trip is the bravest signature you'll ever write — keep signing your own name like you mean it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    expected = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(expected)
    # Round-trip verification: read back and compare bytes exactly.
    with open(path, "rb") as f:
        actual = f.read()
    if actual != expected:
        raise SystemExit(f"verification failed: entry.txt bytes differ from ENTRY ({len(actual)} bytes read, {len(expected)} expected)")


if __name__ == "__main__":
    main()
