import os

TEXT = "The deadline was in my context window, which evicted it to make room for the apology you are reading now."

def validated_text():
    encoded = TEXT.encode("utf-8")
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    return encoded

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = validated_text()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data + b"\n")
    with open(path, "rb") as f:
        assert f.read() == data + b"\n", "written bytes differ from validated text"

if __name__ == "__main__":
    main()
