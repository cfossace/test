#!/usr/bin/python
import os
import time
#Read in the path with user input (or navigate to the directory in the GUI)
#path = '/home/wildcat/Lockheed/laikaboss/malware/' 
os.chdir("/home/wildcat/Lockheed/laikaboss")
#print("Hint: /home/wildcat/Lockheed/laikaboss/malware/")
#path = raw_input("Enter the path of your file: ")
#if the path doesn't work, throw an error
#assert os.path.exists(path), "I did not find the file at, "+str(path)
#Start the laikaboss server in the background, in a docker container
#os.system("gnome-terminal")
#os.spawnl(os.P_DETACH,'sudo docker run --rm -it -v ~/laikaboss-workdir:/home/nonroot/workdir wzod/laikaboss')
#os.system("sudo docker run --rm -it -v ~/laikaboss-workdir:/home/nonroot/workdir wzod/laikaboss")
os.system("sudo docker run --name CONTAINER -d -it -p 5558:5558 -v ~/laikaboss-workdir:/home/nonroot/workdir wzod/laikaboss")
time.sleep(5)
os.system("sudo docker exec -d CONTAINER ./laikad.py")
#os.system("./laikad.py")
#For every file in the directory, start a container, 
#save the file into the container, and run the laika.py script
#for f in os.listdir(path):
 #       os.system("sudo docker run --rm -it -v ~/Lockheed:/home/nonroot/workdir wzod/laikaboss")

#sudo docker exec -d 904a7ff733f1 ./laikad.py

	#os.system("./laika.py {}".format(os.path.join(path,f))
