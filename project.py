import time
rooms = {"A": "Dirt", "B": "Dirt"}
current_room = "A"
while rooms["A"] == "Dirt" or rooms["B"] == "Dirt":
    
    agent_location = current_room
    print(f"Vacuum Cleaner is in the Room {agent_location}")
    time.sleep(2)
    if rooms[agent_location] == "Dirt":
        print(f"Dirt found in Room {agent_location} !")
        time.sleep(2)
        print("Cleaning the Dirt...")
        rooms[agent_location] = "Clean"
        time.sleep(2)
        print("Dirt Cleaned !") 

    else:
        time.sleep(2)
        print(f"No Dirt found in Room {agent_location} !")
        time.sleep(2)
        print(f"Moving to another room !")
        current_room = "B" if current_room == "A" else "A"

    time.sleep(2)

time.sleep(2)
print("\nAll Rooms Cleaned !")