def vacuum_cleaner(roomsNumber):
    for i in range(1, roomsNumber+1):
        print(f"vacuum cleaner is currently in room {i}.")
        room_state = input(f"Enter the state of room {i} (clean or dirty): ")
        while room_state.lower() not in ["clean", "dirty"]:
            print("Invalid input. Please enter 'clean' or 'dirty'.")
            room_state = input(f"Enter the state of room {i} (clean or dirty): ")
        if room_state == "dirty":
            print(f"Cleaning room {i}.")
        else:
            print(f"Room {i} is already cleaned.")
    print("All yours rooms are clean.Successfully cleaning complete.")

roomsNumber = int(input("Enter number of rooms to clean / Goal state: "))
vacuum_cleaner(roomsNumber)
