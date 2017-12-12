'''
Created by auto_sdk on 2017.02.27
'''
from top.api.base import RestApi
class AlibabaAliqinFcFlowGradeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.phone_num = None

	def getapiname(self):
		return 'alibaba.aliqin.fc.flow.grade'
