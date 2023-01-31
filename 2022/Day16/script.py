import logging
logging.basicConfig(level=logging.DEBUG)

valves : 'list[Valve]' = list()

class Valve:
    def __init__(self, line : str) -> None:
        line_tokens = line.split(';')
        valve_tokens = line_tokens[0].split()
        name = valve_tokens[1]
        rate = valve_tokens[4].split('=')[1]
        tunnel_names = line_tokens[1].replace('tunnels lead to valves','').replace('tunnel leads to valve','').replace(',',' ').split()

        self.name = name
        self.rate = rate
        self.tunnel_names = tunnel_names
        self.is_open = False

with open('test.txt','r') as testFile:
    lines = [line.rstrip() for line in testFile]

for line in lines:
    valve = Valve(line)
    valves.append(valve)