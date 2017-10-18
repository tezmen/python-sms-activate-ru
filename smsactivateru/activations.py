# -*- coding: utf-8 -*-
import time
import smsactivateru


class SmsActivation:
	def __init__(self, activation_id, number):
		self.__id = activation_id
		self.__number = number

	def cancel(self):
		return smsactivateru.SetStatus(
			id=self.__id,
			status=smsactivateru.SmsTypes.Status.Cancel
		)

	def was_sent(self):
		return smsactivateru.SetStatus(
			id=self.__id,
			status=smsactivateru.SmsTypes.Status.SmsSent
		)

	def wait_code(self, wrapper, callback=None):
		code = ''
		while True:
			time.sleep(1)
			response = smsactivateru.GetStatus(id=self.__id).request(wrapper)
			if response['code']:
				code = response['code']
				smsactivateru.SetStatus(
					id=self.__id,
					status=smsactivateru.SmsTypes.Status.End
				).request(wrapper)
				break
		if callback:
			callback(code)
		else:
			return code

	@property
	def id(self):
		return self.__id

	@property
	def phone_number(self):
		return self.__number
