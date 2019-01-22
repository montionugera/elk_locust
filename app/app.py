import json
import time
from logging.handlers import RotatingFileHandler

import os
from flask import Flask, request

app = Flask(__name__)
import random

Names = "Beatrix,Blaire,Callie,Cecily,Cleo,Coco,Cosette,Cybil,Daisy".split(",")
import logging
dir_path = os.path.dirname(os.path.realpath(__file__))
default_log_file_name = os.path.join(dir_path,'logs/default.log' )
logging.basicConfig(filename=default_log_file_name, level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')

api_log_file_name = os.path.join(dir_path,'logs/api.log' )

logger = logging.getLogger('api')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(api_log_file_name, maxBytes=2000000, backupCount=10)
formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s', datefmt='%d/%b/%Y:%H:%M:%S%z')
handler.setFormatter(formatter)
logger.addHandler(handler)


listener_log_file_name = os.path.join(dir_path,'logs/listener.log' )
logger_listener = logging.getLogger('listener')
handler = RotatingFileHandler(listener_log_file_name, maxBytes=2000000, backupCount=10)
handler.setFormatter(formatter)
logger_listener.setLevel(logging.DEBUG)
logger_listener.addHandler(handler)

@app.route('/')
def work():
    response = "work"
    time_usage = random.uniform(0.00001, 0.00002)
    time.sleep(time_usage)
    log_msg = f"/|{response}|{time_usage}"
    logger.info(log_msg)
    return "Work !"


@app.route('/api1')
def ptt():
    time_usage = random.uniform(0.02, 0.05)
    time.sleep(time_usage)
    response = random.choice(Names)
    log_msg = f"/api1|{response}|{time_usage}"
    logger.info(log_msg)
    return response


@app.route('/api2')
def scg():
    time_usage = random.uniform(0.3, 0.7)
    time.sleep(time_usage)
    response = random.choice(Names)
    log_msg = f"api2|{response}|{time_usage}"
    logger.info(log_msg)
    return response


@app.route('/api3')
def api3():
    response = random.choice(Names)
    time_usage = random.uniform(0.201, 1.44)
    time.sleep(time_usage)
    log_msg = f"api3|{response}|{time_usage}"
    logger.info(log_msg)
    return response


@app.route('/listen', methods=["POST"])
def listen():
    time_usage = random.uniform(0.201, 1.44)
    log_msg = f"listen|{request.data}|{time_usage}"
    logger_listener.info(log_msg)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="80")
