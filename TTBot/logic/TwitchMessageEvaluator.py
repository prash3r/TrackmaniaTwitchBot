# vendor
import minidi
import twitchio

# local
from .Environment import Environment

class TwitchMessageEvaluator(minidi.Injectable):
	pEnvironment: Environment

	def getAuthor(self, pMessage: twitchio.Message) -> twitchio.Chatter:
		return pMessage.author
	
	def getAuthorName(self, pMessage: twitchio.Message) -> str:
		return pMessage.author.name

	def getChannel(self, pMessage: twitchio.Message) -> twitchio.Channel:
		return pMessage.channel

	def getChannelName(self, pMessage: twitchio.Message) -> str:
		return pMessage.channel.name
	
	def getContent(self, pMessage: twitchio.Message) -> str:
		return pMessage.content

	def getUserLevel(self, pMessage: twitchio.Message) -> int:
		pAuthor = self.getAuthor(pMessage)
		authorName = self.getAuthorName(pMessage)

		try:
			if authorName.lower() == 'prash3r' or self.isOwnerMessage(pMessage):
				return 100
			elif pAuthor.is_mod():
				return 10
			elif pAuthor.is_subscriber():
				return 5
			else:
				return 1
		except:
			return 1
	# def getUserLevel(self, pMessage: twitchio.Message) -> int

	def isBotAuthor(self, pMessage: twitchio.Message) -> bool:
		authorName = self.getAuthorName(pMessage)
		return self.pEnvironment.getTwitchBotUsername() == authorName.lower()
	# def isBotChannel(self, pMessage: twitchio.Message) -> bool

	def isBotChannel(self, pMessage: twitchio.Message) -> bool:
		channelName = self.getChannelName(pMessage)
		return self.pEnvironment.getTwitchBotUsername() == channelName.lower()
	# def isBotChannel(self, pMessage: twitchio.Message) -> bool

	def isOwnerMessage(self, pMessage: twitchio.Message) -> bool:
		authorName = self.getAuthorName(pMessage)
		channelName = self.getChannelName(pMessage)
		return authorName.lower() == channelName.lower()
	# def isOwnerMessage(self, pMessage: twitchio.Message) -> bool
# class TwitchMessageEvaluator(minidi.Injectable)