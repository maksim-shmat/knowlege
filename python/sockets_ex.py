"""Listening to notifications with WegSockets."""


# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from notifier.consumers import NotificationConsumer


application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NotificationConsumer),
    ]),
})


# consumer.py

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gossip", self.channel_name)

    async def name_gossip(self, event):
        await self.send_json(event)

# signals.py

from .post.models import Post
from django.db.models.signals import pre_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(pre_save, sender=Post)
def notify_post_save(sender, **kwargs):
    if "instance" in kwargs:
        instance = kwargs["instance"]
        # check if it is a new post
        ...
        channels_layer = get_channels_layer()
        async_to_sync(channel_layer.group_send)("gossip",
                {"type": "name.gossip",
                 "event": "New Post",
                 "sender": instance.posted_by.get_full_name(),
                 "message": instance.message})

#
