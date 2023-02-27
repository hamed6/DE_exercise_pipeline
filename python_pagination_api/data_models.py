from dataclasses import dataclass
from typing import Literal, Dict, List, Optional



@dataclass
class CharacterSchema:

    id: int
    name: str
    status: Literal ['unknown', 'Alive', 'Dead']
    species: str
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
        self.count = count
        self.pages = pages
        self.next = next
        self.prev = prev

@dataclass
class ResponseSchema:
    info: InfoSchema
    results: List[CharacterSchema]

    def __post_init__(self):
        self.info= InfoSchema(**self.info)
        self.results= [CharacterSchema(**x) for x in self.results]

@dataclass
class FilterApi:
    page: Optional[str] = None
    name: Optional[str] = None
    status: Optional[Literal['unknown', 'Alive', 'Dead']] = None
    species: Optional[str]= None
    type: Optional[str] = None
    gender: Optional[Literal['female', 'male', 'genderless', 'unknown']] = None