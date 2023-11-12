import glob, os
import subprocess as sbp
import os
import subprocess

path1 = '/home/ssauto/Label/videos/video_1_mp4/*.jpg'
path2 = '/home/ssauto/Label/videos/video_2_mp4/*.jpg'


path_txt = '/home/ssauto/Label/output/YOLO/*.txt'


## where to place the merged data
merged_path = '/home/ssauto/Label/data/'  # /home/ssauto/Datasets/

## write an rsync commands to merge the directories
rsync_cmd = 'rsync' + ' -avzh ' + path1 + ' '+ path2 +' '+ path_txt + ' ' + merged_path



## run the rsync command
subprocess.run(rsync_cmd, shell=True) 


print("---------------Done---------------------------")



'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

dataset_path = '/home/ssauto/VISION-GUI/darknet/damage_cam2'                # '/home/ssauto/VISION-GUI/darknet/Datasets/Datasets'    

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('/home/ssauto/VISION-GUI/darknet/damage_cam2/train.txt', 'w')  
file_test = open('/home/ssauto/VISION-GUI/darknet/damage_cam2/test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  

index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test+1:
        counter = 1
        file_test.write(dataset_path + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(dataset_path + "/" + title + '.jpg' + "\n")
        counter = counter + 1




#-------------------------------------------------------------------------------------------------------------------------------------------------

os.system("python3 /home/ssauto/VISION-GUI/darknet/damage_cam2/file.py")          #  /home/ssauto/VISION-GUI/darknet/Datasets/file.py


print("--------------------------------")
print("---------------CFG File Done---------------")
print("\n")
print("\n")


'''


'''
fol = os.listdir(path)
p2 = raw_input('Please enter a path\n')

for i in fol:
    p1 = os.path.join(path,i)
    p3 = 'cp -r ' + p1 +' ' + p2+'/.'
    sbp.Popen(p3,shell=True)

'''
