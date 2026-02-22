import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Slug:
    value: str

    def __post_init__(self):
        normalized = self.value.strip().lower()

        if not normalized:
            raise ValueError("Slug cannot be empty")

        if not re.match(r"^[a-z0-9-]+$", normalized):
            raise ValueError(
                "Slug must contain only lowercase letters, numbers, and hyphens"
            )

        object.__setattr__(self, "value", normalized)

    def __str__(self):
        return self.value