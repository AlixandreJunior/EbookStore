from dataclasses import dataclass
from enum import Enum


class FileFormat(Enum):
    PDF = "pdf"
    EPUB = "epub"
    MOBI = "mobi"


@dataclass(frozen=True)
class File:
    name: str
    content: bytes
    format: FileFormat