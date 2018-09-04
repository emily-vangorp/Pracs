"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

short_states = []
long_states = []
for short_state in STATE_NAMES:
    short_states.append(short_state)
for long_state in STATE_NAMES.values():
    long_states.append(long_state)
for i in range(len(short_states)):
    print("{:3} is {}".format(short_states[i], long_states[i]))
