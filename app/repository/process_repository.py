from sqlalchemy.orm import Session

from .repository import Repository

from ..model import ProcessModel

class ProcessRepository(Repository):
    def __init__(self, session: Session):
        super().__init__(session)

    def add(self, process: ProcessModel):
        self.session.add(process)
        self.session.commit()
        self.session.refresh(process)
        return process

    def get_by_id(self, process_id: int):
        return self.session.query(ProcessModel).filter(ProcessModel.id == process_id).first()

    def get_all(self):
        return self.session.query(ProcessModel).all()

    def delete(self, process_id: int):
        process = self.get_by_id(process_id)
        if process:
            self.session.delete(process)
            self.session.commit()
        return process

    def update(self, process: ProcessModel):
        self.session.merge(process)
        self.session.commit()
        return process