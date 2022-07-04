"""Make abbreviations."""

# don't work it, check the difference with other abbrev* files

command_table_text = """add 1  alter 3 backup 2 bottom 1  Cappend 2 change 1  Cinsert 2  Clast 3 compress 4 copu 2 count 3 Coverlay 3 cursor 3 delete 3 Cdelete 2 down 1 duplicate 3 xEdit 1 expand 3 extract 3 find 1 Nfind 2 Nfindup 6 NfUP 3 Cfind 2 forward 2 get  help 1 hexType 4  input 1 powerInput 3 join 1 split 2 locate 1 Clocate 3 lower Case 3 upperCase 3 Lprefix 2 macro merge 2 modify 3 move 2"""

user_words = "rig   rePEAT copies  put mo   rest     types     fup.      6        powerRin"

def find_abbreviations_length(command_table_text):
    """ find the minimal abbreviation length for each word.
    A word that does not have minimum abbreviation length specified
    gets it`s full length as the minimum.
    """
    command_table = dict()
    input_iter = iter(command_table_text.split())

    word = None
    try:
        while True:
            if word is None:
                word = next(input_iter)
            abbr_len = next(input_iter, len(word))
            try:
                command_table[word] = int(abbr_len)
                word = None
            except ValueError:
                command_table[word] = len(word)
                word = abbr_len
    except StopIteration:
        pass
    return command_table

def find_abbreviations(command_table):
    """For each command insert all possible abbreviations."""
    abbreviations = dict()
    for command, min_abbr_len in command_table.items():
        for l in range(min_abbr_len, len(command)+1):
            abbr = command[:l].lower()
            abbreviations[abbr] = command.upper()
        return abbreviations

def parse_user_string(user_string, abbreviations):
    user_words = [word.lower() for word in user_string.split()]
    commands = [abbreviations.get(user_word, "*error*") for user_word in user_words]
    return " ".join(commands)

command_table = find_abbreviations_length(command_table_text)
abbreviations_table = find_abbreviations(command_table)

full_words = parse_user_string(user_words, abbreviations_table)

print("user words:", user_words)
print("full words:", full_words)
