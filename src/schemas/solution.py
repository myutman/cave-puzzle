from pydantic import BaseModel

class Solution(BaseModel):
    field: list[list[int]]
    field_colors: list[list[int]]
