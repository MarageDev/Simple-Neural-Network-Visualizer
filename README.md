<h1 align="center"> Simple-Neural-Network-Visualizer </h2>
<p align="center">
This is a simple Python program to visualize neural networks ( only the one where each perceptron of a layer are linked to all the other ones of the next layer ).
</p>

> This program was made just to test pygame and as I was learning more about neural networks, I wanted to try to create a neural network visualizer 

## Requirements 
The program requires PyGame, it can be installed like that :
```console
pip install pygame
```
> You can find more information on the website https://www.pygame.org/

## Information
### Configuration of the layers in the neural network

<img align="right" width="500px" src="https://user-images.githubusercontent.com/76840739/233704478-eccef435-6ddf-46f4-86ff-e7553081a760.png" title="neural network visualizer result">

You can change the number of perceptrons and the number of layers by editing the variable `nn_layers` ( neural network layers ), by default it is set to : 
```python
nn_layers    = [2,5,3,8,2,1]    # Layers of the neural network
```
> Note : the color of the connections have random colors ( red or green )


### Spacing between the layers and perceptrons
The horizontal and vertical spacing of the neural network can be modified to make it more "read-able" with the variables `nn_h_spacing` and `nn_v_spacing`:
```python 
nn_h_spacing = 120              # Horizontal spacing between the perceptrons of the neural network
nn_v_spacing = 60               # Vertical spacing between the perceptrons of the neural network
```


### Position of the neural network
Its position can be changed with the variable `nn_origin` :
```python 
nn_origin    = (100, resolution[1]/2)     # Center of the neural network ( x anchor is at the left of the neural network and y anchor is at the center of the neural network)
```


### Additional information
Most of the parts of the code are commented. 

## Possible updates
- Use of martices to display it instead of an array of integers
- Addition of a real neural network logic and not only a visualization of it
