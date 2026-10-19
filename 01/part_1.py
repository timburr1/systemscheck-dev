
# https://systemscheck.dev/missions/1

MAX_TIME = 48985 + 1

max_duration = 0
reactor_status = dict()

def parse(string):
    global max_duration, reactor_status

    parts = string.split(' ')
    time = int(parts[0].replace('t=', ''))
    reactor_id = int(parts[1].replace('#', ''))
    enable = parts[2] == 'enabled'

    if enable:
        time_disabled = time - reactor_status.pop(reactor_id)
        if time_disabled > max_duration:
            max_duration = time_disabled
    else:
        reactor_status[reactor_id] = time
     
# sample-input.txt
with open('input.txt') as fp:
    for line in fp:
        parse(line.strip())

for key in reactor_status:
    duration = MAX_TIME - reactor_status[key]
    if duration > max_duration:
        max_duration = duration

print(str(max_duration) + ' seconds')