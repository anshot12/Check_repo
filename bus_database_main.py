import itertools
import json
import re


class DataBase:
    def __init__(self, text):
        self.data = text
        self.dictionary = {}
        self.dictionary_errors = {}
        self.dictionary_bus_line_info = {}
        self.dictionary_start_stop = {}
        self.dictionary_time = {}
        self.dictionary_on_demand = {}

    def str_errors(self, key, value):
        if key == "stop_name":
            self.check_stop_name(value)
        elif key == "stop_type":
            self.check_stop_type(value),
        elif key == "a_time":
            self.check_a_time(value)

    def convert(self):
        self.dictionary = json.loads(self.data)
        return self.dictionary

    def format_dict(self):
        self.convert()
        for field in self.dictionary:
            for key in field.keys():
                self.dictionary_errors.setdefault(key, 0)
            return self.dictionary_errors

    def check_int(self):
        for field in self.dictionary:
            for key, value in field.items():
                if (key == "bus_id" or key == "stop_id" or key == "next_stop") and type(value) != int:
                    self.dictionary_errors[key] += 1
        return self.dictionary_errors

    def check_str(self):
        for field in self.dictionary:
            for key, value in field.items():
                if key == "stop_name" or key == "stop_type" or key == "a_time":
                    if type(value) != str:
                        self.dictionary_errors[key] += 1
                    else:
                        self.str_errors(key, value)

    def check_stop_name(self, value):
        pattern = re.compile(r"([A-Z][\w\d\s]+)+ (Road|Avenue|Boulevard|Street)(?!.+)")
        if pattern.match(value) is None:
            self.dictionary_errors["stop_name"] += 1

    def check_stop_type(self, value):
        if value == "":
            self.dictionary_errors["stop_type"] += 0
        else:
            pattern = re.compile(r"(S)|(O)|(F)")
            if pattern.match(value) is None or len(value) > 1:
                self.dictionary_errors["stop_type"] += 1

    def check_a_time(self, value):
        pattern = re.compile(r"(\d{2}):(\d{2})(?!.+)")
        if pattern.match(value) is None:
            self.dictionary_errors["a_time"] += 1
        else:
            hours = pattern.match(value).group(1)
            minute = pattern.match(value).group(2)
            if int(hours[0]) >= 2 or int(minute) >= 60 or (int(hours) < 10 and hours[0] != "0"):
                self.dictionary_errors["a_time"] += 1

    def output_format_errors(self):
        lst = ["stop_name", "stop_type", "a_time"]
        summa = 0
        for key, value in self.dictionary_errors.items():
            if key in lst:
                summa += value
        print(f"Format validation: {summa} errors")

    def output_each_format_error(self):
        lst = ["stop_name", "stop_type", "a_time"]
        for key, value in self.dictionary_errors.items():
            if key in lst:
                print(f"{key}: {value}")

    def bus_line_info(self):
        for field in self.dictionary:
            for key in field:
                if key == "bus_id":
                    self.dictionary_bus_line_info.setdefault(field[key], []).append(field["stop_id"])

    def output_bus_line_info(self):
        print("Line names and number of stops:")
        for key, value in self.dictionary_bus_line_info.items():
            print(f"bus_id: {key}, stops: {len(value)}")

    def start_stop_check(self):
        for field in self.dictionary:
            for key in field:
                if key == "bus_id":
                    self.dictionary_start_stop.setdefault(field[key], []).append((field["stop_id"],
                                                                                  field["stop_type"],
                                                                                  field["stop_name"]))

    def start_stop_check_output(self):
        start_stop = []
        transfer_stop = {}
        transfer_stop_lst = []
        finish_stop = []
        for bus_line, stops in self.dictionary_start_stop.items():
            if stops[0][1] != "S" or stops[-1][1] != "F":
                print(f"There is no start or end stop for the line {bus_line}.")
            else:
                for i in range(len(stops)):
                    transfer_stop.setdefault(stops[i][2], 0)
                    transfer_stop[stops[i][2]] += 1
                    if stops[i][1] == "S":
                        start_stop.append(stops[i][2])
                    elif stops[i][1] == "F":
                        finish_stop.append(stops[i][2])
                for key, value in transfer_stop.items():
                    if value > 1:
                        transfer_stop_lst.append(key)
        print(f"Start stops: {len(set(start_stop))} {sorted(set(start_stop))}\n"
              f"Transfer stops: {len(set(transfer_stop_lst))} {sorted(set(transfer_stop_lst))}\n"
              f"Finish stops: {len(set(finish_stop))} {sorted(set(finish_stop))}")

    def time_check(self):
        for field in self.dictionary:
            for key in field:
                if key == "bus_id":
                    self.dictionary_time.setdefault(field[key], []).append((field["stop_name"],
                                                                            field["a_time"]))

    def time_check_output(self):
        lst_time = {}
        time_errors = 0
        for bus_id, time in self.dictionary_time.items():
            for stop in time:
                pattern = re.compile(r"(\d{2}):(\d{2})")
                hour = pattern.match(stop[1]).group(1)
                minute = pattern.match(stop[1]).group(2)
                lst_time.setdefault(bus_id, [])
                lst_time[bus_id].append((int(hour), int(minute), stop[0]))
        print("Arrival time test:")
        for key, time_check in lst_time.items():
            for i in range(len(time_check) - 1):
                if time_check[i][0] >= time_check[i+1][0] and time_check[i][1] >= time_check[i+1][1]:
                    print(f"bus_id line {key}: wrong time on station {time_check[i+1][2]}")
                    time_errors += 1
                    break
                else:
                    time_errors += 0
        if time_errors == 0:
            print("OK")

    def on_demand(self):
        for field in self.dictionary:
            for key in field:
                if key == "bus_id":
                    self.dictionary_on_demand.setdefault(field["stop_name"], []).append(field["stop_type"])

    def on_demand_output(self):
        wrong_stop_type = []
        for key, value in self.dictionary_on_demand.items():
            if len(value) > 1 and "O" in value:
                wrong_stop_type.append(key)
        if len(wrong_stop_type) == 0:
            print("On demand stops test:\nOK")
        else:
            print(f"On demand stops test:\nWrong stop type: {sorted(wrong_stop_type)}")


text_str = DataBase(input())
text_str.convert()
text_str.on_demand()
text_str.on_demand_output()
