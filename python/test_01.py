"""Test example."""

def write_numbers(fout):
    fout.write("1\n")
    fout.write("2\n")
    fout.write("3\n")

### bad test
class DummyFile:

    def __init__(self):
        self.written = []

    def write(self, thing):
        self.written.append(thing)

    def test_write_numbers():
        fout.write("1\n2\n3\n")

### better test
class DummyFile:

    def __init__(self):
        self.written = []

    def write(self, thing):
        self.written.append(thing)

def test_write_numbers():
    fout = DummyFile()
    write_numbers(fout)
    assert_that("".join(fout.written), is_("1\n2\n3\n"))

### better add
def write_numbers(fout):
    fout.writelines(["1\n",
                     "2\n",
                     "3\n"])

### supply a file object
def test_write_numbers():
    fout = io.StringIO()
    write_numbers(fout)
    assert_that(fout.getvalue(), is_("1\n2\n3\n"))


