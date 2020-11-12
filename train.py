import gym

# setting up environment
env = gym.make('BipedalWalker-v3')
env.reset()

# get env information
print(env.action_space)
print(env.observation_space)


# done
env.close()