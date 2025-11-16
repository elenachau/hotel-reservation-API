from typing import Any, Protocol

DataObject = dict[str, Any]

class DataInterface(Protocol):
    def read_by_id(self, id: int): # read obj fromn id
        ...
    
    def  read_all(self) -> list[DataObject]:
        ...
    
    def create(self, data: DataObject) -> DataObject:
        ...
    
    def update(self, id: int, data: DataObject) -> DataObject:
        ...
    
    def delete(self, id: int) -> DataObject:
        ...