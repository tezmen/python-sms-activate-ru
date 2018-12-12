# -*- coding: utf-8 -*-
import time

import smsactivateru


class SmsActivation:
	"""
	This is simple worker!
	For hand-settings any other params – check /example/custom.py
	"""

	def __init__(self, activation_id, number, wrapper):
		self.__id = activation_id
		self.__number = number
		self.__wrapper = wrapper
		self.__last_code = str()

	def cancel(self):
		set_status = smsactivateru.SetStatus(
			id=self.__id,
			status=smsactivateru.SmsTypes.Status.Cancel
		)
		if self.wrapper:
			return set_status.request(self.wrapper)
		return set_status

	def mark_as_used(self):
		set_status = smsactivateru.SetStatus(
			id=self.__id,
			status=smsactivateru.SmsTypes.Status.AlreadyUsed
		)
		if self.wrapper:
			return set_status.request(self.wrapper)
		return set_status

	def was_sent(self):
		set_status = smsactivateru.SetStatus(
			id=self.__id,
			status=smsactivateru.SmsTypes.Status.SmsSent
		)
		if self.wrapper:
			return set_status.request(self.wrapper)
		return set_status

	def wait_code(self, timeout=1200, callback=None, not_end=False, *args, **kwargs):
		"""
		:param wrapper: obj for work with sms-activate
		:param timeout: timeout waiting of code from sms in secs. 1200 - 20 min, this is max time of a live session.
		:param callback: function for eval before getting code
		:param not_end:
		:return: str
		"""
		counter = 0
		while True:
			time.sleep(1)
			counter += 1
			if counter >= timeout:
				raise ('Timeout error')
			response = smsactivateru.GetStatus(id=self.id).request(self.wrapper)
			if response['code'] and not not_end and response['code'] != self.last_code:
				self.__last_code = response['code']
				smsactivateru.SetStatus(
					id=self.id,
					status=smsactivateru.SmsTypes.Status.End
				).request(self.wrapper)
				break
			elif response['code'] and not_end and response['code'] != self.last_code:
				self.__last_code = response['code']
				smsactivateru.SetStatus(
					id=self.id,
					status=smsactivateru.SmsTypes.Status.OneMoreCode
				)
				break
		if callback:
			callback(self.last_code)
		else:
			return self.last_code

	@property
	def id(self):
		return self.__id

	@property
	def phone_number(self):
		return self.__number

	@property
	def wrapper(self):
		return self.__wrapper

	@property
	def last_code(self):
		return self.__last_code
