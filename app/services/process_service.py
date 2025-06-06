from sqlalchemy.orm import Session
from typing import List, Optional

from ..dto import ProcessDTO
from ..model import ProcessModel
from ..repository import ProcessRepository

class ProcessService:
    def __init__(self, session: Session):
        self.repository = ProcessRepository(session)

    def create_process(self, process_dto: ProcessDTO) -> ProcessDTO:
        process = ProcessModel(
            name=process_dto.name
        )
        created = self.repository.add(process)
        return ProcessDTO.from_model(created)

    def get_process_by_id(self, process_id: int) -> Optional[ProcessDTO]:
        process = self.repository.get_by_id(process_id)
        return ProcessDTO.from_model(process) if process else None

    def get_all_processes(self) -> List[ProcessDTO]:
        processes = self.repository.get_all()
        return [ProcessDTO.from_model(process) for process in processes]

    def delete_process(self, process_id: int) -> bool:
        deleted_process = self.repository.delete(process_id)
        return deleted_process is not None

    def update_process(self, process_dto: ProcessDTO) -> Optional[ProcessDTO]:
        if process_dto.id is None:
            raise ValueError("ID obrigatório para atualização.")

        process = ProcessModel(
            id=process_dto.id,
            name=process_dto.name
        )
        updated = self.repository.update(process)
        return ProcessDTO.from_model(updated) if updated else None
