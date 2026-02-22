from apps.ebook.application.dtos.author import AuthorDTO
from apps.ebook.domain.entities.author import AuthorEntity


class AuthorDTOMapper:
    @staticmethod
    def to_entity(dto):
        return AuthorEntity(
            id=dto.id,
            bio=dto.bio,
            weblink=dto.weblink
        )
    
    @staticmethod
    def to_dto(entity):
        return AuthorDTO(
            id=entity.id,
            bio=entity.bio,
            weblink=entity.weblink
        )