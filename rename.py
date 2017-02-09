import os, glob

def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        
        #uncomment to change from number based filenames
        #os.rename(pathAndFilename, os.path.join(dir, titlePattern % title + ext))
        
        if unicode(title).isnumeric():
            os.rename(pathAndFilename, 
                  os.path.join(dir, titlePattern % title + ext))