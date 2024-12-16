#%%
import turtle
import random
import math

# %%
def draw_until_break(starting_x, starting_y, starting_angle, branch_length, breaking_angle):
    turtle.width(2)
    turtle.penup()
    turtle.goto(starting_x, starting_y)
    turtle.setheading(starting_angle)  # Apontando para cima
    turtle.pendown()

    new_angle = starting_angle
    for l in range(0, branch_length):
        turtle.forward(1)
        delta_angle = random.randint(-5, 5)
        turtle.right(delta_angle)
        new_angle = new_angle + delta_angle
        print(new_angle)
        if abs(new_angle - starting_angle) > breaking_angle:
            break

# draw_until_break(0, -250, 90, 500, 25)
# %%

# branch = {
#     'id': 1, 
#     'active': True,
#     'starting_angle': 90,
#     'breaking_angle': 20,
#     'starting_x': 0,
#     'starting_y': -250,
#     'x_series': [],
#     'y_series': [],
#     'angle_series': [],
#     'length': 0,
#     'width': 2
# }

# branches = {}
def draw_branch(x, y, angle, width):

    delta_angle = random.randint(-5, 5)

    turtle.penup()
    turtle.width()
    turtle.goto(x, y)

    return angle


def orquestrate_branches(total_length):

    branches = {
        '0': {
            'active': True,
            'starting_angle': 90,
            'breaking_angle': 20,
            'starting_x': 0,
            'starting_y': -250,
            'x_series': [],
            'y_series': [],
            'angle_series': [],
            'length': 0,
            'width': 2
        }
    }

    for _ in range(0, total_length):

        for branch_id, branch_data in branches.items():

            turtle.

            print(branch_id, branch_data)

draw_branches(250)