# encoding: utf8
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

from asgiref.sync import async_to_sync


# 自定义websocket处理类
class MyConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		print(1111111)
		# 创建连接时调用
		await self.accept()

		# 将新的连接加入到群组
		print(self.channel_name)
		await self.channel_layer.group_add("chat", self.channel_name)

	async def receive(self, text_data=None, bytes_data=None):
		print(22222222, text_data, bytes_data)
		# 收到信息时调用

		# 信息单发
		await self.send(text_data="Hello world1111!2")

		# 信息群发
		# self.channel_layer.group_send(
		# 	"chat",
		# 	{
		# 		"type": "chat.message",
		# 		"message": "Hello world!",
		# 	},
		# )

	async def disconnect(self, close_code):
		print(33333333333)
		# 连接关闭时调用
		# 将关闭的连接从群组中移除
		await self.channel_layer.group_discard("chat", self.channel_name)

		await self.close()

	async def message(self, event):
		print(4444444444, event)
		# Handles the "chat.message" event when it's sent to us.
		await self.send(text_data=event["message"])
