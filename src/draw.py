#%%
import turtle
import random
import math
from time import sleep

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

def split_branches(branches, parent_id, angle_opening=75, n_childs=2):
    
    if n_childs == 'random':
        n_childs = random.randint(2, 3)
    
    parent_branch = branches[parent_id]
    parent_x = parent_branch['x_series'][-1]
    parent_y = parent_branch['y_series'][-1]
    parent_angle = parent_branch['angle_series'][-1]
    parent_angle_range_module = parent_branch['angle_range_module']
    parent_maximum_length = parent_branch['maximum_branch_length']
    parent_width = parent_branch['width']
    
    for b in range(1,n_childs+1):
        child_id = f'{parent_id}.{b}'
        child_starting_angle = parent_angle - angle_opening + angle_opening*b/2 
        child_angle_range_module = parent_angle_range_module * 0.5
        child_width = parent_width - 1 if parent_width > 1 else 1
        lower_bound, upper_bound = (0.4, 0.7) if parent_width <= 2 else (0.5, 1)
        maximum_child_length = random.randint(math.ceil(parent_maximum_length * lower_bound), math.ceil(parent_maximum_length * upper_bound))
        if maximum_child_length > 4:
            branches[child_id] = {
                'active': True,
                'starting_angle': child_starting_angle,
                'angle_range_module': child_angle_range_module,
                'starting_x': parent_x,
                'starting_y': parent_y,
                'x_series': [],
                'y_series': [],
                'angle_series': [],
                'length': 0,
                'maximum_branch_length': maximum_child_length,
                'width': child_width
            }
        


def draw_branch(x, y, angle, length=1, width=1):

    new_angle = random.normalvariate(0, 6) + angle
    turtle.speed(0)
    turtle.penup()
    turtle.width(width)
    turtle.goto(x, y)
    turtle.setheading(new_angle)
    
    turtle.pendown()
    turtle.forward(length)
    
    new_x, new_y = turtle.pos()
    
    return new_x, new_y, new_angle


def orquestrate_branches(branches):    
    
    # ==== INLCUIR EM NOVO PIPELINE QUE IRÁ ORQUESTRAR TODO O DESENHO =====
    turtle.hideturtle()
    turtle.pencolor('#ebb9c2')
    turtle.bgcolor('black')
    # =====================================================================
    
    for i in range(0, 140):
        
       
        
        for branch_id, branch_data in list(branches.items()):
            
            if branch_data['active']:
            
                if len(branch_data['x_series']) == 0:
                    current_x = branch_data['starting_x']
                    current_y = branch_data['starting_y']
                    current_angle = branch_data['starting_angle']
                else:
                    current_x = branch_data['x_series'][-1]
                    current_y = branch_data['y_series'][-1]
                    current_angle = branch_data['angle_series'][-1]
                
                current_width = branch_data['width']

                result_x, result_y, result_angle = draw_branch(current_x, current_y, current_angle, 5, current_width)
                
                branches[branch_id]['length'] += 1
                branches[branch_id]['x_series'].append(result_x)
                branches[branch_id]['y_series'].append(result_y)
                branches[branch_id]['angle_series'].append(result_angle)
                if branches[branch_id]['maximum_branch_length'] < 4:
                    branch_data['active'] = False
                elif branches[branch_id]['length'] >= branches[branch_id]['maximum_branch_length']:
                    branch_data['active'] = False
                    split_branches(branches=branches, parent_id=branch_id, n_childs='random')

    from datetime import datetime
    now = datetime.now().strftime('%Y%m%d%H%M')
    
    canvas = turtle.getcanvas()
    canvas.postscript(file="drawing.eps")
    from PIL import Image

    # Convert EPS to PNG
    image = Image.open("drawing.eps")
    image.save(rf"data/images/drawing_{now}.png")
    
    import json
    
    with open(rf"data/json/output_{now}.json", "w") as json_file:
        json.dump(branches, json_file, indent=4)  # 4 spaces for indentation
    

for _ in range(0, 50):
    
    branches = {
        '1': {
            'active': True,
            'starting_angle': 90,
            'angle_range_module': 15,
            'starting_x': 0,
            'starting_y': -250,
            'x_series': [],
            'y_series': [],
            'angle_series': [],
            'length': 0,
            'maximum_branch_length': 30,
            'width': 6
        }
    }
    
    orquestrate_branches(branches)
    
    turtle.reset()