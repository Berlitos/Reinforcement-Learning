import sys
sys.path.append('../util')
from check_files import check


'''
Ce fichier sert à initialiser les paramètres de notre algorithme
'''

ENV = "MountainCar-v0"


## Model ##
SIZE_HIDDEN_LAYER = 50
LR_MODEL = 0.01
TARGET_MODEL_UPDATE = 0.001
ACTIVATION_OUTPUT = 'linear'
METRICS = 'mae'
BATCH_SIZE = 64
REPLAY_BUFFER_SIZE = 100000


## Simulation ##
SEED = 123
N_STEPS_TRAIN = 10000000
N_EPISODE_TEST = 100
VERBOSE = 1
'''
0: pas de descriptif
1: descriptif toutes les LOG_INTERVAL steps
2: descriptif à chaque épisode
'''
LOG_INTERVAL = 10000


## Check before running main ##
check('DQN', ENV)


PARAMS = [SIZE_HIDDEN_LAYER, ACTIVATION_OUTPUT, LR_MODEL, TARGET_MODEL_UPDATE, BATCH_SIZE, METRICS, SEED]
