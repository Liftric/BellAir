from datetime import datetime, timedelta

list = [[], []]
button_counter = 0
signal = None
timeout_limit = 5

while signal != 0:
    signal = int(input("Please input a number: "))

    def appender(signal, button_counter):
        list[0].append(datetime.now())
        timer_start = datetime.now()

        while datetime.now() < timer_start + timedelta(seconds=timeout_limit):
            button = int(input("Chance to append with 1-4: "))
            button_counter += 1

            if button_counter == 1:

                if datetime.now() < timer_start + timedelta(seconds=timeout_limit):
                    list[1].append(button)

                else:
                    list[1].append(0)

                button_counter += 1

        button_counter = 0

        def printer():
            print("list len: ", len(list))
            for i in range(len(list)):
                print(list[i])

        printer()

    appender(signal, button_counter)

print("Done")
