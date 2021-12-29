"""For Django save data aftere parse, for example."""

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    parser_class = [MeasuringXmlParse, ]

    def create(self, request, *args, **kwargs):
        data = request.data['message']
        area = Area.objects.create(name=data['area']['name'].encode("cp1251").decode('utf-8'),
                                   inn=data['area']['inn'].encode("cp1251").decode('utf-8'))
        for point in data['area']['measuringpoint']:  # get one data point
            point_obj = Point.objects.create(name=point['@name'].encode("cp1251").decode('utf-8'), code=point['@code'].encode("cp1251").decode('utf-8'))  # make an object of point
            for channel in point['measuringchannel']:  # get a channel into point
                channel_obj = Channels.objects.create(
                        code=channel['@code'].encode("cp1251").decode('utf-8'),  # make one channel for point
                        desc=channel['@desc'].encode("cp1251").decode('utf-8')                )
                
                period_obj = Period.objects.bulk_create([Period(
                    start=period['@start'].encode("cp1251").decode('utf-8'),
                    end=period['@end'].encode("cp1251").decode('utf-8'), # make a list of periods for chanel
                    value=period['value']) for period in channel['period']])

                for i in period_obj:
                    ChannelsPeriod.objects.create(channel=channel_obj, period=i)
                    channel_obj.period.add(i)  # add a list of periods into channel
                point_obj.channels.add(channel_obj)
            area.point.add(point_obj)

        message = Message.objects.create(
                message_class=data['@class'].encode("cp1251").decode('utf-8'),
                message_version=data['@version'].encode("cp1251").decode('utf-8'),
                message_number=data['@number'].encode("cp1251").decode('utf-8'),
                datetime=datetime.strptime(str(data['datetime']['timestamp']), '%Y%m%d%H%M%S'),
                day=datetime.strptime(str(data['datetime']['day']), '%Y%m%d'),
                sender_name=data['sender']['name'].encode("cp1251").decode('utf-8'),
                sender_code=data['sender']['inn'].encode("cp1251").decode('utf-8'),
                area=area)

        serilzer = MessageSerializer(message)
        return Response(serializer.data)
