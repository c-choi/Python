#stochastic = nondeterministic = inherent randomness
# slippery = True => Q does not work anymore (less usable than random selection)
# USE LEARNING RATE Alpha = listen to Q with 10% incliniation
# Convergence ?  => with enough trial convergence still occurs



import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('FrozenLake-v0')

# initialize with all zeros
Q = np.zeros([env.observation_space.n, env.action_space.n])

# Set learning params
learning_rate = .85
dis = .99
num_episodes = 2000

# create lists to contain total rewards and steps per episodes
rList = []
for i in range(num_episodes):
    # reset env and get first new observation
    state = env.reset()
    rAll = 0
    done = False

    # The Q-Table learning algorithm
    while not done:
        # choose an action by greedily (with noise) pciking from Q table
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) / (i + 1))

        # get new state and reward from environment
        new_state, reward, done, _ = env.step(action)

        # update Q-Table with new knowledge using learning rate
        # difference
        Q[state, action] = (1-learning_rate) * Q[state, action] \
            + learning_rate * (reward + dis * np.max(Q[new_state, :]))

        rAll += reward
        state = new_state

    rList.append(rAll)

print("Score over time: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print(Q)
plt.bar(range(len(rList)), rList, color="blue")
plt.show()
