##### IMPORTATION DES LIBRAIRIES #####
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Input
from keras.optimizers import Adam 
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import BoltzmannQPolicy
from rl.random import OrnsteinUhlenbeckProcess 
import argparse
import gym
import sys
import params 
sys.path.append('../util')
from check_files import check_overwrite
from save_train_test import save_plot_reward, save_result


##### RECUPERATION DES PARAMETRES #####
parser = argparse.ArgumentParser(description='Train or test agent')
parser.add_argument('--train', dest='train', action='store_true', default=True)
parser.add_argument('--test', dest='train', action='store_false', default=True)
parser.add_argument('--visualize', dest='visualize', action='store_true', default=False)
parser.add_argument('--model', dest='model', action='store', default="default")
args = parser.parse_args()


## Save ##
WEIGHTS_FILES = params.ENV + '/weights/' + args.model + '.h5f'


## Load environment ##
env = gym.make(params.ENV) 
env.seed(params.SEED)  # for comparison
env.reset()


## Examine the action space ##
action_size = env.action_space.n
print('Size of each action:', action_size)

## Examine the state space ##
state_size = env.observation_space.shape
print('Size of state:', state_size)


## Create network for DQN ##
model = Sequential()
model.add(Flatten(input_shape=(1,) + state_size))
model.add(Dense(params.SIZE_HIDDEN_LAYER,  activation = 'relu'))
model.add(Dense(params.SIZE_HIDDEN_LAYER,  activation = 'relu'))
model.add(Dense(params.SIZE_HIDDEN_LAYER,  activation = 'relu'))
model.add(Dense(action_size))
model.add(Activation(params.ACTIVATION_OUTPUT))


## Set up the agent for training ##
memory = SequentialMemory(limit=params.REPLAY_BUFFER_SIZE, window_length=1)
agent = DQNAgent(model = model, policy = BoltzmannQPolicy(), 
                memory= memory, nb_actions = action_size)

agent.compile(Adam(lr=params.LR_MODEL), metrics=[params.METRICS])


## Train ##
if args.train:
    check_overwrite('DQN', params.ENV, args.model)
    history = agent.fit(env, nb_steps=params.N_STEPS_TRAIN, visualize=args.visualize, verbose=1, nb_max_episode_steps=env._max_episode_steps, log_interval=params.LOG_INTERVAL)
    agent.save_weights(WEIGHTS_FILES, overwrite=True)
    save_plot_reward('DQN', params.ENV, history, args.model, params.PARAMS)


## Test ##
if not args.train :
    agent.load_weights(WEIGHTS_FILES)
    history = agent.test(env, nb_episodes=params.N_EPISODE_TEST, visualize=args.visualize, nb_max_episode_steps=env._max_episode_steps)
    save_result('DQN', params.ENV, history, args.model, params.PARAMS)
