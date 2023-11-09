from pydantic import BaseModel
from typing import Optional, Sequence

class ValidSTL(BaseModel):
    isBottomSurfaceLargeEnough: str = None
    correctDimensions: bool = None
    correctPosition: bool = None
    isWatertight: bool = None
    