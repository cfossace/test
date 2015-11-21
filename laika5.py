#!/usr/bin/python
import os

#Read in the path with user input (or navigate to the directory in the GUI)
#path = '/home/wildcat/Lockheed/laikaboss/malware/' 

path = raw_input("Enter the path of your file: ")

#if the path doesn't work, throw an error
assert os.path.exists(path), "I did not find the file at, "+str(path)

#Start the laikaboss server in the background, in a docker container
os.system("sudo docker run --rm -it -v ~/Lockheed:/home/nonroot/workdir wzod/laikaboss/laika.py")
#For every file in the directory, start a container, 
#save the file into the container, and run the laika.py script
#for f in os.listdir(path):
 #       os.system("sudo docker run --rm -it -v ~/Lockheed:/home/nonroot/workdir wzod/laikaboss")
       
	

	#os.system("./laika.py {}".format(os.path.join(path,f)))
