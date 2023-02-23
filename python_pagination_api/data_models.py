from dataclasses import dataclass
from typing import Literal, Dict, List


    



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