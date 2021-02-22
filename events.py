import time

class event:
    
    print("What is the event?")
    event_name = input()
    
    print("Who does this event belong to?")
    event_owner = input()
    
    print("What day is the event?")
    event_date = input()
    
    print("What time is the event?")
    event_time = input()
    
if __name__ == '__main__':
    user1 = event
    
    time.sleep(1)
    
    print("\n")
    print("EVENT: ", user1.event_name)
    print("OWNER: ", user1.event_owner)
    print("DATE: ", user1.event_date)
    print("TIME: ", user1.event_time)
    print("\n")
    
    print("Is this information correct? Reply YES or NO")
    confirm = input()
    if confirm == "NO":
        user1 = event
    else:
        print("See you then!")