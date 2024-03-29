import serial
import serial.tools.list_ports as SerialTools

class SerialConnection:
    def __init__(self):
        self.port = "NONE"
        self.speed = 9600
        self.connection = serial.Serial(timeout=1)
        

    def show_ports(self):
        '''
        List of the avilable ports.'''
        return SerialTools.comports()
    
        for port, desc, _ in sorted(SerialTools.comports()):
            print("{}: {}".format(port, desc))

    def establish_parameters(self, port, speed):
        '''
        Receive external parameters to set the port and speed.
        '''
        self.port = port
        self.speed = speed

    def start_connection(self):
        '''
        Starting the connection, it first make sure that there 
        is no current connection. Then parameters are established
        and connection is made. 
        '''
        self.connection.close()
        self.connection.port = self.port
        self.connection.baudrate = self.speed
        self.connection.open()

    def close_connection(self):
        ''' 
        Used to make an external call of the connection object
        to be closed. More code can be added if needed.
        '''
        self.connection.close()


    def write_message(self, msg):
        self.connection.write(msg)
        return True

    def flush_serial(self):
        '''
        In case it is needed, this function flushes the input 
        buffer and reads a single line in order to clear any 
        incomplete data.
        '''
        self.connection.reset_input_buffer()
        self.connection.readline()