from smsactivateru import Sms, SmsTypes, SmsService, GetBalance, GetFreeSlots, GetNumber

"""
create wrapper with secret api-key
search here: http://sms-activate.ru/index.php?act=profile
             https://5sim.net/settings/security
"""
wrapper = Sms('API KEY', 'http://sms-activate.api.5sim.net/stubs/handler_api.php')

# ------------------------------ #

# getting balance
balance = GetBalance().request(wrapper)
# show balance
print('На счету {} руб.'.format(balance))

# ------------------------------ #

# getting free slots (count available phone numbers for each services)
available_phones = GetFreeSlots(
	country=SmsTypes.Country.RU,
	operator=SmsTypes.Operator.TELE2
).request(wrapper)
# show for vk.com, whatsapp and youla.io)
print('vk.com: {} номеров'.format(available_phones.VkCom.count))
print('whatsapp: {} номеров'.format(available_phones.Whatsapp.count))
print('youla.io: {} номеров'.format(available_phones.Youla.count))

# ------------------------------ #

# try get phone for youla.io
activation = GetNumber(
	service=SmsService().Youla,
	country=SmsTypes.Country.RU,
	operator=SmsTypes.Operator.Beeline
).request(wrapper)

# show activation id and phone for reception sms
print('id: {} phone: {}'.format(str(activation.id), str(activation.phone_number)))

# .. send phone number to you service
user_action = input('Press enter if you sms was sent or type "cancel": ')
if user_action == 'cancel':
	activation.cancel()
	exit(1)

# set current activation status as SmsSent (code was sent to phone)
activation.was_sent()


# callback method for eval (if callback not set, code will be return)
def fuck_yeah(code):
	print('Oh, it\'s my code! {}'.format(code))


# .. wait code
activation.wait_code(callback=fuck_yeah, wrapper=wrapper, not_end=True)

print('this string print befoer eval fuck_yeah function')

# .. and wait one mode code
# (!) if you not set not_end (or set False) – activation ended before return code
activation.wait_code(callback=fuck_yeah, wrapper=wrapper)
