'''
Created by auto_sdk on 2017.03.03
'''
from top.api.base import RestApi
class AlibabaAliqinFcIotQryPersoninfoRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.iccid = None
		self.mid_pat_channel = None
		self.userid = None

	def getapiname(self):
		return 'alibaba.aliqin.fc.iot.qry.personinfo'
