# -*- coding: utf-8 -*-


class SmsTypes:
	class Country:
		RU = '0'  # Россия (Russia)
		UA = '1'  # Украина (Ukraine)
		KZ = '2'  # Казахстан (Kazakhstan)
		CN = '3'  # Китай (China)
		PH = '4'  # Филиппины (Philippines)
		MM = '5'  # Мьянма (Myanmar)
		ID = '6'  # Индонезия (Indonesia)
		MY = '7'  # Малайзия (Malaysia)
		KE = '8'  # Кения (Kenya) – temp disable
		TZ = '9'  # Танзания (Tanzania) – temp disable
		VN = '10'  # Вьетнам (Vietnam)
		KG = '11'  # Кыргызстан (Kyrgyzstan)
		US_VIRT = '12'  # США ВИРТ (USA)
		IL = '13'  # Израиль (Israel)
		HK = '14'  # Гонконг (Hong Kong)
		PL = '15'  # Польша (Poland)
		UK = '16'  # Великобритания/Англия (United Kingdom)
		MG = '17'  # Мадагаскар (Madagascar)
		CG = '18'  # Конго (Congo)
		NG = '19'  # Нигерия (Nigeria)
		MO = '20'  # Макао (Macau)
		EG = '21'  # Египет (Egypt)
		IE = '23'  # Ирландия (Ireland)
		KH = '24'  # Камбоджа (Cambodia)
		LA = '25'  # Лаос (Lao)
		HT = '26'  # Гаити (Haiti)
		CI = '27'  # Кот д'Ивуар (République de Côte d'Ivoire)
		GM = '28'  # Гамбия (Gambia)
		RS = '29'  # Сербия (Serbian)
		YE = '30'  # Йемен (Yemen)
		ZA = '31'  # ЮАР (South Africa)
		RO = '32'  # Румыния (Romania)
		EE = '34'  # Эстония (Estonia)
		AZ = '35'  # Азербайджан (Azerbaijan)
		CA = '36'  # Канада (Canada)
		MA = '37'  # Марокко (Morocco)
		GH = '38'  # Гана (Ghana)
		AR = '39'  # Аргентина (Argentina)
		UZ = '40'  # Узбекистан (Uzbekistan)
		CM = '41'  # Камерун (Cameroon)
		TG = '42'  # Чад (Chad)
		DE = '43'  # Германия (Germany)
		LT = '44'  # Литва (Lithuania)
		HR = '45'  # Хорватия ( Croatia)
		IQ = '47'  # Ирак (Iraq)
		NL = '48'  # Нидерланды (Netherlands)
		TH = '52'  # Таиланд (Thailand)
		SA = '53'  # Саудовская Аравия (Saudi Arabia)
		MX = '54'  # Мексика (Mexico)
		TW = '55'  # Тайвань (Taiwan)
		ES = '56'  # Испания (Spain)
		IR = '57'  # Иран (Iran)
		DZ = '58'  # Алжир (Algeria)
		SI = '59'  # Словения (Slovenia)
		BD = '60'  # Бангладеш (Bangladesh)
		SN = '61'  # Сенегал (Senegal)
		TR = '62'  # Турция (Turkey)
		CZ = '63'  # Чехия (Czechia)
		LK = '64'  # Шри-Ланка (Sri Lanka)
		PE = '65'  # Перу (Peru)
		PK = '66'  # Пакистан (Pakistan)
		NZ = '67'  # Новая Зеландия (New Zealand)
		GN = '68'  # Гвинея (Guinea)
		ML = '69'  # Мали (Mali)
		VE = '70'  # Венесуэла (Venezuela)
		ET = '71'  # Эфиопия (Ethiopia)
		BR = '73'
		US = '187' # США


	class Status:
		Cancel = '-1'
		SmsSent = '1'
		OneMoreCode = '3'
		End = '6'
		AlreadyUsed = '8'

	class Operator:
		MTS = 'mts'
		Beeline = 'beeline'
		Megafon = 'megafon'
		TELE2 = 'tele2'
		any = 'any'
