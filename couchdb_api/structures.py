from dataclasses import dataclass, field
from typing import Optional, TypedDict


class View(TypedDict):
    map: str
    reduce: Optional[str]


class ViewOption(TypedDict):
    local_seq: bool
    include_design: bool


@dataclass
class DesignDocument:
    language: Optional[str] = None
    options: Optional[ViewOption] = None
    filters: Optional[dict[str, str]] = None
    updates: Optional[dict[str, str]] = None
    validate_doc_update: Optional[str] = None
    views: Optional[dict[str, View]] = None
    autoupdate: Optional[bool] = None


@dataclass
class SecurityObjectUserList:
    names: list[str] = field(default_factory=list)
    roles: list[str] = field(default_factory=list)


@dataclass
class SecurityObject:
    members: SecurityObjectUserList
    admins: SecurityObjectUserList
