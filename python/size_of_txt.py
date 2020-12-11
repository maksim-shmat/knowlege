import pathlib
cur_path = pathlib.Path(".")
size = 0
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
print(size)
