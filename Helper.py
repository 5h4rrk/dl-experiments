import zipfile
import os , time
import numpy as np 
import random as rd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt 


class Helper:
    '''
    Args :
    --------------------------------------------------------
        takes a link as an input
    --------------------------------------------------------
    Output:
        preprocess the data (download & extraction)
    '''
    def __init__(this, link):
        this.file = None
        this.link = link
        this.download_extract()
        this.view_data()
        this.extract_classnames()
        
        
    def download_extract(this):
        this.before = [i for i in os.listdir(".")]
        print(os.popen(f"wget {this.link}").readlines())
        this.after = [i for i in os.listdir(".")]
        for i in this.after:
            if i not in this.before:
                this.file = i 
        this.dir = this.file.split(".")[0]
        r = zipfile.ZipFile(f"{this.file}")
        r.extractall()
        r.close()
    
    def view_random_train_image(this):
        _path = this.dir + "/train/"
        file_names = [ _ for _ in os.listdir(_path)]
        choices = [ rd.randint(0, len(file_names) - 1 ) for _ in range((4))] 
        indx = 0
        plt.figure(figsize=(12,6))
        for _ in range(4):
              plt.subplot(1 , 4, _ + 1)
              indx = choices[_]
              file_names_ = [i for i in os.listdir(_path +f"{file_names[ indx ]}/")]
              choices_ = rd.randint(0, len(file_names_) - 1 )
              plt.title(f"{file_names[indx]}/" + file_names_[indx], fontsize=10)
              img = mpimg.imread(_path + f"{file_names[indx]}/" + file_names_[choices_])
              plt.imshow(img/255.)
                
    def view_random_test_image(this):
        _path = this.dir + "/test/"
        file_names = [ _ for _ in os.listdir(_path)]
        choices = [ rd.randint(0, len(file_names) - 1 ) for _ in range((4))] 
        indx = 0
        plt.figure(figsize=(12,6))
        for _ in range(4):
              plt.subplot(1 , 4, _ + 1)
              indx = choices[_]
              file_names_ = [i for i in os.listdir(_path +f"{file_names[ indx ]}/")]
              choices_ = rd.randint(0, len(file_names_) - 1 )
              plt.title(f"{file_names[indx]}/" + file_names_[indx], fontsize=10)
              img = mpimg.imread(_path + f"{file_names[indx]}/" + file_names_[choices_])
              plt.imshow(img/255.)

    def get_classnames(this):
        return np.array(this.class_names)

    def view_data(this):
        for path, dirs , filenames in os.walk(this.dir):
            print(f"{len(dirs)} -- {len(filenames)} at {path}")

    def extract_classnames(this):
        '''
        Navigates through each directory and extract the class names
        '''
        temp = [ i for i in os.listdir(this.dir)]
        path_ = this.dir + "/" + temp[0]
        this.class_names = np.array(sorted([ j for j in os.listdir(path_)]))

  