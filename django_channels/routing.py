# encoding: utf8
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from django_channels.consumer import MyConsumer

application = ProtocolTypeRouter({

	# WebSocket chat handler
	"websocket": AuthMiddlewareStack(
		URLRouter([
			path("chart/push", MyConsumer),
		])
	),
})
