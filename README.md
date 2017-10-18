# python-sms-activate-ru
Wrapper for automatic reception of SMS-messages by sms-activate.ru

[![N|Solid](https://img.shields.io/pypi/pyversions/smsactivateru.svg)](https://pypi.python.org/pypi/smsactivateru)

### Installation
You can install or upgrade package with:
```
$ pip install smsactivateru --upgrade
```
Or you can install from source with:
```
$ git clone https://github.com/tezmen/python-sms-activate-ru
$ cd python-sms-activate-ru
$ python setup.py install
```
### Example
```python
from smsactivateru import Sms, SmsService, GetNumber

wrapper = Sms('API KEY')

activation = GetNumber(
	service=SmsService().Youla,
).request(wrapper)

input('Press enter if you sms was sent')

activation.was_sent().request(wrapper)
code = activation.wait_code(wrapper=wrapper)
print(code)
```
More examples located in /example/