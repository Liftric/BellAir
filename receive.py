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

timestamp_total = []
signal_counter = 1
timer = datetime.now() - timedelta(seconds=10)
program_start = True  # just used so that the divider 'print("-" * 80)' doesn't appear at first program boot

while True:
    if rfdevice.rx_code_timestamp != timestamp:  # wat soll die Zeile?
        # reset 5s time (avoids spam when >1 signals received from door within 5s window)
        if datetime.now() >= timer + timedelta(seconds=5):  # reset
            signal_counter = 1

            if program_start == False:
                print("_" * 80)

            program_start = False

        # signal info
        timestamp = rfdevice.rx_code_timestamp
        logging.info(
            str(rfdevice.rx_code)
            + " [pulselength "
            + str(rfdevice.rx_pulselength)
            + ", protocol "
            + str(rfdevice.rx_proto)
            + "]"
        )

        # main loop if door signal (for testing case: door signal = 666)
        if rfdevice.rx_code == 666:
            print("signal #{}".format(signal_counter))

            # only send message to messaging services if it's the first signal
            if signal_counter == 1:
                timer = datetime.now()

                # import msg_ms
                # import msg_slack

                # msg_ms.send()
                # msg_slack.send()

                # save rings in a list for data analysis etc. --> add "who rang" to ring/list in post via buttons at door
                timestamp_total.append(datetime.now())

                for i in range(len(timestamp_total)):
                    print("Ring {}: {}".format(i + 1, timestamp_total[i]))
                print()

            signal_counter += 1

        print()

    time.sleep(0.01)
rfdevice.cleanup()
