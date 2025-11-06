from pydantic import BaseModel

class QueueDto(BaseModel):
    broker:str
    name:str
    url:str|None = None
    fifoQueue:bool = False
    contentBasedDeduplication: bool = False
    defaultVisibilityTimeout:int = 30
    delay:int = 0
    receiveMessageWait:int = 0
