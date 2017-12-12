# -*- coding: utf-8 -*-
import requests


class Sms:
	def __init__(self, api_key, api_url):
		self.key = api_key
		self.url = api_url

	def request(self, action):
		params = {**{'api_key': self.key}, **action.data}
		response = requests.get(self.url, params)
		return response.text
