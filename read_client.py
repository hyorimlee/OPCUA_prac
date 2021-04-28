import sys
sys.path.insert(0, "..")


from opcua import Client


if __name__ == "__main__":

    #client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    client = Client("opc.tcp://164.125.34.159:4840/freeopcua/server/")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()
        client.load_type_definitions()  # load definition of server specific structures/extension objects
        
        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        print("Root node is: ", root)
        objects = client.get_objects_node()
        print("Objects node is: ", objects)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        print("Children of root are: ", root.get_children())

        # Stacked myvar access
        print("myvar1 is: ", objects.get_children()[1].get_variables()[0].get_value())
        print("myvar2 is: ", objects.get_children()[1].get_variables()[1].get_value())

    finally:
        client.disconnect()