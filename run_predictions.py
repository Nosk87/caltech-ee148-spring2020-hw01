import os
import numpy as np
import json
from PIL import Image

def detect_red_light(I):
    '''
    This function takes a numpy array <I> and returns a list <bounding_boxes>.
    The list <bounding_boxes> should have one element for each red light in the 
    image. Each element of <bounding_boxes> should itself be a list, containing 
    four integers that specify a bounding box: the row and column index of the 
    top left corner and the row and column index of the bottom right corner (in
    that order). See the code below for an example.
    
    Note that PIL loads images in RGB order, so:
    I[:,:,0] is the red channel
    I[:,:,1] is the green channel
    I[:,:,2] is the blue channel
    '''
    
    
    bounding_boxes = [] # This should be a list of lists, each of length 4. See format example below. 
    match_list = []
    '''
    BEGIN YOUR CODE
    '''
    
    box_height = 8
    box_width = 6
    
    #print(I[:,:,0])
    
    for i in range(479):
        for j in range(479):
            if I[i,j,0] <= 255 and I[i,j,0] >= 250:
                if I[i,j,1] <= 220 and I[i,j,1] >= 175:
                    if I[i,j,2] <= 140 and I[i,j,2] >= 110:
                            bounding_boxes.append([i-box_height,j-box_width,i+box_height,j+box_width])
                            
    '''
    As an example, here's code that generates between 1 and 5 random boxes
    of fixed size and returns the results in the proper format.
   

    END YOUR CODE
     '''
    
    for i in range(len(bounding_boxes)):
        assert len(bounding_boxes[i]) == 4
    
    return bounding_boxes

# set the path to the downloaded data: 
data_path = r'C:\Users\space\Downloads\RedLights2011_Medium\RedLights2011_Medium'

# set a path for saving predictions: 
preds_path = r'C:\Users\space\Downloads\RedLights2011_Medium\data\hw01_preds' 
os.makedirs(preds_path,exist_ok=True) # create directory if needed 

# get sorted list of files: 
file_names = sorted(os.listdir(data_path)) 

# remove any non-JPEG files: 
file_names = [f for f in file_names if '.jpg' in f] 

preds = {}
for i in range(len(file_names)):
    
    # read image using PIL:
    I = Image.open(os.path.join(data_path,file_names[i]))
    
    # convert to numpy array:
    I = np.asarray(I)
    
    preds[file_names[i]] = detect_red_light(I)

# save preds (overwrites any previous predictions!)
with open(os.path.join(preds_path,'preds.json'),'w') as f:
    json.dump(preds,f)
