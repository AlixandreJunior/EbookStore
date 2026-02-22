from apps.ebook.domain.entities.author import Author


class AuthorRepositoryInterface:
    def get_by_id(self, author_id: int) -> Author:
        raise NotImplementedError

    def create(self, author: Author) -> Author:
        raise NotImplementedError

    def update(self, author: Author) -> Author:
        raise NotImplementedError

    def delete(self, author_id: int) -> None:
        raise NotImplementedError