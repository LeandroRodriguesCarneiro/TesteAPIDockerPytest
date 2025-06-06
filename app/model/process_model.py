from .base_model import Base

from sqlalchemy import Column, Integer, String

class ProcessModel(Base):
    __tablename__ = 'process'

    id =  Column(Integer, primary_key=True)
    name = Column(String,  unique=True)

    def __repr__(self):
        return f'<Process(nome={self.name})>'