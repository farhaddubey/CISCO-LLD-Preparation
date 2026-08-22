from abc import ABC, abstractmethod
from enum import Enum 
from typing import Optional 


class Status(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

class BaseEntity(ABC):

    def __init__(self, entity_id : int):
        self.entity_id = entity_id

class Service:

    def __init__(eslf):
        self.entities: dict[int, BaseEntity] = {}

    def add(self, entity : BaseEntity) -> None:

        if entity.entity_id in self.entities:
            raise ValueError("Already Exists")

        self.entities[entity.entity_id] = entity 

    def get(self, entity_id : int) -> Optional[BaseEntity]: 

        return self.entities.get(entity_id)