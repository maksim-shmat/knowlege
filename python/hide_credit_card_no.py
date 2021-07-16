"""Four last digits is view, and another is hide under asterisks."""

# retur string as long as origin input
# 1
def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]

def card_hide(card):
    return '*' * (len(card)-4) + card[-4:]
