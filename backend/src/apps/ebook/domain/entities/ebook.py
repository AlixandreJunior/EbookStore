from dataclasses import dataclass

from apps.ebook.domain.entities.author import Author
from apps.ebook.domain.entities.category import Category
from apps.ebook.domain.entities.tag import Tag
from apps.ebook.domain.value_objects.ebook.file import File
from apps.ebook.domain.value_objects.ebook.price import Price
from apps.ebook.domain.value_objects.ebook.publication import Publication
from apps.ebook.domain.value_objects.ebook.visibility import Visibility



@dataclass(frozen=True)
class EbookEntity:
    id: int
    author: Author
    category: Category
    tags: list[Tag]
    publication: Publication
    price: Price
    file: File
    visibility: Visibility