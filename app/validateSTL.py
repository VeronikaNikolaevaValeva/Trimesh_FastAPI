import numpy as np
import trimesh
import pyvista as pv
from app.models import ValidSTL

const_bounds = [60, 150, 500]

def process_stl_file(filePath: str) -> ValidSTL:
    validSTL = ValidSTL()
    mesh = trimesh.load(filePath, process=False)
    validSTL.isBottomSurfaceLargeEnough = check_if_bottom_surface_is_large_enough(mesh)
    validSTL.correctDimensions = measure_stl_dimension(mesh)
    validSTL.correctPosition = measure_stl_position(mesh)
    validSTL.isWatertight = measure_stl_watertightness(mesh)
    return validSTL

def process_stl_thickness(filePath: str):
    mesh = trimesh.load(filePath, process=False)
    measure_stl_thickness(mesh)
    return None

def process_stl_bottom_surface_area(filePath: str):
    mesh = trimesh.load(filePath, process=False)
    check_if_bottom_surface_is_flat(mesh)
    return None

##################

def measure_stl_thickness(mesh: trimesh) -> bool: 
    start_points = mesh.vertices - (0.09 * mesh.vertex_normals) # done to get the vertices slightly inside
    thickness = trimesh.proximity.thickness(mesh, start_points, normals=mesh.vertex_normals)
    pv.wrap(mesh).plot(scalars=thickness) #visualized by pyvista
    return None

def measure_stl_watertightness(mesh: trimesh) -> bool:   
    if mesh.is_empty: return False
    if not mesh.is_watertight: 
        return mesh.fill_holes() #Check if a mesh has all the properties required to represent a valid volume, rather than just a surface.
    return mesh.is_watertight


def measure_stl_dimension(mesh: trimesh) -> bool:
    arranged_bounds= get_mesh_bounds_in_length(mesh)
    arranged_bounds.sort()
    for i in range(2):
        if(arranged_bounds[i]>const_bounds[i]):
            return False
    return True


def measure_stl_position(mesh: trimesh) -> bool:
    arranged_bounds= get_mesh_bounds_in_length(mesh)
    x_bound = arranged_bounds[0]
    y_bound = arranged_bounds[1]
    z_bound = arranged_bounds[2]
    if not y_bound < x_bound < z_bound: return False
    return True


def get_mesh_bounds_in_length(mesh: trimesh) -> list:
    listOfBoundCorners = trimesh.bounds.corners(mesh.bounding_box_oriented.bounds)
    if listOfBoundCorners.__len__()>8:
        return False
    x_corners = []
    y_corners = []
    z_corners = []

    for bound in listOfBoundCorners:
        if not x_corners.__contains__(bound[0]):
            x_corners.append(bound[0])
        if not y_corners.__contains__(bound[1]):
            y_corners.append(bound[1])
        if not z_corners.__contains__(bound[2]):
            z_corners.append(bound[2])

    x_bound = round(np.max(x_corners) - np.min(x_corners))
    y_bound = round(np.max(y_corners) - np.min(y_corners))
    z_bound = round(np.max(z_corners) - np.min(z_corners))
    arranged_bounds = [x_bound, y_bound, z_bound]
    return arranged_bounds


def check_if_bottom_surface_is_flat(mesh: trimesh) -> bool:
    up_axis = 2 # z vertical axis
    bottom_threshold = -0.99
    radius = 0.9

    bottom_mask = mesh.vertex_normals[:, up_axis] < bottom_threshold 
    mean_curvature = trimesh.curvature.discrete_gaussian_curvature_measure(mesh, mesh.vertices, radius)
    mean_curvature[~bottom_mask ] = 0 # we are not interested in the curvature of the upper part
    
    pv.wrap(mesh).plot(scalars=mean_curvature) #visualized by pyvista
    print(mean_curvature)
    return None


def check_if_bottom_surface_is_large_enough(mesh: trimesh) -> bool:
    up_axis = 2 # z vertical axis
    bottom_threshold = -0.99
    top_threshold = 0.25

    bottom_mask = mesh.vertex_normals[:, up_axis] < bottom_threshold 
    top_mask = mesh.vertex_normals[:, up_axis] > top_threshold 

    triangle_bottom_mask = np.any(bottom_mask[mesh.faces],axis=-1)
    triangle_top_mask =  np.any(top_mask[mesh.faces],axis=-1)

    bottom_area = trimesh.triangles.area(mesh.triangles[triangle_bottom_mask])
    top_area = trimesh.triangles.area(mesh.triangles[triangle_top_mask])

    return f'The bottom of the insole is at {int(100 * np.sum(bottom_area)/np.sum(top_area))}% of the top surface area of the insole'
    
