import PIL
import os.path 
import PIL.ImageDraw
from PIL import Image

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

def paste_logo(image, percent_of_side):
    '''takes the image given, and the percent of the smallest side
    then pastes the image onto the image. The size is based on the
    percent of the smallest side
    '''
    
    #open the background image
    image = PIL.Image.open(image)
    
    width, height = image.size
    position = int(percent_of_side * min(width, height))

    
    #find the logo and open it
    logo = PIL.Image.open("/Users/231303/Desktop/CompSciPrin Files/Unit 1/1.4/1.4.7/Logo/logo.png")
    #resize the logo
    logo = logo.resize((position, position))
    
    #paste the logo onto the images
    image.paste(logo, (0, 0), logo)
    return image
    
def watermark_all_images(directory=None):
    '''grabs each image in the current working directory
    then runs the procedure paste_logo to paste the logo onto the images
    '''
    
    if directory == None:
        directory = os.getcwd()
        
    new_directory = os.path.join(directory, 'Seom Seong-ji')
    try:
        os.mkdir(new_directory) #make a directory
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)
    
    
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        #run the procedure paste_logo
        new_image = paste_logo(file_list[n], .4)
        print n
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
    