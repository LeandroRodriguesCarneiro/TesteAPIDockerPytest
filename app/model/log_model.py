from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func

from .base_model import Base

class LogModel(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    id_process = Column(Integer, ForeignKey('process.id'))
    status_code = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    message = Column(String)

    def __repr__(self):
        return (f"<Logs(id={self.id}, id_process={self.id_process}, "
            f"status_code={self.status_code}, timestamp={self.timestamp}, "
            f"message='{self.message}')>")