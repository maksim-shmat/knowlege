"""Align columns from file align_colums.dat."""

for align in '<^>':
    rows = [line.strip().split('$') for line in open('align_column.dat')]
    fmts = ['{:%s%d}' % (align, max(len(row[i]) if i < len(row) else 0 for row in rows)) for i in range(max(map(len, rows)))]
    for row in rows:
        print(' '.join(fmts).format(*(row + [''] * len(fmts))))
    print('')
