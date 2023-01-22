from dataclasses import dataclass
from typing import TypeVar

from query_typing.model_base import ModelBase, QueryBase


@dataclass
class EmployeeModel(ModelBase):
    department_id: int | None
    name: str


EmployeeModelType = TypeVar("EmployeeModelType", bound=EmployeeModel)


class EmployeeQuery(QueryBase[EmployeeModelType]):
    pass


@dataclass
class DepartmentModel(ModelBase):
    parent_id: int | None
    name: str


DepartmentModelType = TypeVar("DepartmentModelType", bound=DepartmentModel)


class DepartmentQuery(QueryBase[DepartmentModelType]):
    pass
