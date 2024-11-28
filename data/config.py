import os
from dotenv import load_dotenv
from common.fileWork import read_text_file

load_dotenv()

parent_dir = os.path.dirname(os.path.abspath(__file__))
usersFile = os.path.join(parent_dir, 'dataBase', "users.json")
productsFile = os.path.join(parent_dir, 'dataBase', "ResultFile.json")
parserFolder = os.path.join(parent_dir, 'dataBase', "parcer")

TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AssistantID = 'asst_COt7IUWH96AQMZVBmw6eykuu'
MODEL = "gpt-4-turbo-preview"
pattern = r'【\d+:\d+†[^】]+】'


nameBot = 'Помічник у кондитерській'
proptPath = os.path.join(parent_dir, 'dataBase', "propt.txt")
resultQestionPath = os.path.join(parent_dir, 'dataBase', "resultQestion.txt")
propt = read_text_file(proptPath)