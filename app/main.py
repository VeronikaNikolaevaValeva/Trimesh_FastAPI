from fastapi import FastAPI
import numpy as np
from app.models import ValidSTL
import app.validateSTL as STLValidator

app = FastAPI()
#app/files/Klaverness 3.stl
#app/files/Insole2 STL Right.stl
#app/files/OneFIDrechts.stl
@app.post("/stl_general_Klaverness", response_model=ValidSTL)
async def measure_stl_3d(filePath: str):
    return STLValidator.process_stl_file(filePath)

@app.post("/stl_thickness_Design1_Left", response_model=ValidSTL)
async def measure_stl_3d(filePath: str):
    return STLValidator.process_stl_thickness(filePath)

@app.post("/stl_bottom_surface_Insole1_STL_Right=", response_model=ValidSTL)
async def measure_stl_3d(filePath: str):
    return STLValidator.process_stl_bottom_surface_area(filePath)



    