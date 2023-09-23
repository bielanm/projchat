from typing import List
from connections.pg import get_connection
from models.message import Message
from abc import abstractmethod, ABC


class MessagesRepository(ABC):

    @classmethod
    @abstractmethod
    def save_message(cls, message: Message):
        pass
    
    @classmethod
    @abstractmethod
    def get_all_messages(cls) -> List[Message]:
        pass


class InmemoryMessagesRepository(MessagesRepository):

    STORAGE = []
    CURRENT_ID = 0

    @classmethod
    def save_message(cls, message: Message):
        message.id = cls.CURRENT_ID
        cls.STORAGE.append(message)
        cls.CURRENT_ID += 1

    @classmethod
    def get_all_messages(cls) -> List[Message]:
        return cls.STORAGE


class SqlMessagesRepository:


    @classmethod
    def save_message(cls, message: Message):
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO message (text) VALUES (%s)", (message.text,))
        connection.commit()


    @classmethod
    def get_all_messages(cls) -> List[Message]:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM message")
            return [Message(id=id, text=text) for id, text in cursor.fetchall()]