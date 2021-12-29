"""Models for Django file pars_xml_view.py"""

class Message(models.Model):
    message_class = models.CharField(max_length=6)
    message_version = models.CharField(max_length=2)
    message_number = models.CharField(max_length=4)
    sender_name = models.CharField(max_length=255, null=True, verbose_name='Sender name')
    sender_code = models.CharField(max_length=20, null=True, , verbose_name='Sender code')
    area = models.ForeignKey('Area', on_delete=models.CASCADE, verbose_name='Area')
    day = models.CharField(max_length=20)


    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

        def __str__(self):
            return f'{self.area}'


class Period(models.Model):
    start = models.CharField(max_length=4, verbose_name='Start measuring')
    end = models.CharField(max_length=4, verbose_name='End measuring')
    value = models.IntegerField(verbose_name='Indication')

    def __str__(self):
        return f'{self.start} - {self.end}'


class Meta:
    verbos_name = 'Period'
    verbose_name_plural = 'Periods'
    ordering = ('start',)


class ChannelsPeriod(models.Model):
    channel = models.ForeignKey('Channels', on_delete=models.CASCADE)
    period = models.ForeignKey('Period', on_delete=models.CASCADE)


class Channels(models.Model):
    code = models.CharField(max_length=3, db_index=True, verbose_name='Channel code')
    desc = models.CharField(max_length=50, verbose_name='Description')
    period = models.ManyToManyField('Period', through=ChannelsPeriod)

    def __str__(self):
        return f'{self.desc}'


    class Meta:
        verbose_name = 'Measuring channel'
        verbose_name_plural = 'Measuring channels'
        ordering = ('code',)


class Points(models.Model):
    code = models.CharField(max_length=15, db_index=True, verbose_name='Point code')
    name = models.CharField(max_length=255, db_index=True, verbose_name='Pointname')
    channels = models.ManyToManyField(Channels)

    def __str__(self):
        return f'{self.name} - {self.code}'


    class Meta:
        verbose_name = 'Measuring point'
        verbose_name_plural = 'Measuring points'
        ordering = ('code',)


class Area(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Area name')
    inn = models.CharField(max_length=10, verbose_name='Area code')
    points = models.ManyToManyField(Points)

    def __str__(self):
        return f'{self.name} - {self.inn}'

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        ordering = ('name',)
