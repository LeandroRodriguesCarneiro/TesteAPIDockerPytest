from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from ..model import LogModel

@dataclass
class LogDTO:
    id: Optional[int]
    id_process: int
    status_code: int
    message: str
    timestamp: Optional[datetime] = None

    @classmethod
    def from_model(cls, log: LogModel) -> 'LogDTO':
        return cls(
            id=log.id,
            id_process=log.id_process,
            status_code=log.status_code,
            timestamp=log.timestamp,
            message=log.message
        )
