import pathlib
cur_path = pathlib.Path(".")
new_path = cur_path.joinpath("backup")
size = 0
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
        text_path.rename(new_path.joinpath(text_path.name))
print(size)
