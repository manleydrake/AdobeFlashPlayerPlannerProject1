import time
import sqlite3
connection = sqlite3.connect("Database.db")
cursor = connection.cursor()

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



#ONLY EXECUTE ONCE
cursor.execute("CREATE TABLE events(event char(50), owner char(50), date char(50), time char(50));")

cursor.execute("""INSERT INTO events(Event, Owner, Date, Time)
                    VALUES (?,?,?,?)""", (user1.event_name, user1.event_owner, user1.event_date, user1.event_time))

#DEMONSTRATION PURPOSES
cursor.execute("SELECT * FROM events;")
result = cursor.fetchall()
print(result)



connection.commit ()

print('Data Entered Successfully.')




connection.close()

if (connection):
    connection.close()
    print("\nThe SQLite connection is closed.")
