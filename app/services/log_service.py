from sqlalchemy.orm import Session

from ..dto import LogDTO
from ..model import LogModel
from ..repository import LogRepository

from typing import List, Optional

class LogService:
    def __init__(self, session:Session):
        self.repository = LogRepository(session)

    def create_log(self, log_dto: LogDTO) -> LogDTO:
        log = LogModel(
            id_process=log_dto.id_process,
            status_code=log_dto.status_code,
            message=log_dto.message
        )
        created = self.repository.add(log)
        return LogDTO.from_model(created)

    def get_log_by_id(self, log_id: int) -> Optional[LogDTO]:
        log = self.repository.get_by_id(log_id)
        return LogDTO.from_model(log) if log else None

    def get_all_logs(self) -> List[LogDTO]:
        logs = self.repository.get_all()
        return [LogDTO.from_model(log) for log in logs]

    def delete_log(self, log_id: int) -> bool:
        deleted_log = self.repository.delete(log_id)
        return deleted_log is not None

    def update_log(self, log_dto: LogDTO) -> Optional[LogDTO]:
        if log_dto.id is None:
            raise ValueError("ID obrigatório para atualização.")
        
        log = LogModel(
            id=log_dto.id,
            id_process=log_dto.id_process,
            status_code=log_dto.status_code,
            timestamp=log_dto.timestamp,
            message=log_dto.message
        )
        updated = self.repository.update(log)
        return LogDTO.from_model(updated)
