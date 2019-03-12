# -*- coding: utf-8 -*-

from .vhtemplate import *
from .vhflex.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
import requests, json, urllib.parse

class VHTemplate:
	'''
	CREATOR: FCKVEZA 
	LINE: veza1001
	'''
	def allowLiff(token, lineApp):
		url  = 'https://access.line.me/dialog/api/permissions'
		data = {
			'on': [
				'P',
				'CM'
			],
			'off': []
		}
		headers = {
			'X-Line-Access': token,
			'X-Line-Application': lineApp,
			'X-Line-ChannelId': '1603968955',
			'Content-Type': 'application/json'
		}
		requests.post(url, json=data, headers=headers)
	def postTemplate(to, data, token, lineApp):
		template.allowLiff(token, lineApp)
		client  = LINE(token, appName=lineApp)
		VE     = LiffChatContext(to)
		ZA     = LiffContext(chat=VE)
		VH     = LiffViewRequest("1636169025-bgap47xO", ZA)
		FCK     = client.liff.issueLiffView(VH)
		token   = 'Bearer {}'.format(FCK.accessToken)
		url     = 'https://api.line.me/message/v3/share'
		headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0.2; Lenovo A6000 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 Line/8.16.2','Content-Type': 'application/json','Authorization': token}
		data    = {"messages":[data]}
		laso    = requests.post(url, json=data, headers=headers)
		return laso