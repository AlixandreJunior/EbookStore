from dataclasses import dataclass
from typing import Self

from apps.ebook.domain.value_objects.category.icon import Icon
from apps.ebook.domain.value_objects.slug import Slug


@dataclass(frozen=True)
class Category:
    id: int
    name: str
    slug: Slug
    description: str
    parent: Self | None
    icon: Icon
    is_active: bool