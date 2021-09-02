# pylib
import unittest
from unittest import mock

# local
from TTBot.data.Message import Message
from TTBot.data.MessageChannel import MessageChannel
from TTBot.logic.LocalVariables import LocalVariables
from TTBot.module.karma.EvaluatorKarmaPlusPlus import EvaluatorKarmaPlusPlus

class TestEvaluatorKarmaPlusPlus(unittest.IsolatedAsyncioTestCase):
	async def test_getMessageRegex(self):
		pEvaluatorKarmaPlusPlus = EvaluatorKarmaPlusPlus()
		regex = pEvaluatorKarmaPlusPlus.getMessageRegex()
		self.assertRegex("++", regex)
		self.assertRegex("++ it is", regex)
		self.assertRegex("That's a ++", regex)
		self.assertNotRegex("YEP ++ YEP", regex)
	# async def test_getMessageRegex(self)

	async def test_execute(self):
		pLocalVariables = LocalVariables()
		pLocalVariables.get = mock.Mock(return_value=68)
		pLocalVariables.write = mock.Mock()

		pEvaluatorKarmaPlusPlus = EvaluatorKarmaPlusPlus()
		pEvaluatorKarmaPlusPlus.pLocalVariables = pLocalVariables

		pChannel = MessageChannel(name='unittest')
		pMessage = Message(channel=pChannel, content='++')

		message = await pEvaluatorKarmaPlusPlus.execute(pMessage)
		self.assertEqual(message, "Successfully voted ++, current streamer karma: 69")

		pLocalVariables.get.assert_called_once_with('karma', 'unittest', 0)
		pLocalVariables.write.assert_called_once_with('karma', 'unittest', 69)
	# async def test_execute(self)
# class TestEvaluatorKarmaPlusPlus(unittest.IsolatedAsyncioTestCase)