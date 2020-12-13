while True:
    reply = input('Enter text:\n')
    if reply == 'stop': break
    try:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print(num ** 2)
    except:
        print('Bad!' * 8)

print('Bye!')
