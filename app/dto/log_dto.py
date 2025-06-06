from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from ..model import LogModel

@dataclass
class LogDTO:
    id: Optional[int]
    process_id: int
    status_code: int
    message: str
    timestamp: Optional[datetime] = None
    process_name: Optional[str] = None

    @classmethod
    def from_model(cls, log: LogModel) -> 'LogDTO':
        return cls(
            id=log.id,
            process_id=log.id_process,
            process_name=log.process.name if log.process else None,
            status_code=log.status_code,
            message=log.message,
            timestamp=log.timestamp
        )