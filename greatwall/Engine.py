from Vec import Vec
from random import random
from WindowSingleton import hole_pos, valley_center, hill_center, wall_corners


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
        
    # vertical wall
    if pos.y >= wall_corners[0][0].y and pos.y <= wall_corners[0][1].y:
        # print("hi")
        if (pos + vel * dt).x >= wall_corners[0][0].x and pos.x <= wall_corners[0][0].x:
            Nn = Vec(-1, 0, 0)
            hit = True
        if (pos + vel * dt).x <= wall_corners[0][0].x and pos.x >= wall_corners[0][0].x:
            Nn = Vec(1, 0, 0)
            hit = True
    
    # diagonal wall
    P = pos + vel * dt
    B = valley_center
    A = hill_center
    
    # if ((wall_corners[1][1] - wall_corners[1][0]) - ((next_pos - wall_corners[1][0]) + (wall_corners[1][1] - next_pos))).magnitude() > 0.01:
    if (((B-P).magnitude()+(A-P).magnitude()) - (A-B).magnitude()) < 0.001:
            Nn = (wall_corners[1][1] - wall_corners[1][0]).normalize()
            if 2 * P.x + 3 > P.y:
                Nn.rotate(90)
            else:
                Nn.rotate(-90)
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
    if hill_dist <= 0.5:
        return 0.2 * hill_dist * direction
    elif hill_dist <= 1:
        return 0.05 / hill_dist * direction
    
    # valley
    direction = (valley_center - pos).normalize()
    valley_dist = (valley_center - pos).magnitude()
    if valley_dist <= 0.5:
        return 0.2 * valley_dist * direction
    elif valley_dist <= 1:
        return 0.05 / valley_dist * direction
    
    return Vec(0, 0, 0)


def tick(forces, mass, velocity, position, dt):
    # if checkInHole(position, velocity):
    #     return (hole_pos, Vec(0, 0, 0))

    position, velocity = collide(position, velocity, dt)
    
    forces += checkObstacles(position)

    acceleration = forces / mass
    velocity += acceleration * dt
    position += velocity * dt

    return (position, velocity)
