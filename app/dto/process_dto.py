from dataclasses import dataclass
from typing import Optional

from ..model import ProcessModel

@dataclass
class ProcessDTO:
    id: Optional[int]
    name: str

    @classmethod
    def from_model(cls, process: ProcessModel) -> 'ProcessDTO':
        return cls(
            id=process.id,
            name=process.name
        )
