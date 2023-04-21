### Imports the libraries       #################################################################################################
import pygame
from pygame import gfxdraw
import random


### Window's settings           #################################################################################################
resolution = (1080,640)         # Resolution of the window

programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
pygame.init()                   # Initializes pygame
pygame.display.set_caption('Neural Network Vizualizer')      # The name of the window

window = pygame.display.set_mode(resolution)    # Initializes and create the window 

launched = True                 # Defines whether the window is launched or not (default is True)


### Neural Network's settings   #################################################################################################
nn_h_spacing = 120              # Horizontal spacing between the neurons of the neural network
nn_v_spacing = 60               # Vertical spacing between the neurons of the neural network
nn_layers    = [3,3,3]          # Layers of the neural network
nn_origin    = (100, 640/2)     # Center of the neural network ( x anchor is at the left of the neural network and y anchor is at the center of the neural network)


### Main functions               #################################################################################################
def d_circle(coord,radius, color):
    gfxdraw.filled_circle(window,int(coord[0]),int(coord[1]),radius,color)
def d_line(coords, width, color):
    pygame.draw.line(window,color,coords[0], coords[1], width)
def cd_neuron(coord,radius,brightness,thickness):
    d_circle(coord,radius,(255, 255, 255))
    d_circle(coord,radius-thickness,(200*brightness,200*brightness,200*brightness))


### Neural network function     #################################################################################################
def d_tree(origin,r,space):
    neurons_positions = []                          # Save the positions of the neurons in the window
    
    for i in range(len(r)):                         # Loop x times depending on the length of the array r[]
        neurons_positions.append([])                # Add an element to the array containing the positions of the neurons in the layer
        temp_neuron_position = []                   # Create an array containing temporary the position of the neurons in the layer i 
        
        for j in range(r[i]):                       # Loop the number of time the number of neurons in the layer is defined in the array r, for example r=[2] means that there's two neurons
            temp_neuron_position.append((origin[0]+i*space[0]*1.5,origin[1]+(r[i]/2-0.5)*space[1] - j*space[1] ))           # Add the position of the neuron in the temporary array so each positions will be stored in an array of positions of neurons from the same layer, which will then be stored in the array neurons_positions[]
        
        neurons_positions[i]=temp_neuron_position   # Set the elements of the array neurons_positions previously created l20 to the temporary array from the previous loop
    
    for o in range(len(neurons_positions)-1):       # Loop x-1 times depending on the length of the array neurons_positions[], it's not x times because the lines are created between the x-1-th and x-th position for the last layer
        
        for p in neurons_positions[o]:              # Loop through the elements of the array neurons_positions[] for the o-th layer
            
            for u in neurons_positions[o+1]:        # Loop through the elements of the array neurons_positions[] for the o+1-th layer
                if random.randint(0,1) == 1:
                    clr = (131, 191, 104)
                else: 
                    clr = (217, 121, 89)
                d_line([(p[0],p[1]),(u[0],u[1])], 2, clr)          # Draw a line between the o-th position and the o+1-th position, between every neurons from the current layer and the next one
    
    # Draw the neurons on top of the lines so it's cleaner and easier to visualize/read
    for o in range(len(neurons_positions)):
        
        for p in neurons_positions[o]:
            cd_neuron(p,20,0,2)
    
### The loop for the window     #################################################################################################
while launched:                 # Keep running until the window is closed
    
    d_tree(nn_origin,nn_layers,(nn_h_spacing,nn_v_spacing))
    pygame.display.update()
    
    
    for event in pygame.event.get():        # Catch the events 
        if event.type == pygame.QUIT:       # If the window is closed, set launched to False and end the loop
            launched = False
            pygame.quit()
            
