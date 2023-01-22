import copy
from abc import ABCMeta
from dataclasses import dataclass
from typing import Generic, TypeVar, Type


@dataclass
class ModelBase:
    id: int


QueryBaseType = TypeVar("QueryBaseType", bound=ModelBase)


class QueryBase(Generic[QueryBaseType], metaclass=ABCMeta):
    class NotFoundError(Exception):
        pass

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()

        class NotFoundError(QueryBase.NotFoundError):
            pass

        cls.NotFoundError: Type["QueryBase.NotFoundError"] = NotFoundError  # type: ignore

    def __init__(self, models: list[QueryBaseType]):
        self.models: list[QueryBaseType] = models

    def all(self) -> list[QueryBaseType]:
        return self.models

    def get(self, id: int) -> QueryBaseType:
        for model in self.models:
            if model.id == id:
                return model

        raise self.NotFoundError()
