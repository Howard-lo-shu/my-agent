from pydantic import BaseModel, Field


class MoveRequest(BaseModel):
    location: str = Field(min_length=1)


class ToolResult(BaseModel):
    result: str
