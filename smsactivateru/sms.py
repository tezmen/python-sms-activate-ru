# -*- coding: utf-8 -*-
import requests


class Sms:
	def __init__(self, api_key, api_url='http://sms-activate.ru/stubs/handler_api.php'):
		self.key = api_key
		self.url = api_url

	def request(self, action):
		try:
			params = {**{'api_key': self.key}, **action.data}
			response = requests.get(self.url, params)
			return response.text
		except (ConnectionError, TimeoutError):
			return 'NO_CONNECTION'
