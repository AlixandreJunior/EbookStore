from dataclasses import dataclass
from datetime import date

from apps.ebook.domain.value_objects import visibility
from apps.ebook.domain.value_objects.ebook import money
from apps.ebook.domain.value_objects.ebook.file import File
from apps.ebook.domain.value_objects.ebook.price import Price
from apps.ebook.domain.value_objects.ebook.publication import Publication
from apps.ebook.domain.value_objects.ebook.visibility import Visibility



@dataclass(frozen=True)
class Ebook:
    id: int
    publication: Publication
    price: Price
    file: File
    visibility: Visibility