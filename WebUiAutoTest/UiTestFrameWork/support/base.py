# -*- coding: utf-8 -*-
import importlib


class BaseItem(object):

	def _init_item(self, item_suffix):
		module = importlib.import_module('.item_locate', 'support')
		item_locate = getattr(module, item_suffix)
		for k, v in item_locate.items():
			self.__dict__[k] = v	