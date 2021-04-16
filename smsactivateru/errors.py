# -*- coding: utf-8 -*-
from .helper import object_factory
from .models import ErrorsModel


class ErrorStorage:
	codes = {
		'NO_NUMBERS':    {
			'text':  'Нет свободных номеров для приёма смс от текущего сервиса',
			'class': 'NoFreeNumber'
		},
		'NO_BALANCE':    {
			'text':  'Закончился баланс',
			'class': 'NoBalance'
		},
		'BAD_ACTION':    {
			'text':  'Некорректное действие (параметр action)',
			'class': 'InvalidAction'
		},
		'BAD_SERVICE':   {
			'text':  'Некорректное наименование сервиса (параметр service)',
			'class': 'InvalidService'
		},
		'BAD_KEY':       {
			'text':  'Неверный API ключ доступа',
			'class': 'InvalidApiKey'
		},
		'ERROR_SQL':     {
			'text':  'Один из параметров имеет недопустимое значение',
			'class': 'InvalidData'
		},
		'NO_ACTIVATION': {
			'text':  'Указанного id активации не существует',
			'class': 'InvalidId'
		},
		'BAD_STATUS':    {
			'text':  'Попытка установить несуществующий статус',
			'class': 'InvalidStatus'
		},
		'STATUS_CANCEL': {
			'text':  'Текущая активация отменена и больше не доступна',
			'class': 'CanceledActivation'
		},
		'BANNED':        {
			'text':  'Аккаунт заблокирован',
			'class': 'BannedUser'
		},
		'NO_CONNECTION': {
			'text':  'Нет соединения с серверами sms-activate',
			'class': 'ConnectionError'
		}
	}


def error_handler(function: classmethod):
	def wrapper(self, response, *args, **kwargs):
		for key in ErrorStorage.codes.keys():
			if key in response:
				except_class = object_factory(
					ErrorStorage.codes[key]['class'],
					base_class=ErrorsModel,
					argnames=['message', 'code'])
				raise except_class(message=ErrorStorage.codes[key]['text'], code=key)
		return function(self, response, *args, **kwargs)
	return wrapper
