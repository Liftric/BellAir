#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging
import requests

from rpi_rf import RFDevice
from datetime import datetime, timedelta

rfdevice = None

# pylint: disable=unused-argument
def exithandler(signal, frame):
    rfdevice.cleanup()
    sys.exit(0)


logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s",
)

parser = argparse.ArgumentParser(
    description="Receives a decimal code via a 433/315MHz GPIO device"
)
parser.add_argument(
    "-g", dest="gpio", type=int, default=27, help="GPIO pin (Default: 27)"
)
args = parser.parse_args()

signal.signal(signal.SIGINT, exithandler)
rfdevice = RFDevice(args.gpio)
rfdevice.enable_rx()
timestamp = None
logging.info("Listening for codes on GPIO " + str(args.gpio))

while True:
    if rfdevice.rx_code_timestamp != timestamp:  # wat soll die Zeile?
        print()
        timestamp = rfdevice.rx_code_timestamp
        logging.info(
            str(rfdevice.rx_code)
            + " [pulselength "
            + str(rfdevice.rx_pulselength)
            + ", protocol "
            + str(rfdevice.rx_proto)
            + "]"
        )

        requests.post(
            "http://192.168.1.121:8080/signal", json={"id": 1, "timestamp": "test"},
        )

    time.sleep(0.01)
rfdevice.cleanup()
