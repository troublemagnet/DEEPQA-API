from django.apps import AppConfig
import sys
import os

temp = r'C:\Users\IIIT\Desktop\DeepQA-master\DeepQA-master' # make it the absolute path of your DeepQA

sys.path.insert(0, temp)
from chatbot import chatbot

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chatbotPath = "\\".join(BASE_DIR.split("\\")[:-1])
sys.path.append(chatbotPath)

class RetrieveAnswer(AppConfig):
    """ Manage a single instance of the chatbot shared over the website
    """
    name = 'API'
    bot = None

    def ready(self):
        # Initialize the chatbot daemon (should be launched only once)
        if not RetrieveAnswer.bot:
            RetrieveAnswer.initializeBot()

    @staticmethod
    def initializeBot():
        """ Instantiate the chatbot for later use
        Should be called only once
        """
        if not RetrieveAnswer.bot:
            RetrieveAnswer.bot = chatbot.Chatbot()
            RetrieveAnswer.bot.main(['--modelTag', 'server', '--test', 'daemon', '--rootDir', 'interactive', chatbotPath])
        else:
            return

    @staticmethod
    def callBot(sentence):
        """ Use the previously instantiated bot to predict a response to the given sentence
        Args:
            sentence (str): the question to answer
        Return:
            str: the answer
        """
        RetrieveAnswer.initializeBot()
        if RetrieveAnswer.bot:
            return RetrieveAnswer.bot.daemonPredict(sentence)
