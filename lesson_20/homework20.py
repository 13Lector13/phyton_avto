from datetime import datetime


def analyze_heartbeat(input_file: str, output_file: str):
    key_value = "Key TSTFEED0300|7E3E|0400"
    timestamps = []

    with open(input_file, "r") as file:
        for line in file:
            if key_value in line:
                start_index = line.find("Timestamp ")
                if start_index != -1:
                    time_str = line[start_index + 10:start_index + 18]
                    time_obj = datetime.strptime(time_str, "%H:%M:%S")
                    timestamps.append(time_obj)

    with open(output_file, "w") as log_file:
        for i in range(len(timestamps) - 1):
            current_time = timestamps[i]
            next_time = timestamps[i + 1]

            heartbeat = abs((current_time - next_time).total_seconds())

            if 31 < heartbeat < 33:
                log_file.write(
                    f"WARNING: Heartbeat {heartbeat} sec at {next_time.strftime('%H:%M:%S')}\n"
                )
            elif heartbeat >= 33:
                log_file.write(
                    f"ERROR: Heartbeat {heartbeat} sec at {next_time.strftime('%H:%M:%S')}\n"
                )


analyze_heartbeat("hblog.txt", "hb_test.log")
