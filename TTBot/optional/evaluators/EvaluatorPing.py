# local
from .Evaluator import Evaluator

class EvaluatorPing(Evaluator):
    def getMessageRegex(self) -> str:
        return r'\b(ping)\b'
    
    def getRightsId(self) -> str:
        return 'ping'
    
    async def execute(self, _) -> str:
        return 'pong'
# class EvaluatorPing(Evaluator)