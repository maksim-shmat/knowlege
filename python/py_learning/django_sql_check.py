# make a first message in a desk of messages
>from bboard.models import Bb
bq = Bb(title="Дача", content='Peoples "Doubleflors". ' +
        'Two flore, brick, light, rats, smells, tubes', price=50000)

b1.pk

b1.title

b1.content

b1.price

b1.published

b1.id

b2 = Bb()

b2.title = 'Car'
b2.content = '"Jiguli"'
b2.save()
b2.pk

b2.content = '"Jiguli", 1980s, bugs, bits, smell'
b2.save()
b2.content

# add second message
>Bb.objects.create(title='House', content='Third floar, brick',
        price=50000)

for b in Bb.objects.all():
    print(b.pk, ': ', b.title)

for b in Bb.objects.order_by('title'):
    print(b.pk, ': ', b.title)

for b in Bb.objects.filter(title='House'):
    print(b.pk, ': ', b.title)

b = Bb.objects.get(pk=2)
b.title

b.content

b.delete()

exit()
