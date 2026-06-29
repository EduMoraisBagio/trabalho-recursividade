def inverter_string(s):
    if len(s) <= 1:
        return s

    return inverter_string(s[1:]) + s[0]


print(inverter_string("ufsc"))