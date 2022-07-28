"""Align columns."""

# need test it, not correct worked

txt = """Given$a$txt$file$of$many$lin3s,$where$fields$witin$a$line$
are$delineated$by$a$single$'dollar'$character,$write$a$program
that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$
column$are$separated$by$at$least$one$space.
Further,$allow$for$each$word$in$a$column$to$be$either$left$
justified,$right$justified,$or$center$justified$witin$its$column."""

parts = [line.rstrip("$").split("$") for line in txt.splitlines()]

max_widths = {}
for line in parts:
    for i, word in enumerate(line):
        max_widths[i] = max(max_widths.get(i, 0), len(word))

for i, justify in enumerate([str.ljust, str.center, str.rjust]):
    print(["Left", "Center", "Right"][i], " column-aligned output:\n")
    for line in parts:
        for j, word in enumerate(line):
            print(justify(word, max_widths[j]), end=' ')
    print("- " * 52)
