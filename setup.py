# -*- coding: utf-8 -*-
from setuptools import setup

"""
@author: tezmen
@contact: https://t.me/tezmen
@license Apache License, Version 2.0, see LICENSE file
Copyright (C) 2017
"""


def requirements():
	"""Build the requirements list for this project"""
	requirements_list = list()
	with open('requirements.txt') as pc_requirements:
		for install in pc_requirements:
			requirements_list.append(install.strip())
	return requirements_list

setup(
	name='smsactivateru',
	version='1.1',
	description='Wrapper for automatic reception of SMS-messages by sms-activate.ru',
	author='tezmen',
	license='Apache License, Version 2.0, see LICENSE file',
	keywords='sms, revice, sms-activate-ru, autoreg',
	author_email='tezmenpro@gmail.com',
	url='https://github.com/tezmen/python-sms-activate-ru',
	download_url='https://github.com/tezmen/python-sms-activate-ru/archive/master.zip',
	packages=['smsactivateru'],
	install_requires=requirements(),
	classifiers=[
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: OS Independent',
		'Environment :: Console',
		'Development Status :: 3 - Alpha',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: Implementation :: PyPy',
	]
)
