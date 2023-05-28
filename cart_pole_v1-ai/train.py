import sys
assert sys.version_info >= (3, 5)

import sklearn
assert sklearn.__version__ >= "0.20"

import numpy as np
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation

import gym
import datetime

# 1. Modify deault configure value
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# 2. Make dirs
root_path = os.getcwd()
base_path = os.environ.get("BASE_PATH", '../data/')
data_path = os.path.join(base_path + 'lab13/')
result_path = "result"
image_path = "img"

# 3. Define save function
def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(result_path, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()

    plt.savefig(path, format=fig_extension, dpi=resolution)

# 4. List all gym envs
all_envs = gym.envs.registry.all()
env_ids = [env_spec.id for env_spec in all_envs]
print(env_ids)

# 4.8 Define visualization function
def plot_environment(env, figsize=(5, 4)):
    plt.figure(figsize=figsize)
    img = env.render(mode="rgb_array")
    plt.imshow(img)
    plt.axis("off")

    return img

# Create a basic policy
def basic_policy(obs):
    angle = obs[2]
    return 0 if angle < 0 else 1

# Display animation
def update_scene(num, frames, patch):
    patch.set_data(frames[num])
    return patch

def plot_animation(frames, repeat=False, interval=40):
    fig = plt.figure()
    patch = plt.imshow(frames[0])
    plt.axis("off")
    anim = animation.FuncAnimation(fig, update_scene, fargs=(frames, patch), frames=len(frames), repeat=repeat, interval=interval)
    plt.close()
    return anim

# Global variables
totals = []
start_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
record_path = "./record/train_" + start_time
os.makedirs(record_path, exist_ok=True)

# 4.3 Select env
env = gym.make('CartPole-v1')

# Play 500 times
for episode in range(1):
    # Rewards
    episode_rewards = 0

    # Reset environment
    obs = env.reset()

    # Record frames
    frames = []

    # Play 200 step in every episode
    for setp in range(2000):
        # Render
        img = env.render("rgb_array")
        frames.append(img)

        # Choose action with base policy
        action = basic_policy(obs)

        # Take action
        obs, reward, done, info = env.step(action)
        episode_rewards += reward

    totals.append(episode_rewards)

    # save frames
    anim_save_path = "{}/episode_{}.gif".format(record_path, episode)
    anim = plot_animation(frames)
    anim.save(anim_save_path, writer='imagemagick')

print(np.mean(totals), np.std(totals), np.min(totals), np.max(totals))