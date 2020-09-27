import math

def in_his_footsteps(steps):
    """
    A math function that approximates pi using even steps around
    a unit circle, similar to how Archimedes discovered pi by walking around
    a circle of a known area in 250 bce


    """
    radius = 1 # unit circle
    theta = 2*math.pi/steps #internal angle of each triangle at center is 2pi/steps
    half_theta = theta/2 # split isosceles into two right angles triangles
    hypotenuse = radius # Hypotenuse is the radius in this case
    half_opposite = math.sin(half_theta) * hypotenuse # opposite is h*sin(theta)
    triangle_perimeter = half_opposite*2*steps # total perimeter length of all triangles
    pi_approx = triangle_perimeter/2*radius
    pi_diff = round(math.pi - pi_approx,3)
    return "{} even steps around a circle would have gotten Archimedes within {} of pi".format(steps, pi_diff)
