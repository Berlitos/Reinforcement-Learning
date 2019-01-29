##### IMPORTATION DES LIBRAIRIES #####
import numpy as np
import sys
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Input, concatenate
from keras.optimizers import Adam 
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import BoltzmannQPolicy
from rl.random import OrnsteinUhlenbeckProcess 
from keras.optimizers import RMSprop
import argparse
import gym


##### RECUPERATION DES PARAMETRES #####
parser = argparse.ArgumentParser(description='Train or test neural net motor controller')
parser.add_argument('--train', dest='train', action='store_true', default=True)
parser.add_argument('--test', dest='train', action='store_false', default=True)
parser.add_argument('--steps', dest='steps', action='store', default=50000, type=int)
parser.add_argument('--visualize', dest='visualize', action='store_true', default=False)
parser.add_argument('--model', dest='model', action='store', default="CartPole0.h5f")
args = parser.parse_args()


##### INITIALISATION DES CONSTANTES #####
## Model ##
SIZE_HIDDEN_LAYER_MODEL = 16
LR_MODEL = 0.001
TARGET_MODEL_UPDATE = 0.01
BATCH_SIZE = 64
REPLAY_BUFFER_SIZE = 100000

## Exploration ##
POLICY = BoltzmannQPolicy()

params = [SIZE_HIDDEN_LAYER_MODEL, LR_MODEL, TARGET_MODEL_UPDATE, BATCH_SIZE, REPLAY_BUFFER_SIZE]

## Simulation ##
N_STEPS_TRAIN = 50000
N_EPISODE_TEST = 10
VERBOSE = 1
# 0: pas de descriptif
# 1: descriptif toutes les LOG_INTERVAL steps
# 2: descriptif à chaque épisode
LOG_INTERVAL = 5000

## Save ##
FILE_PLOT_REWARD = args.model + '.png'
FILES_WEIGHTS_NETWORKS = './weights/' + args.model + '.h5f'

# Load environment
env = gym.make('CartPole-v0')
env.reset()

# Get the total number of step for training
nallsteps = args.steps

# Get Spaces
nb_actions = env.action_space.n
state_size = env.observation_space.shape

# Create network for DQN
model = Sequential()
model.add(Flatten(input_shape=(1,) + state_size))
model.add(Dense(24))
model.add(Activation('relu'))
model.add(Dense(24))
model.add(Activation('relu'))
model.add(Dense(24))
model.add(Activation('relu'))
model.add(Dense(24))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))


# Set up the agent for training
memory = SequentialMemory(limit=REPLAY_BUFFER_SIZE, window_length=1)
agent = DQNAgent(model = model, policy = POLICY, 
                memory= memory, nb_actions = nb_actions, 
                target_model_update=TARGET_MODEL_UPDATE)

# Create the model based on the information above
agent.compile(Adam(lr=LR_MODEL), metrics=['mae'])

# IF train arg :
if args.train:
    history = agent.fit(env, nb_steps=nallsteps, visualize=False, verbose=2, nb_max_episode_steps=env._max_episode_steps, log_interval=1000)
    agent.save_weights(args.model, overwrite=True)
    save_plot_reward(history, FILE_PLOT_REWARD, params) 


# IF test arg : 
if not args.train :
    agent.load_weights(args.model)
    agent.test(env, nb_episodes=10, visualize=True, nb_max_episode_steps=500)
