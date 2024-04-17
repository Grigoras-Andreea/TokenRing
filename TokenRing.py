import random

class Computer:
    def __init__(self, ip, buffer):
        self.ip = ip
        self.buffer = buffer

class Token:
    def __init__(self) :
        self.source = None
        self.destination = None
        self.message = None
        self.reached_destination = False
        self.free = True

def genrate_ip():
    return str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))

def generate_computers():
    computers = []
    used_ips = set()
    for i in range(10):
        ip = genrate_ip()
        while ip in used_ips:
            ip = genrate_ip()
        used_ips.add(ip)
        computers.append(Computer(ip, ''))
    return computers

def find_computer_index(computers, target_ip):
    for i, computer in enumerate(computers):
        if computer.ip == target_ip:
            return i
    return -1

def free_token(token):
    last_source = token.source
    token.source = None
    token.destination = None
    token.message = None
    token.reached_destination = False
    token.free = True
    return last_source

def generate():
    token.source = random.choice(computers).ip
    token.destination = random.choice(computers).ip
    while token.source == token.destination:
        token.destination = random.choice(computers).ip
    token.message = "Hello from "+ token.source
    token.free = False
       
def run_token(computers, token, start):
    if start == None:
        start = token.source
    position = start
    index = find_computer_index(computers, start)
    while position != token.source:
        print("Computer ", position, " received the token")
        index += 1
        if index == len(computers):
            index = 0
        position = computers[index].ip
    print("Computer ", position, " sent a message to ", token.destination)
    while position != token.destination:
        index += 1
        if index == len(computers):
            index = 0
        position = computers[index].ip
        print("Computer ", position, " received the token")
    token.reached_destination = True
    print("Computer ", position, " received the message")
    computers[find_computer_index(computers, position)].buffer = token.message
    while position != token.source:
        index += 1
        if index == len(computers):
            index = 0
        position = computers[index].ip
        print("Computer ", position, " received the token")
    print("Computer ", position, " has received the token back")
    token.free = True
    
def print_computers(computers):
    for i in range(10):
        print('c'+str(i)+':',computers[i].ip," ",str(computers[i].buffer))
    print()

def main():
    global token
    global computers
    computers = generate_computers()
    token = Token()
    last_source = None 
    for _ in range(10):
        print_computers(computers)
        generate()
        print("Token is generated")
        print("Source: ", token.source)
        print("Destination: ", token.destination)
        print("Message: ", token.message)
        print()
        run_token(computers, token, last_source)
        print()
        last_source = free_token(token)
        print("Token is free")
        print()   
    print_computers(computers)
main()