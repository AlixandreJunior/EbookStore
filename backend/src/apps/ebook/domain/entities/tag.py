from dataclasses import dataclass

from apps.ebook.domain.value_objects.slug import Slug



@dataclass(frozen=True)
class TagEntity:
    id: int
    name: str
    slug: Slug
    is_active: bool = True