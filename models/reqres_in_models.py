from pydantic import BaseModel, ConfigDict, Field


class User(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    id_: int = Field(alias="id")
    email: str
    first_name: str
    last_name: str
    avatar: str


class Resource(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    id_: int = Field(alias="id")
    name: str
    year: int
    color: str
    pantone_value: str


class Support(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    url: str
    text: str


class ListUsers(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[User]
    support: Support


class ListResources(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[Resource]
    support: Support


class SingleUser(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    data: User
    support: Support


class SingleResource(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    data: Resource
    support: Support
