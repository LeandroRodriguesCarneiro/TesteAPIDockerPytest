from sqlalchemy.orm import Session, joinedload

from .repository import Repository

from ..model import LogModel

class LogRepository(Repository):

    def __init__(self, session: Session):
        super().__init__(session)

    def add(self, log: LogModel):
        self.session.add(log)
        self.session.commit()
        self.session.refresh(log)
        return log

    def get_by_id(self, log_id: int):
        return self.session.query(LogModel).filter(LogModel.id == log_id).options(joinedload(LogModel.process)).first()

    def get_all(self):
        return self.session.query(LogModel).options(joinedload(LogModel.process)).all()

    def delete(self, log_id: int):
        log = self.get_by_id(log_id)
        if log:
            self.session.delete(log)
            self.session.commit()
        return log

    def update(self, log: LogModel):
        self.session.merge(log)
        self.session.commit()
        return log
