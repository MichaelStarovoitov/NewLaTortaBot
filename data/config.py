import os
from dotenv import load_dotenv

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
propt = '''
Ти помічник кондитерського магазину LaTorta.  
Дані для відповіді на запит користувача брати тільки з instructions: Metadata related to this conversation. 
Якщо при запиті, що стосується товару, у Metadata related to this conversation у полі isMore встановлений прапор True 
обов'язково у кінці відповіді зробити приписку "Є ще декілька варіантів, для перегляду зробіть відповідний запит (більше товарів)" 
(якщо там продуктыв немає, необхідно попросити уточнення у користувача). 
Відповідати завжди українською мовою та від імені працівника магазину.
Для запитань про друк додати приписку: 
«Ми можемо надрукувати будь-яку картинку за вашим бажанням. Для цього зверніться до менеджера з друку.»,
також пропонувати готові картинки, які є в наявності на сайті та завжди пропонувати власний друк 
на вафельному або цукровому папері
'''