# -*- coding: utf-8 -*-
import inspect
import sys


def all_classes_name(module: str):
	clsmembers = inspect.getmembers(sys.modules[module], inspect.isclass)
	result = []
	for class_tuple in clsmembers:
		result.append(class_tuple[0])
	return result


def object_factory(name, base_class, argnames):
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			if key not in argnames:
				raise TypeError('Argument {} not valid for {}'.format(key, self.__class__.__name__))
			setattr(self, key, value)
		base_class.__init__(self)

	newclass = type(name, (base_class,), {'__init__': __init__})
	return newclass


def singleton(class_):
	instances = {}

	def get_instance(*args, **kwargs):
		if class_ not in instances:
			instances[class_] = class_(*args, **kwargs)
		return instances[class_]

	return get_instance
