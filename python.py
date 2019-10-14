#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a test module'

'''
multi-line
comment
'''

__author__ = 'Hu'
__version__ = '1.0'
class Dict(dict):
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' has no attribute '%s'!" % key)
	def __setattr__(self,key,value):
		self[key] = value
if __name__ == '__main__':
	test()
