"""Edit PDF's on the Linux command line."""

$ sudo apt install qpdf poppler-utils

# qpdf

qpdf --split-pages original.pdf  # make a file

qpdf --empty concatenated.pdf --pages split-*.pdf --  # concatenate files

# --empty    # start with an empty file
# --         # at the end, no more files to process

######
poppler-utils
# for make a ppm(portable mixmap)
