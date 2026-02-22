from dataclasses import dataclass

from apps.ebook.domain.entities.author import Author
from apps.ebook.domain.value_objects.ebook.file import File
from apps.ebook.domain.value_objects.ebook.price import Price
from apps.ebook.domain.value_objects.ebook.publication import Publication
from apps.ebook.domain.value_objects.ebook.visibility import Visibility



@dataclass(frozen=True)
class Ebook:
    id: int
    author: Author
    publication: Publication
    price: Price
    file: File
    visibility: Visibility