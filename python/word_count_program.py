""" Читает файл и возвращает количество строк, слов и символов - по 
    аналогии с утилитой UNIX uc.  """

import sys
def main():
    # Initialisation counters
    line_count = 0
    word_count = 0
    char_count = 0

    option = None
    params = sys.argv[1:]
    if len(params) > 1:
        # If parameters both go to first
        option = params.pop(0).lower().strip()
    filename = params[0]   # Open file
    with open("jill.txt") as infile:
        for line in infile:
            line_count += 1
            char_count += len(line)
            words = line.split()
            word_count += len(words)

    if option == "-c":
        print("File has {} characters".format(char_count))
    elif option == "-w":
        print("File has {} words".format(word_count))
    elif option == "-l":
        print("File has {} lines".format(line_count))
    else:
        # Print answers with format() method
        print("File has {0} lines, {1} words, {2} characters".format\
                (line_count, word_count, char_count))
    if __name__ == '__main__':
        main()
# It is module? And it with main() do not print in shell
