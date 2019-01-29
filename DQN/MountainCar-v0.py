# Derived from keras-rl
import numpy as np
import sys

from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Input, concatenate
from keras.optimizers import Adam 

from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import BoltzmannQPolicy, GreedyQPolicy, LinearAnnealedPolicy
from rl.random import OrnsteinUhlenbeckProcess 

from keras.optimizers import RMSprop
import argparse
import gym


# Command line parameters
parser = argparse.ArgumentParser(description='Train or test neural net motor controller')
parser.add_argument('--train', dest='train', action='store_true', default=True)
parser.add_argument('--test', dest='train', action='store_false', default=True)
parser.add_argument('--steps', dest='steps', action='store', default=50000, type=int)
parser.add_argument('--visualize', dest='visualize', action='store_true', default=False)
parser.add_argument('--model', dest='model', action='store', default="MountainCar.h5f")
args = parser.parse_args()

# Load environment
env = gym.make('MountainCar-v0')
env.reset()

# Get the total number of step for training
nallsteps = args.steps

# Get Spaces
nb_actions = env.action_space.n
state_size = env.observation_space.shape

print(nb_actions)
print(state_size)

# Create network for DQN
model = Sequential()
model.add(Flatten(input_shape=(1,) + state_size))
model.add(Dense(24))
model.add(Activation('relu'))
model.add(Dense(24))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))


# Set up the agent for training
memory = SequentialMemory(limit=100000, window_length=1)
policy = GreedyQPolicy()
agent = DQNAgent(model = model, policy = policy, 
                memory= memory, nb_actions = nb_actions, 
                target_model_update=1e-3)

# Create the model based on the information above
agent.compile(Adam(lr=1e-2), metrics=['mae'])

# IF train arg :
if args.train:
    agent.fit(env, nb_steps=nallsteps, visualize=args.visualize, verbose=2, nb_max_episode_steps=env._max_episode_steps, log_interval=1000)
    # After training is done, we save the final weights.
    agent.save_weights(args.model, overwrite=True)


# IF test arg : 
if not args.train :
    agent.load_weights(args.model)
    agent.test(env, nb_episodes=10, visualize=args.visualize, nb_max_episode_steps=500)
