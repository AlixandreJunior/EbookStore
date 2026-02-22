from dataclasses import dataclass


@dataclass(frozen=True)
class AuthorEntity:
    id: int
    bio: str
    weblink: str