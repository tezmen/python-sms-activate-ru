import time
from smsactivateru import Sms, SmsTypes, SmsService, GetBalance, GetFreeSlots, GetNumber, SetStatus, GetStatus

"""
create wrapper with secret api-key
search here: http://sms-activate.ru/index.php?act=profile
             https://5sim.net/settings/security
"""
wrapper = Sms('API KEY', 'http://sms-activate.api.5sim.net/stubs/handler_api.php')

# getting balance
balance = GetBalance().request(wrapper)
# show balance
print('На счету {} руб.'.format(balance))

# getting free slots (count available phone numbers for each services)
available_phones = GetFreeSlots(
	country=SmsTypes.Country.RU
).request(wrapper)
# show for vk.com, whatsapp and youla.io)
print('vk.com: {} номеров'.format(available_phones.VkCom.count))
print('whatsapp: {} номеров'.format(available_phones.Whatsapp.count))
print('youla.io: {} номеров'.format(available_phones.Youla.count))

# try get phone for youla.io
activation = GetNumber(
	service=SmsService().Youla,
	country=SmsTypes.Country.RU,
	operator=SmsTypes.Operator.Beeline
).request(wrapper)
# show activation id and phone for reception sms
print('id: {} phone: {}'.format(str(activation.id), str(activation.phone_number)))

# getting and show current activation status
response = GetStatus(id=activation.id).request(wrapper)
print(response)

# .. send phone number to you service
user_action = input('Press enter if you sms was sent or type "cancel": ')
if user_action == 'cancel':
	set_as_cancel = SetStatus(
		id=activation.id,
		status=SmsTypes.Status.Cancel
	).request(wrapper)
	print(set_as_cancel)
	exit(1)

# set current activation status as SmsSent (code was sent to phone)
set_as_sent = SetStatus(
	id=activation.id,
	status=SmsTypes.Status.SmsSent
).request(wrapper)
print(set_as_sent)

# .. wait code
while True:
	time.sleep(1)
	response = GetStatus(id=activation.id).request(wrapper)
	if response['code']:
		print('Your code:{}'.format(response['code']))
		break

# set current activation status as End (you got code and it was right)
set_as_end = SetStatus(
	id=activation.id,
	status=SmsTypes.Status.End
).request(wrapper)
print(set_as_end)
