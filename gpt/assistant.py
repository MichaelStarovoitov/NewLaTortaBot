import time
import openai
from openai.types.beta.threads.run import Run

from common.textWork import escape_markdown_v2, get_simple_markdown
from data.config import OPENAI_API_KEY, AssistantID, MODEL, pattern


class parentAssistant:
    def __init__(self,name, personality, prodList):
        self.name = name
        self.personality = personality
        self.prodList = prodList
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
        self._createAssistant(AssistantID, MODEL)
    
    def _createAssistant(self, assistantId, model):
        if len(assistantId) > 0:
            self.assistant = self.client.beta.assistants.retrieve(assistantId)  
        else:
            self.assistant = self.client.beta.assistants.create( name=self.name, model=model )
    def _retrieve_run(self,idThread, run: Run):
        return self.client.beta.threads.runs.retrieve( run_id=run.id, thread_id=idThread)
    def _cancel_run(self,idThread, run: Run):
        self.client.beta.threads.runs.cancel(run_id=run.id, thread_id=idThread)
    def _create_run(self, idThread):
        return self.client.beta.threads.runs.create(
            thread_id=idThread, assistant_id=self.assistant.id, tools=[],
            instructions=f"""
                Your name is: {self.name}
                Your personality is: {self.personality}
                Metadata related to this conversation:
                {{
                    "dataProducts":{self.prodList.getSortProduct()},
                    "dataContacts":{self.prodList.getContacts()},
                    "dataDelivAndPayment":{self.prodList.getDelivAndPay()},
                    "isMore":{self.prodList.getIsMore()}
                }}
            """,
        )
    def _poll_run(self,idThread, run: Run):
        status = run.status
        start_time = time.time()
        while status != "completed":
            if status == 'failed':
                raise Exception(f"Run failed with error: {run.last_error}")
            if (status == 'expired') or (status == 'requires_action'):
                raise Exception("Run expired.")
            time.sleep(2)
            run = self._retrieve_run(idThread, run)
            status = run.status
            elapsed_time = time.time() - start_time
            if elapsed_time > 120:  # 2 minutes
                self._cancel_run(idThread, run)
                raise Exception("Run took longer than 2 minutes.")


class gptAssistant(parentAssistant):
    def __init__(self,name, personality, prodList):
        super().__init__(name, personality, prodList)
    
    def create_thread(self):
        return self.client.beta.threads.create().id

    def sendMessage(self, idThread, message):
        self.prodList.search_json_with_similarityNew(message)
        self.client.beta.threads.messages.create( thread_id=idThread, role="user", content=message )
        self._poll_run(idThread, self._create_run(idThread))
        resultMessage = self.client.beta.threads.messages.list( thread_id=idThread ).data[0].content[0].text.value
        # resultMessage = escape_markdown_v2(resultMessage)
        # resultMessage = get_simple_markdown(pattern, resultMessage)
        return resultMessage



