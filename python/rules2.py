def internal(conjunct):
    return [clause.split() for clause in conjunct.split(',')]

def external(conjunct):
    return ', '.join(' '.join(clause) for clause in conjunct)
