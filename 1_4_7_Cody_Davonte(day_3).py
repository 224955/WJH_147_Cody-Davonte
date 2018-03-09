import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw      
import numpy as np      


def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    
def make_mask(original_image, wide, ):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    directory = os.getcwd()
    
    new_directory = os.path.jion(directory, 'Seom Seong-ji') 
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    image_list, file_list = get_images(directory)
    
    image = np.array(img)
    for n in range(len(image_list)):
        filename, filetype = os.oath.splitext(file_list[n])
        img = PIL.Image.open(file_list[n])
        
    width, height = original_image.size
    
    drawing_layer = PIL.ImageDraw.Draw(frame_mask) 
    thickness = int(wide * min(width,height)) #thickness in pixels  
    
    drawing_layer.rectangle((0,0,width,thickness), fill= (r, g, b, 255)),
    drawing_layer.rectangle((0,0, thickness,height), fill= (r, g, b, 255)), 
    
    img_filename= os.path.join(new_directory, filename + '.png')
    img.save(img_filename)

def logo1(original_image, logo, logo_size = .3):
    logo = PIL.Image.open(logo)
    original_image = PIL.Image.open(original_image)
    width, height = original_image.size
    position = int(logo_size * min(width, height)) 
    
    rlogo = logo.resize((position, position)) 
    
    directory = os.getcwd()
    
    new_directory = os.path.join(directory, 'Seom Seong-ji') 
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    
    result= original_image.copy()
    result= result.paste(rlogo, (0,0), rlogo) 
    img_filename= os.path.join(new_directory, "itDoesn'tMatterCole.png")
    result.save(img_filename)
    
    