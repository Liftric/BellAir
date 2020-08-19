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
doorbell_identifier = 11249698
last_signal_match = None
timer_before_message = None  # brauch ich das?
timer_after_message = None  # brauch ich das?

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

        # full signal: -p 475 -t 1 11249698
        doorbell_match = doorbell_identifier == rfdevice.rx_code
        if doorbell_match:
            print("*** Received door signal ***")

            if last_signal_match != None and datetime.now() < last_signal_match + timedelta(
                seconds=5
            ):
                print("--> Backoff (5s)")
            else:
                print("--> Processing signal")
                last_signal_match = datetime.now()
                timer_before_message = last_signal_match

                import msg_ms
                import msg_slack

                # msg_ms.send()
                msg_slack.send()

                timer_after_message = datetime.now()

                # make 2x list to add button (e.g. 0-3)
                timestamp_total.append(timer_before_message)
                print(
                    "Ring {}: {}".format(
                        len(timestamp_total), timestamp_total[len(timestamp_total) - 1],
                    )
                )
        else:
            print("*** Not door signal ***")

    time.sleep(0.01)
rfdevice.cleanup()
