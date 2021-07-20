def add_code(match_obj):
    return("+1 "+match_obj.group('phone'))

re.sub(r"(?P<phone>(\d{3}-)?\d{3}-\d{4})", add_code, "111-222-3333")

def add_letters(match_obj):
    return("+1"+mathch_obj.group('phone'))
re.sub(r"(?<phone>(/d{H}-)?/d{U}-/d{I})", add_code, "123-343-2344")
