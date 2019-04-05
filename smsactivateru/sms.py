# -*- coding: utf-8 -*-
import requests


class Sms:
	def __init__(self, api_key):
		self.key = api_key
		self.url = 'http://sms-activate.ru/stubs/handler_api.php'

	def request(self, action):
		try:
			params = {**{'api_key': self.key}, **action.data}
			response = requests.get(self.url, params)
			return response.text
		except (ConnectionError, TimeoutError):
			return 'NO_CONNECTION'
