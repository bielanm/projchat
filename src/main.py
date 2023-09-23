
from typing import List
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from models.message import Message
from repositories.messages import SqlMessagesRepository


app = FastAPI()


@app.get("/message")
def get_messages() -> List[Message]:
    return SqlMessagesRepository.get_all_messages()


@app.post("/message")
def save_message(message: Message):
    SqlMessagesRepository.save_message(message=message)
    return JSONResponse(content={"done": True}, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
