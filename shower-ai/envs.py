import gym

from gym import Env 
from gym.spaces import Discrete, Box 

import numpy as np
import random

# Refrenece: https://www.youtube.com/watch?v=bD6V3rcr_54
class ShowerEnv(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        self.action_space = Discrete(3)
        # Temperature array
        self.observation_space = Box(low=np.array([0]), high=np.array([100]))
        # Set start temp
        self.state = 38 + random.randint(-3, 3)
        # Set shower length
        self.shower_length = 60

    def step(self, action):
        # Apply action
        # 0 - 1 = -1 temperature
        # 1 - 1 = 0
        # 2 - 1 = 1 temperature
        self.state += action - 1
        # Reduce shower length by 1 second
        self.shower_length -= 1

        # Calculate reward
        if self.state >=37 and self.state <=39:
            reward = 1
        else :
            reward = -1

        # Check if shower is done
        if self.shower_length <= 0:
            done = True
        else:
            done = False

        # Aplply temperature noise
        self.state += random.randint(-1, 1)

        # Set placeholder for info
        info = {}

        # return step information
        return self.state, reward, done, info

    def render(self):
        # Implement viz 
        pass

    def reset(self):
        # Reset shower temperature
        self.state = 38 + random.randint(-3, 3)
        # Reset shower time
        self.shower_length = 60
        
        return self.state