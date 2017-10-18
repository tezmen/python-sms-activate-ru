# -*- coding: utf-8 -*-
from .models import ServiceModel
from .helper import object_factory


class ServiceStorage:
	names = {
		'VkCom': 'vk_0', 'Odnoklassniki': 'ok_0', 'Whatsapp': 'wa_0', 'Viber': 'vi_0', 'Telegram': 'tg_0',
		'WeChat': 'wb_0', 'Google': 'go_0', 'YouTube': 'go_0', 'Gmail': 'go_0', 'Avito': 'av_0',
		'AvitoSmsForwarding': 'av_1', 'Facebook': 'fb_0', 'Twitter': 'tw_0', 'AnyOther': 'ot_0',
		'AnyOtherSmsForwarding': 'ot_1',
		'Uber': 'ub_0', 'Qiwi': 'qw_0', 'GettTaxi': 'gt_0', 'OlxUA': 'sn_0', 'Instagram': 'ig_0',
		'SeoSprint': 'ss_0', 'Youla': 'ym_0', 'YoulaSmsForwarding': 'ym_1', 'MailRu': 'ma_0', 'Microsoft': 'mm_0',
		'MeetMe': 'uk_0', 'LineMessenger': 'me_0', 'Yahoo': 'mb_0', 'DrugVokrug': 'we_0', 'Rambler': 'bd_0',
		'TencentQQ': 'kp_0', 'TaxiMaxim': 'dt_0', 'Yandex': 'ya_0', 'YandexSmsForwarding': 'ya_1', 'Skout': 'mt_0',
		'Nimses': 'oi_0', 'GetResponseRu': 'fd_0', 'DromRu': 'zz_0', 'KakaoTalk': 'kt_0', 'ProtonMail': 'pm_0'}


class SmsService:
	def __init__(self):
		for name, short_name in ServiceStorage.names.items():
			object = object_factory(
				name,
				base_class=ServiceModel,
				argnames=['__service_short_name', '__count_slot']
			)(__service_short_name=short_name, __count_slot=0)
			setattr(self, '_' + name, object)

	@property
	def VkCom(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._VkCom

	@property
	def Odnoklassniki(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Odnoklassniki

	@property
	def Whatsapp(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Whatsapp

	@property
	def Viber(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Viber

	@property
	def Telegram(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Telegram

	@property
	def WeChat(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._WeChat

	@property
	def Google(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Google

	@property
	def YouTube(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._YouTube

	@property
	def Gmail(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Gmail

	@property
	def Avito(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Avito

	@property
	def AvitoSmsForwarding(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._AvitoSmsForwarding

	@property
	def Facebook(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Facebook

	@property
	def Twitter(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Twitter

	@property
	def AnyOther(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._AnyOther

	@property
	def AnyOtherSmsForwarding(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._AnyOtherSmsForwarding

	@property
	def Uber(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Uber

	@property
	def Qiwi(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Qiwi

	@property
	def GettTaxi(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._GettTaxi

	@property
	def OlxUA(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._OlxUA

	@property
	def Instagram(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Instagram

	@property
	def SeoSprint(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._SeoSprint

	@property
	def Youla(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Youla

	@property
	def YoulaSmsForwarding(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._YoulaSmsForwarding

	@property
	def MailRu(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._MailRu

	@property
	def Microsoft(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Microsoft

	@property
	def MeetMe(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._MeetMe

	@property
	def LineMessenger(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._LineMessenger

	@property
	def Yahoo(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Yahoo

	@property
	def DrugVokrug(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._DrugVokrug

	@property
	def Rambler(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Rambler

	@property
	def TencentQQ(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._TencentQQ

	@property
	def TaxiMaxim(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._TaxiMaxim

	@property
	def Yandex(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Yandex

	@property
	def YandexSmsForwarding(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._YandexSmsForwarding

	@property
	def Skout(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Skout

	@property
	def Nimses(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._Nimses

	@property
	def GetResponseRu(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._GetResponseRu

	@property
	def DromRu(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._DromRu

	@property
	def KakaoTalk(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._KakaoTalk

	@property
	def ProtonMail(self):
		"""
		:rtype: smsactivateru.models.ServiceModel
		"""
		return self._ProtonMail
