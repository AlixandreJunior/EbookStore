from dataclasses import dataclass


@dataclass(frozen=True)
class Icon:
    content: bytes
    max_size: int = 1024 * 1024

    def __post_init__(self):
        if not isinstance(self.content, bytes):
            raise ValueError("Icon content must be bytes")

        if len(self.content) == 0:
            raise ValueError("Icon cannot be empty")

        if len(self.content) > self.max_size:
            raise ValueError("Icon exceeds maximum allowed size")

    @property
    def size(self) -> int:
        return len(self.content)