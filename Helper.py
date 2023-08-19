import zipfile
import os 

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
        this.link = link
        this.download_extract()
        this.view_data()
        
    def download_extract(this):
        this.before = [i for i in os.listdir(".")]
        os.system(f"!wget {this.link}")
        this.after = [i for i in os.listdir(".")]
        for i in this.after:
            if i not in this.before:
                this.file = i 
        this.dir = this.file.split(".")[0]
        r = zipfile.ZipFile(f"{this.file}")
        r.extractall()
        r.close()


    def view_data(this):
        for path, dirs , filenames in os.walk(this.dir):
            print(f"{len(dirs)} -- {len(filenames)} at {path}")

