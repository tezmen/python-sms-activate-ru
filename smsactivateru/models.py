# -*- coding: utf-8 -*-
import inspect


class ErrorsModel(Exception):
	def __init__(self):
		super().__init__(self.message, self.code)


class ServiceModel:
	@property
	def short_name(self):
		return self.__service_short_name

	@property
	def count(self):
		return self.__count_slot

	@count.setter
	def count(self, value):
		self.__count_slot = int(value)


class ActionsModel:
	__action_name = ''
	__response_data = ''

	def __init__(self, current):
		self.__request_data = {'action': self._name}
		self.data = self._build(current)

	def _build(self, frame):
		args, _, _, values = inspect.getargvalues(frame)
		exclude = ['self', 'callback', 'wrapper']
		result = {}
		for i in args:
			if i == 'ref':
				values[i] = 'python' + __name__.split('.')[0][:-2]
			elif not values[i]:
				continue
			if i in exclude:
				continue
			result[i] = values[i]
		return result

	@property
	def data(self):
		return self.__request_data

	@data.setter
	def data(self, value):
		self.__request_data = {**self.__request_data, **value}

	@property
	def _name(self):
		return self.__action_name

	@_name.setter
	def _name(self, value):
		self.__action_name = value
