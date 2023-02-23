from dataclasses import dataclass
from typing import Literal, Dict, List, Optional


    



@dataclass
class CharacterSchema:
    # def __init__(self, id: int, name: str, status: str):
    #     self.id = id
    #     self.name = name
    #     self.status = status
    id: int
    name: str
    status: Literal ['unknown', 'Alive', 'Dead']
    speices: str
    type: str
    gender: str
    origin: Dict[str, str]
    location: Dict[str, str]
    image: str
    episode: List[str]
    url: str
    created: str



class InfoSchema:
    def __init__(self, count: int, 
                 pages: int, 
                 next: Optional[str], 
                 prev: Optional[str] ) -> None:
        pass



@dataclass
class ResponseSchema:
    info: InfoSchema
    results: List[CharacterSchema]

    def __post_init__(self):
        self.info= InfoSchema(**self.info)
        self.results= [CharacterSchema(**x) for x in self.results]