# pylib
from abc import abstractmethod, abstractstaticmethod

# local
from ..Module import Module

class Evaluator(Module):
	@staticmethod
	@abstractstaticmethod
	def getMessageRegex() -> str:
		pass
# class Evaluator(ABC)