from dataclasses import dataclass
from typing import Generic, List, TypeVar

T = TypeVar("T")


@dataclass
class PageResponse(Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
