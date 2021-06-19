# pylib
import unittest

# local
from TTBot.optional.evaluators.EvaluatorOoga import EvaluatorOoga

class TestEvaluatorOoga(unittest.IsolatedAsyncioTestCase):
	async def test_getMessageRegex(self):
		regex = EvaluatorOoga.getMessageRegex()
		self.assertRegex('ooga', regex)
		self.assertRegex('hey ooga booga', regex)
		self.assertNotRegex('ogoa', regex)
	# async def test_getMessageRegex(self)

	async def test_execute(self):
		pEvaluatorOoga = EvaluatorOoga()
		result = await pEvaluatorOoga.execute()
		self.assertEqual(result, 'booga')
	# async def test_execute(self)
# class TestEvaluatorOoga(unittest.IsolatedAsyncioTestCase)