from dataclasses import dataclass


@dataclass(frozen=True)
class Visibility:
    is_published: bool
    published_at: str