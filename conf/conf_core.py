# coding=utf-8
import ConfigParser
import os

config_dir = os.path.dirname(os.path.abspath(__file__))
config_parser = ConfigParser.ConfigParser()

polyv_path = os.path.join(config_dir, 'polyv.conf')
config_parser.read(polyv_path)

# [polyv]
APPID = config_parser.get("polyv", "appid")  # 在直播系统登记的appId
USERID = config_parser.get("polyv", "userid")  # 用户ID
APPSECRET = config_parser.get("polyv", "appsecret")

# [live]
CREATE_LIVE = config_parser.get("live", "create")  # 创建直播频道
DELETE_LIVE = config_parser.get("live", "delete")  # 删除直播频道
PASSWD_SET_LIVE = config_parser.get("live", "passwd_set")  # 设置频道号密码
GET_LIVE_STATUS_LIVE = config_parser.get("live", "get_live_status")  # 批量获取频道直播状态接口
