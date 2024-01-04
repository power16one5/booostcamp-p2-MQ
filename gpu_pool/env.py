import os

CWD = os.getcwd()

MYSQL_SERVER_IP = '10.28.224.124'
MYSQL_SERVER_PORT = 30156
MYSQL_SERVER_USER = 'teemo'
MYSQL_SERVER_PASSWORD = 'teemo'

MESSAGE_FILE_PATH = './message.json'

# id, branch, train_path, pushed의 위치를 수정하지 마세요.
MESSAGE_COLUMNS = ['id', 'branch', 'train_path',
                   'name', 'seed', 'epoch', 'dataset', 'augmentation',
                   'criterion', 'batch_size',
                   'model', 'optimizer', 
                  'pushed']

# 이하 수정 x
ARGS_EXCEPTION = ['id', 'branch', 'train_path', 'pushed']
BRANCH_INDEX = 1
TRAIN_INDEX = 2