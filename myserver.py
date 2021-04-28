import sys
sys.path.insert(0, "..")
import time


from opcua import ua, Server


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    server.set_server_name("hyorim Example Server")

    #uri = server.get_application_uri()
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)
    #idx = server.get_namespace_index(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    ## object추가
    myobj = objects.add_object(idx, "MyObject")
    ## 변수 추가
    myvar = myobj.add_variable(idx, "original_temperature", 6.7)
    myvar = myobj.add_variable(idx, "temperature", 6)
    ## 해당 변수를 클라이언트가 writable하게 함
    myvar.set_writable()    # Set MyVariable to be writable by clients

    # starting!
    server.start()
    
    try:
        count = 0
        while True:
            time.sleep(1)
            count += 0.1
            #myvar.set_value(0)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
