from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

max_duration = 5
cumulative_time = 0
beginning_time = datetime.now()

signal_time_and_length_list = [[], []]  # time, length
signal_length_list = []
signal_start = None

print("**Started recording**\n")

while cumulative_time < max_duration:
    signal_start = datetime.now()

    while GPIO.input(27) == 1:
        pass

    cumulative_time = (datetime.now() - beginning_time).seconds
    signal_time_and_length_list.extend([cumulative_time, datetime.now() - signal_start])
    signal_length_list.append(datetime.now() - signal_start)

print("\n**Ended recording**")

sum_11 = 0
sum_10 = 0
sum_09 = 0

for signal in signal_length_list:

    # if signal.total_seconds() > 0.000011:
    #     print(signal)

    if signal.total_seconds() == 0.000011:
        sum_11 += 1

    elif signal.total_seconds() == 0.000010:
        sum_10 += 1

    elif signal.total_seconds() < 0.000010:
        sum_09 += 1

    # if signal not in "0:00:00.000011" or "0:00:00.000010":
    #     print(signal)


# for time_and_signal in signal_time_and_length_list:
#     print(time_and_signal)

print("\nFound {} total signals".format(int(len(signal_time_and_length_list) / 2)))
print("\nFound {} total signals".format(len(signal_length_list)))
print(
    "\nFound {} signals of length == 0.000011s ({}%)".format(
        sum_11, sum_11 / len(signal_length_list) * 100
    )
)

print(
    "\nFound {} signals of length == 0.000010s ({}%)".format(
        sum_10, sum_10 / len(signal_length_list) * 100
    )
)

print(
    "\nFound {} signals of length <= 0.000009s ({}%)".format(
        sum_09, sum_09 / len(signal_length_list) * 100
    )
)

print()

GPIO.cleanup()
