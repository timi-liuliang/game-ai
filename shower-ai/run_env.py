import envs

env = envs.ShowerEnv()
states = env.observation_space.shape
actions = env.action_space.n

episodes = 10
for episode in range(episodes):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        
        score += reward

    print("Episode:{} Score:{}".format(episode, score))

