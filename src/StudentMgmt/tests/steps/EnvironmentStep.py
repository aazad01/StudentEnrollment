import socket

from behave import *

from StudentMgmt import Environment


@given('Server is running')
def step_impl(context):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((Environment.LOCAL_HOST, Environment.PORT))
    if result == 0:
        print("Port is open")
        return True
    else:
        print("Port is not open")
        return False
