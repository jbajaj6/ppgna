from Vec import Vec
from random import random
from WindowSingleton import hole_pos, valley_center, hill_center, moat_corners, circle_corners


def collide(pos, vel, dt):
    hit = False
    Nn = Vec(0, 0, 0)
    if pos.x <= -1.5:  # left wall
        Nn = Vec(1, 0, 0)
        hit = True
    if pos.x >= 1.5:  # right wall
        Nn = Vec(-1, 0, 0)
        hit = True
    if pos.y <= 0:  # bottom wall
        Nn = Vec(0, 1, 0)
        hit = True
    if pos.y >= 6:  # top wall
        Nn = Vec(0, -1, 0)
        hit = True
        
    for circle_corner in circle_corners:
        v = (circle_corner - pos)
        if v.magnitude() < 0.5:
            Nn = v.normalize()
            Nn *= -1
            # Nn.rotate(90)
            hit = True

    if hit:
        randomness = 0.004
        pos -= vel * dt
        Nn.rotate((0.5-random())*randomness)
        speed_kept = 1-(0.2*abs(vel.normalize().dot(Nn))+randomness*random())
        vel += 2*(Nn*abs(vel.dot(Nn)))*speed_kept

    return (pos, vel)


def checkInHole(pos, vel):
    effective_radius = - (1/32) * vel.magnitude() + 0.05
    if (hole_pos - pos).magnitude() < effective_radius:
        return True
    return False

def checkObstacles(pos):
    # hill
    direction = (pos - hill_center).normalize()
    hill_dist = (hill_center - pos).magnitude()
    if hill_dist <= 0.8 and hill_dist >= 0.5:
        return 0.2 * hill_dist * direction
    
    # valley
    direction = (valley_center - pos).normalize()
    valley_dist = (valley_center - pos).magnitude()
    if valley_dist <= 0.25:
        return 0.2 * valley_dist * direction
    elif valley_dist <= 0.5:
        return 0.05 / valley_dist * direction
    
    return Vec(0, 0, 0)

def checkMoat(pos):
    if pos.x > moat_corners[0].x and pos.x < moat_corners[1].x:
        if pos.y > moat_corners[0].y and pos.y < moat_corners[1].y:
            return True


def tick(forces, mass, velocity, position, dt):
    # if checkInHole(position, velocity):
    #     return (hole_pos, Vec(0, 0, 0))
    
    if checkMoat(position):
        return (position, Vec(0, 0, 0))

    position, velocity = collide(position, velocity, dt)
    
    forces += checkObstacles(position)

    acceleration = forces / mass
    velocity += acceleration * dt
    position += velocity * dt

    return (position, velocity)
