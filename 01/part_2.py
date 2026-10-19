
# https://systemscheck.dev/missions/1#part-2

MAX_TIME = 48986

input = []

def parse(string):
    global input

    parts = string.split(' ')
    time = int(parts[0].replace('t=', ''))
    reactor_id = int(parts[1].replace('#', ''))
    enable = parts[2] == 'enabled'

    input.append([time, reactor_id, enable])

def find_max_disabled(input) -> int:
    max_cells_disabled = 0
    disabled_reactors = set()

    for k, (time, reactor_id, enable) in enumerate(input):
        if enable:
            disabled_reactors.remove(reactor_id)
        else:
            disabled_reactors.add(reactor_id)

        is_last_at_time = k == len(input) - 1 or input[k + 1][0] != time
        if is_last_at_time and len(disabled_reactors) > max_cells_disabled:
            max_cells_disabled = len(disabled_reactors)

    return max_cells_disabled

def find_max_low_power_duration(input, max_cells_disabled) -> int:
    count = 0
    current_run = 0
    max_duration = 0
    disabled_reactors = set()
    prev_time = 0

    for i in input:
        time = i[0]
        reactor_id = i[1]
        enable = i[2]

        elapsed = time - prev_time
        if elapsed > 0:
            if count == max_cells_disabled:
                current_run += elapsed
                if current_run > max_duration:
                    max_duration = current_run
            else:
                current_run = 0
            prev_time = time

        if enable == False:
            disabled_reactors.add(reactor_id)
        else:
            disabled_reactors.remove(reactor_id)

        count = len(disabled_reactors)

    elapsed = MAX_TIME - prev_time
    if elapsed > 0 and count == max_cells_disabled:
        current_run += elapsed
        if current_run > max_duration:
            max_duration = current_run

    return max_duration

# sample-input.txt  input.txt
with open('input.txt') as fp:
    for line in fp:
        parse(line.strip())

max_cells_disabled = find_max_disabled(input)
max_duration = find_max_low_power_duration(input, max_cells_disabled)

print(str(max_duration))