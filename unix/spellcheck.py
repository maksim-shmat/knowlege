"""Spell checking on the terminal."""

$ aspelll check <filename>  # but it make backup file .bak
$ aspell -c <file>

# Without backup
#---------------
$ aspell check -dont-backup <filename>  # without backup
$ aspell -c <file> -x
