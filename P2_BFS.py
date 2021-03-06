#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:46:49 2021

@author: jayesh
"""

import numpy as np
import copy
import time
import ast
import cv2
import pygame
import os

#Creating an image to use for animation
img = np.zeros((301, 401), np.uint8)
oblist=[] #List to store the obstacle coordinates

#Function to traverse in the downward direction
def ActionMoveDown(curr_node):
    #print('down')
    curr_node1 = copy.deepcopy(curr_node)
    x = curr_node1[0]
    y = curr_node1[1]
    curr_node = (x,y)
    new_node=()
    new_node_x = curr_node1[0]
    new_node_y = curr_node1[1]
    new_node_y-=1
    new_node = [new_node_x,new_node_y]
    if new_node[0]>=0 and new_node[1]>=0:
        return(new_node,True)
    else:
        return(curr_node1,False)

#Function to traverse in the upward direction
def ActionMoveUp(curr_node):
    #print('up')
    curr_node1 = copy.deepcopy(curr_node)
    x = curr_node1[0]
    y = curr_node1[1]
    curr_node = (x,y)
    new_node=()
    new_node_x = curr_node1[0]
    new_node_y = curr_node1[1]
    new_node_y+=1
    new_node = [new_node_x,new_node_y]
    if new_node[0]>=0 and new_node[1]>=0:
        return(new_node,True)
    else:
        return(curr_node1,False)

#Function to traverse to the left
def ActionMoveLeft(curr_node):
    #print('left')
    curr_node1 = copy.deepcopy(curr_node)
    x = curr_node1[0]
    y = curr_node1[1]
    curr_node = (x,y)
    new_node=()
    new_node_x = curr_node1[0]
    new_node_x-=1
    new_node_y = curr_node1[1]
    new_node = [new_node_x,new_node_y]
    if new_node[0]>=0 and new_node[1]>=0:
        return(new_node,True)
    else:
        return(curr_node1,False)

#Function to traverse to the right
def ActionMoveRight(curr_node):
    #print('right')
    curr_node1 = copy.deepcopy(curr_node)
    x = curr_node1[0]
    y = curr_node1[1]
    curr_node = (x,y)
    new_node=()
    new_node_x = curr_node1[0]
    new_node_x+=1
    new_node_y = curr_node1[1]
    new_node = [new_node_x,new_node_y]
    if new_node[0]>=0 and new_node[1]>=0:
        return(new_node,True)
    else:
        return(curr_node1,False)

#Function to traverse in the upward left direction
def ActionMoveUL(curr_node):
    #print('ul')
    curr_node1 = copy.deepcopy(curr_node)
    x = curr_node1[0]
    y = curr_node1[1]
    curr_node = (x,y)
    new_node=()
    new_node_x = curr_node1[0]
    new_node_x -=1
    new_node_y = curr_node1[1]
    new_node_y+=1
    new_node = [new_node_x,new_node_y]
    if new_node[0]>=0 and new_node[1]>=0:
        return(new_node,True)
    else:
        return(curr_node1,False)

#Function to traverse in the upward right direction
def ActionMoveUR(curr_node):
    #print('ur')
    curr_node1 = copy.deepcopy(curr_node)
    x = curr_node1[0]
    y = curr_node1[1]
    curr_node1 = (x,y)
    new_node=()
    new_node_x = curr_node1[0]
    new_node_x+= 1
    new_node_y = curr_node1[1]
    new_node_y+= 1
    new_node = [new_node_x,new_node_y]
    if new_node[0]>=0 and new_node[1]>=0:
        return(new_node,True)
    else:
        return(curr_node1,False)

#Function to traverse in the downward left direction
def ActionMoveDL(curr_node):
    #print('dl')
    curr_node1 = copy.deepcopy(curr_node)
    x = curr_node1[0]
    y = curr_node1[1]
    curr_node = (x,y)
    new_node=()
    new_node_x = curr_node1[0]
    new_node_x-=1
    new_node_y = curr_node1[1]
    new_node_y-=1
    new_node = [new_node_x,new_node_y]
    if new_node[0]>=0 and new_node[1]>=0:
        return(new_node,True)
    else:
        return(curr_node1,False)
    
#Function to traverse in the downward right direction
def ActionMoveDR(curr_node):
    #print('dr')
    curr_node1 = copy.deepcopy(curr_node)
    x = curr_node1[0]
    y = curr_node1[1]
    curr_node = (x,y)
    new_node=()
    new_node_x = curr_node1[0]
    new_node_x+=1
    new_node_y = curr_node1[1]
    new_node_y-=1
    new_node = [new_node_x,new_node_y]
    if new_node[0]>=0 and new_node[1]>=0:
        return(new_node,True)
    else:
        return(curr_node1,False)

#Function run initially to set the obstacle coordinates in the image and append to a list
def getobstaclespace():
    #print('ob space')
    for x in range(0,401):
        for y in range(0,301):
            #Rectangle Shaped Obstacle
            if y-0.7*x>=74.28 and y-0.7*x <= 98.76 and y+1.42*x>=176.42 and y+1.384*x<=430.619:
                img[y][x]=255
                oblist.append([x,y])
                
            #Circle Obstacle
            if ((x-90)**2 + (y-70)**2)<(35**2):
                img[y][x]=255
                oblist.append([x,y])
                
            #Ellipse Object
            if(((x-246)**2)/60**2 +((y-145)**2)/30**2 <= 1):
                img[y][x]=255
                oblist.append([x,y])

            #Polygon shaped obstacle 
            if y-x>=-265 and y+x>=391 and y-x<=-180.22 and y+0.98*x<=464.237:
                img[y][x]=255
                oblist.append([x,y])

            if x<=381.4 and y-171.4<=0 and y-1.21*x<=-293.51 and y-x>=-265 and x>=328:# and y+0.25*x<=224.95
                img[y][x]=255
                oblist.append([x,y])
            
            #U shaped pbstacle
            if (x>=200 and x<=230) and (y>=230 and y<=280):    
                if (x>=200 and x<=210 and y>=240 and y<=270):
                    img[y][x]=255
                    oblist.append([x,y])
                if (y>=270 and y<=280 and x>=210 and x<=230):
                    img[y][x]=255
                    oblist.append([x,y])
                if (y>=230 and y<=240 and x>=210 and x<=240):
                    img[y][x]=255
                    oblist.append([x,y])
                if (x<=210 and y<=240):
                    img[y][x]=255
                    oblist.append([x,y])
                if (x<=210 and y>=270 and y<=280):
                    img[y][x]=255
                    oblist.append([x,y])
           
#Function to check if node is in obstacle space or not
def obstaclecheck(curr_node):
    curr_node1 = copy.deepcopy(curr_node)
    x = curr_node1[0]
    y = curr_node1[1]
    
    if y-0.7*x>=74.28 and y-0.7*x <= 98.76 and y+1.42*x>=176.42 and y+1.384*x<=430.619:
        return True    
            #Circle Object
    elif ((x-90)**2 + (y-70)**2)<(35**2):
        return True
            #Ellipse Object
    elif(((x-246)**2)/60**2 +((y-145)**2)/30**2 <= 1):
        return True
    elif y-x>=-265 and y+x>=391 and y-x<=-180.22 and y+0.98*x<=464.237:
        return True
    elif x<=381.4 and y-171.4<=0 and y-1.21*x<=-293.51 and y-x>=-265 and x>=328:# and y+0.25*x<=224.95
        return True
    elif (x>=200 and x<=230) and (y>=230 and y<=280):    
        if (x>=200 and x<=210 and y>=240 and y<=270):
            return True    
        elif (y>=270 and y<=280 and x>=210 and x<=230):
            return True
        elif (y>=230 and y<=240 and x>=210 and x<=240):
            return True
        elif (x<=210 and y<=240):
            return True
        elif (x<=210 and y>=270 and y<=280):
            return True
    else:
        return False
                    
getobstaclespace()
    
x1=int(input('Enter x coordinate of start node'))
y1=int(input('Enter y coordinate of start node'))
s = [x1,y1]
x2=int(input('Enter x coordinate of goal node'))
y2=int(input('Enter y coordinate of goal node'))
g = [x2,y2]               
#s=[1,1]                     #Start Position Test Case 1
#g=[399,299]                 #Goal Position Test Case 1
#s=[30,30]                  #Start Position Test Case 2
#g=[230,250]                #Goal Position Test Case 2
xmax=400                    #Width of the image
ymax=300                    #Height of the image
start_time = time.time()    #Program start time
visited_nodes = []          #List consisting of all the nodes traversed by the point robot
parent_node = []            #Open list to which the possible new child nodes would be appended to
parent_node.append(s)       #Appending inital state
child_node = []             #stores the child states after point robot moves to different positions
path_track={}               #Dictionary storing the values of the different states to backtrack the path followed
print(s)                    
print(g)
flag = 'n'                  #Flag to verify if the goal state is reached
visited_nodes.append(s)     #Appending the inital state to the list of visited nodes
visited = set([])           #Set consisting of the visited states. Using this because checking if a node is present in a list increases computation time
visited.add(str(s))         #Appending start node to the set
solvable=True
j=0


if s == g: #Checking if goal node is the same as the start node
    print('goal already reached')

if s in oblist or g in oblist: #checking if the goal or start node is in the obstacspace
    print('Starting or goal node in obstacle space')
    solvable=False             #Setting the flag to false in this case

if (s[0] <0 or s[0]> xmax) or (s[1]<0 or s[1] > ymax) or (g[0] <0 or g[0]> xmax) or (g[1]<0 or g[1] > ymax): #Checking if the start and goal node is within the grid(400x300)
    print('start/goal < 0 or greater than grid size')

if solvable:
    print('solvable')
    #traversing through each node in the open list
    for a in parent_node:
        #Calling the functions to obtain the blank tile(0) and validate if the tile can move in the different directions
        #print('in for loop')
        print(j)
        l_child,stat = ActionMoveLeft(a)
        u_child,stat = ActionMoveUp(a)
        r_child,stat = ActionMoveRight(a)
        d_child,stat = ActionMoveDown(a)
        ul_child,stat = ActionMoveUL(a)
        ur_child,stat = ActionMoveUR(a)
        dl_child,stat = ActionMoveDL(a)
        dr_child,stat = ActionMoveDR(a)
     
        #Inititalizing the dictionary with spaces to append subsequent nodes
        path_track[str(a)] = []                            

        #Checking if the child nodes are visited or not, if they lie within the resolution specified and if present in the obstacle space
        if (obstaclecheck(l_child) != True) and (str(l_child) not in visited) and (l_child[0]>0 and l_child[0]<xmax) and (l_child[1]>0 and l_child[1]<ymax):
            #print('l',l_child)
            visited.add(str(l_child))
            visited_nodes.append(l_child)
            parent_node.append(l_child)
            path_track[str(a)].append(l_child)
        if (obstaclecheck(r_child)!=True) and (str(r_child) not in visited) and (r_child[0]>0 and r_child[0]<xmax) and (r_child[1]>0 and r_child[1]<ymax) :
            #print('r',r_child)
            visited.add(str(r_child))
            visited_nodes.append(r_child)
            parent_node.append(r_child)
            path_track[str(a)].append(r_child)
        if (obstaclecheck(u_child)!=True) and (str(u_child) not in visited) and (u_child[0]>0 and u_child[0]<xmax) and (u_child[1]>0 and u_child[1]<ymax) :
            #print('u',u_child)
            visited.add(str(u_child))
            visited_nodes.append(u_child)
            parent_node.append(u_child)
            path_track[str(a)].append(u_child)
        if (obstaclecheck(ul_child)!=True) and (str(ul_child) not in visited) and (ul_child[0]>0 and ul_child[0]<xmax) and (ul_child[1]>0 and ul_child[1]<ymax) :
            #print('ul',ul_child)
            visited.add(str(ul_child))
            visited_nodes.append(ul_child)
            parent_node.append(ul_child)
            path_track[str(a)].append(ul_child)
        if (obstaclecheck(dl_child)!=True) and (str(dl_child) not in visited) and (dl_child[0]>0 and dl_child[0]<xmax) and (dl_child[1]>0 and dl_child[1]<ymax) :
            #print('dl',dl_child)
            visited.add(str(dl_child))
            visited_nodes.append(dl_child)
            parent_node.append(dl_child)
            path_track[str(a)].append(dl_child)
        if (obstaclecheck(ur_child)!=True) and (str(ur_child) not in visited) and (ur_child[0]>0 and ur_child[0]<xmax) and (ur_child[1]>0 and ur_child[1]<ymax) :
            #print('ur',ur_child)
            visited.add(str(ur_child))
            visited_nodes.append(ur_child)
            parent_node.append(ur_child)
            path_track[str(a)].append(ur_child)
        if (obstaclecheck(dr_child)!=True) and (str(dr_child) not in visited) and (dr_child[0]>0 and dr_child[0]<xmax) and (dr_child[1]>0 and dr_child[1]<ymax) :
            #print('dr',dr_child)
            visited.add(str(dr_child))
            visited_nodes.append(dr_child)
            parent_node.append(dr_child)
            path_track[str(a)].append(dr_child)
        if (obstaclecheck(d_child)!=True) and (str(d_child) not in visited) and (d_child[0]>0 and d_child[0]<xmax) and (d_child[1]>0 and d_child[1]<ymax) :
            #print('down',d_child)
            visited.add(str(d_child))
            visited_nodes.append(d_child)
            parent_node.append(d_child)
            path_track[str(a)].append(d_child)


        #Verifying if the goal state is reached
        for x in visited_nodes:
            #print('xgoal',x)
            if x == g:
                print('xgoal',x)
                flag='F'
                break    
                
        #Break out of the loop if goal is reached
        if flag=='F':
            print('goal reached')
            break
        j+=1
   
    
print(time.time()-start_time) #Time taken to reach the goal state
#Backtracking to find the paths traversed from the initial state to the final state
final_state = g
val = g
goal = s
path_track_list=[]
while val!=goal:
    for key, values in path_track.items():
        while val in values:
            key= ast.literal_eval(key) #converting strings of lists to pure lists
            val = key
            path_track_list.append(val)
path_track_list=path_track_list[::-1]
path_track_list.append(final_state) 

# File nodePath.txt to write all the nodes traversed from start to goal
F = open('nodePath10.txt', 'w')
# List of numbers
for c in visited_nodes:
    for i in c:
        F.write(str(i)+' ')
    F.write('\n')
# Close the file
F.close()

path_track_list=path_track_list[::-1]
# File nodePath.txt to backtrack the paths followed from goal to start
F = open('nodetrack10.txt', 'w')
# List of numbers
for c in path_track_list:
    for i in c:
        F.write(str(i)+' ')
    F.write('\n')
# Close the file
F.close()


#Printing the total time taken after backtracking
print("total time:")
print(time.time()-start_time)

#flipping the image axis to use for the animation
img=cv2.flip(img, 0)

#Creating an animation using pygame
pygame.init()

display_width = 400
display_height = 300

gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.SCALED)
pygame.display.set_caption('Animation BFS')

black = (0,0,0)      #Color represnting the background of image
white = (0,255,255)  #Color respresenting the visited nodes
yellow=(255,255,0)   #Color representing the obstacles

i=0
surf = pygame.surfarray.make_surface(img)

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True   
       
    gameDisplay.fill(black)

    #Setting the obstacle space in the animation
    for path in oblist:
            x = path[0]
            y = abs(300-path[1])
            pygame.draw.rect(gameDisplay, yellow, [x,y,1,1])
            
   #Visualizing the visited states in the animation
    for path in visited_nodes:
            x = path[0]
            y = abs(300-path[1])
            pygame.display.flip()
            pygame.draw.rect(gameDisplay, white, [x,y,1,1])
            #pygame.image.save(gameDisplay, f"/home/jayesh/Documents/ENPM661_PROJECT1/map/{i}.png")  #Saving the images to create a video 
            #i+=1                                                                                    #uncomment if not required
            
    #Visualizing the path taken from start to node
    for path in path_track_list:
        pygame.time.wait(10)
        #time.sleep(0.00005)
        x = path[0]
        y = abs(300-path[1])
        pygame.display.flip()
        pygame.draw.rect(gameDisplay, (255,5,5), [x,y,1,1])
        #pygame.image.save(gameDisplay, f"/home/jayesh/Documents/ENPM661_PROJECT1/map/{i}.png")     #Saving the images to create a video
        #i+=1                                                                                       #uncomment if not required
        pygame.time.wait(10)
        
    done = True
    
pygame.quit()

#Writing to video. Uncomment if required
'''
size=(400,300)
out = cv2.VideoWriter('p2bfs.avi',cv2.VideoWriter_fourcc(*'DIVX'), 800, size)
file_list=os.listdir('/home/jayesh/Documents/ENPM661_PROJECT1/map')

new_list=[]

for file in file_list:
    #print(file)
    a=file.split('.')[0]
    #print(a)
    new_list.append(a)
      
#print(new_list)

for i in range(0,len(new_list)):
    filename=f'/home/jayesh/Documents/ENPM661_PROJECT1/map/{i}.png'
    #print(filename)
    j+=1 
    #print(filename)
    img = cv2.imread(filename)
    out.write(img)
#cv2.imshow('obstacle',img)

out.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

  
