## Trimesh FastAPI
Welcome to the Trimesh FastAPI repository! This project aims to demonstrate the integration of the Trimesh library with FastAPI, creating a web API for processing and manipulating 3D mesh data.

## Overview
Trimesh FastAPI provides a RESTful API for handling various operations on 3D meshes. Leveraging the power of FastAPI, the API is designed to be efficient and easy to use. The integration with Trimesh allows users to perform tasks such as mesh processing, analysis, and visualization through simple HTTP requests.

## Features
Mesh Operations: Perform common operations on 3D meshes, including loading, processing, and exporting.

Analysis: Extract valuable information about the mesh, such as volume, surface area, and geometric properties.

Visualization: Generate visual representations of the mesh for analysis and debugging purposes.

Getting Started
To get started with Trimesh FastAPI, follow these steps:

## Clone the Repository:

bash
Copy code
git clone https://github.com/VeronikaNikolaevaValeva/Trimesh_FastAPI.git
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the FastAPI Application:

bash
Copy code
uvicorn main:app --reload
Explore the API:
Visit http://127.0.0.1:8000/docs to interact with the Swagger documentation and test the various API endpoints.

## API Endpoints
The API exposes the following endpoints:

POST /upload: Upload a 3D mesh file.

GET /info: Retrieve information about the uploaded mesh.

GET /analyze: Perform geometric analysis on the mesh.

GET /visualize: Generate a visual representation of the mesh.

Example Usage
Here is an example of using the API to upload a mesh file and retrieve information:

python
Copy code
import requests

url = "http://127.0.0.1:8000/upload"

files = {"file": open("path/to/your/mesh.obj", "rb")}

response = requests.post(url, files=files)

print(response.json())

Happy mesh processing with Trimesh FastAPI!
