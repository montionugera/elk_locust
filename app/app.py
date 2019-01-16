import time
from logging.handlers import RotatingFileHandler

from flask import Flask
app = Flask(__name__)
import random
Names = "Beatrix,Blaire,Callie,Cecily,Cleo,Coco,Cosette,Cybil,Daisy".split(",")
import logging

logging.basicConfig(filename='logs/default.log',level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger('api')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler("logs/api.log", maxBytes=2000000, backupCount=10)
formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s', datefmt='%d/%b/%Y:%H:%M:%S%z')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/')
def work():
    return "Work !"

@app.route('/api1')
def ptt():
    time_usage = random.uniform(0.02, 0.05)
    time.sleep(time_usage)
    response = random.choice(Names)
    log_msg = f"{response}|{time_usage}"
    logger.info(log_msg)
    return response

@app.route('/api2')
def scg():
    time_usage = random.uniform(0.3, 0.7)
    time.sleep(time_usage)
    response = random.choice(Names)
    log_msg = f"{response}|{time_usage}"
    logger.info(log_msg)
    return response

@app.route('/api3')
def api3():
    response = random.choice(Names)
    time_usage = random.uniform(0.201, 1.44)
    time.sleep(time_usage)
    log_msg = f"{response}|{time_usage}"
    logger.info(log_msg)
    return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port="80")

