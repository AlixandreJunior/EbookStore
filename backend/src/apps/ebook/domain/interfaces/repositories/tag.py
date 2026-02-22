from apps.ebook.domain.entities.tag import TagEntity
from apps.ebook.domain.value_objects.slug import Slug


class TagRepositoryInterface:
    def save_tag(self, tag: TagEntity) -> TagEntity:
        raise NotImplementedError

    def get_by_id(self, tag_id: int) -> TagEntity:
        raise NotImplementedError

    def get_by_slug(self, slug: Slug) -> TagEntity:
        raise NotImplementedError

    def list_all(self) -> list[TagEntity]:
        raise NotImplementedError