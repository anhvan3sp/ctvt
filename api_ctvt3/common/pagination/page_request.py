from dataclasses import dataclass


@dataclass
class PageRequest:
    page: int
    size: int
