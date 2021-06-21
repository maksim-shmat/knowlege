"""Size string in bytes."""

def ByteSize(string):
    return len(string.encode("utf8"))
ByteSize("Python")
print(ByteSize("Data"))
