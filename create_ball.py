import prman
import math
import numpy as np

def draw_paraboloids(ri, points):
    for point in points :

        # calculate angles - don't think this works
        n_point = normalise(point)
        n_z = (0,0,1)
        axis = np.cross(n_point, n_z)
        n_axis = normalise(axis)
        cos_theta = np.dot(n_point, n_z)
        angle_radians = np.arccos(cos_theta)
        angle_degrees = np.degrees(angle_radians)

        # top hemisphere of paraboloids
        ri.TransformBegin()

        ri.Translate(point[0], point[1], point[2])
        ri.Rotate(float(angle_degrees), float(n_axis[0]), float(n_axis[1]), float(n_axis[2]))
        ri.Paraboloid(0.2, 0, 0.4, 360)

        ri.TransformEnd()

        # bottom hemisphere of paraboloids
        ri.TransformBegin()

        ri.Translate(-point[0], -point[1], -point[2])
        # ri.Rotate(180, -point[0], -point[1], 1-point[2])
        
        ri.Paraboloid(0.2, 0, 0.4, 360)

        ri.TransformEnd()



def fibonacci_sphere(samples=156, scale=1.0) :
    points = []
    phi = math.pi * (math.sqrt(5.)-1.)

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2 
        radius = math.sqrt(1 - y * y)

        theta = phi * i

        x = math.cos(theta) * radius * scale
        z = math.sin(theta) * radius * scale

        points.append((x, y * scale, z))
 
    return points

def calc_angles(start_angle, end_angle, num_angles) :
    angles = []
    angle_step = (end_angle-start_angle)/(num_angles-1)
    current_angle = start_angle
    for i in range(num_angles-1):
        angles.append(current_angle)
        current_angle += angle_step
    angles.append(current_angle)
    return angles

def create_positions(samples, theta, r):
    points = []
    
    for i in range(samples):
        phi = i * 2 * math.pi / samples
        x = r * math.cos(phi) * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta)) 
        z = r * math.sin(phi) * math.cos(math.radians(theta))

        points.append((x, y, z))
    return points


def normalise(vector):
    magnitude = math.sqrt(sum(x**2 for x in vector))
    normalised_vector = tuple(x / magnitude for x in vector)
    return normalised_vector

if __name__ == "__main__":
    ri = prman.Ri()

    filename = "__render"  #"Ball.rib"

    ri.Begin("__render")
    ri.Display("ball.tiff", "it", "rgb")
    ri.Format(720, 576, 1)
    ri.Projection(ri.PERSPECTIVE)

    ri.WorldBegin()

    ri.Translate(0, 0, 6)  
    # ri.Rotate(90,1,0,0)

   
    # ri.Sphere(2.55,-2.55,2.55,360)

    samples = [22,20,17,12,6,1]
    angles = calc_angles(7.66, 90, len(samples))

    ri.TransformBegin()
    # ri.Rotate(45, 0, 1, 0)
    for i in range(len(samples)):

        points = create_positions(samples[i], angles[i], 3)

        draw_paraboloids(ri, points)

    ri.TransformEnd()

    ri.TransformBegin()
    ri.AttributeBegin()
    ri.Declare("domeLight", "strings")
    ri.Rotate(-90, 1, 0, 0)
    ri.Rotate(100, 0, 0, 1)
    ri.Attribute("visibility", {"int camera": [1]})
    ri.Light("PxrDomeLight", "domeLight", {"string lightColorMap": "source_images/EnvMap.tx"})
    ri.AttributeEnd()
    ri.TransformEnd()


    ri.WorldEnd()

    ri.End()