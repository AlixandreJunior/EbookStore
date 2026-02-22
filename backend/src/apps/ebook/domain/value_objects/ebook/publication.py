from dataclasses import dataclass
from enum import Enum

class Language(Enum):
    ENGLISH = "en"
    SPANISH = "es"
    PORTUGUESE = "pt"
    
@dataclass(frozen=True)
class Publication:
    title: str
    slug: str
    cover: bytes
    description: str
    author: str
    language: Language
