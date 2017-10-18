# -*- coding: utf-8 -*-


class SmsTypes:
	class Country:
		RU = '0'
		UA = '1'
		KZ = '2'
		BZ = '3'

	class Status:
		Cancel = '-1'
		SmsSent = '1'
		OneMoreCode = '3'
		End = '6'
		AlreadyUsed = '8'

	class Operator:
		MTS = 'mts'
		Beeline = 'beeline'