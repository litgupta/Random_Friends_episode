import os
import random
#Replace the below mentioned path with your absolute path to the FRIENDS folder
path='/Volumes/Lalit/tv series/Friends'

os.chdir(path)

#chosing random season
seasons=os.listdir(os.getcwd())
random_season=random.choice(seasons)

os.chdir(os.path.join(os.getcwd(),random_season))

#Choosing random episode
random_episode=random.choice(os.listdir(os.getcwd()))

#Voila ! enjoy 
os.system('open '+random_episode)

