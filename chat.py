# step 1: import the redis-py client package
import redis

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""


def chat():
    """Chat Redis Program"""

    # step 3: create the Redis Connection object
    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

        # step 5: the chat itself

        choice = input('Welcome to the most amazing unknown chat!\nSelect an option to continue:' \
                       '\n1. Register\n2. Login\n3. Exit')

        # Convert string to int type
        choice = int(choice)

        # Take action as per selected menu-option
        if choice == 1:
            r.set("chat:choice", choice)
            choice = r.get("chat:choice")
            print("You have selected the option " + choice + ". Wait while we're preparing everything.")
            login()

        elif choice == 2:
            r.set("chat:choice", choice)
            choice = r.get("chat:choice")
            print("You have selected the option " + choice + ". Wait while we're preparing everything.")
            register()

        elif choice == 3:
            print("See ya.")
        else:
            print("Sorry, invalid number. Try again.")

    except Exception as e:
        print(e)


def login():
    print("it works!")


def register():
    print("it works!")


if __name__ == '__main__':
    chat()
