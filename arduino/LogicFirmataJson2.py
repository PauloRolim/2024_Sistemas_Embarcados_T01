import os.path
import json
from serial.tools import list_ports
from time import sleep
from arduino import Arduino, Pin

Arduino_Uno_2_In = [22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
Arduino_Uno_2_Out = [5,6,7,8,9,10,11,12]

#B_JSON_CONFIG = r'D:\LCHIP_20180507\LCHIP\LCHIP_WORKSPACE\Combinatorial\io_config.json'
B_JSON_CONFIG = r'C:\Users\paulo\OneDrive\Área de Trabalho\arduino\io_config.json'


In = {}
Out = {}
    
def OpenBJsonConfig(input_pins, output_pins, board):
    config = {}
    print(B_JSON_CONFIG)
    if (os.path.isfile(B_JSON_CONFIG)):

        with open(B_JSON_CONFIG, mode='r') as f:
            config = json.load(f)
            
        for i in range(len(config["global_inputs"])):
            In[config["global_inputs"][i]["name"]] = Pin(board, input_pins[i])
        
        for i in range(len(config["global_outputs"])):
            Out[config["global_outputs"][i]["name"]] = Pin(board, output_pins[i])    
    
        
class Scenario():
    
    def __init__(self, board):
        self.board = board
        
    def run(self):
        while True :
          
           In['I01'].clear()
           In['I02'].clear()
           In['I03'].clear()
           
           sleep(2)
           In['I01'].set()
           sleep(5)
           In['I01'].clear()
           In['I02'].set()
           sleep(5)
           In['I02'].clear()
           In['I03'].set()
           sleep(5)
          


           # Out['O0'].read()
           # Out['O1'].read()
           # print("O0= %d O1 = %d" %(Out['O0'].status,Out['O1'].status))
           # In['I0'].clear()
           # sleep(1)

           # Out['O0'].read()
           # Out['O1'].read()
           # print("O0= %d O1 = %d" %(Out['O0'].status,Out['O1'].status))
           # In['I01'].clear()
           # sleep(1)

           # Out['O0'].read()
           # Out['O1'].read()
           # print("O0= %d O1 = %d" %(Out['O0'].status,Out['O1'].status))
           # In['I2'].clear()
           # sleep(1)

           print("iter ")
 

"""            In['I2'].clear()
            Out['O0'].read()
            print("After clear, value %d" % Out['O0'].status)
            assert Out['O0'].status == In['I2'].status
            sleep(1)
            In['I2'].set()
            Out['O0'].read()
            print("After set  , value %d" % Out['O0'].status)
            assert Out['O0'].status == In['I2'].status 
            sleep(1)
"""

def getCSPPort():
    VENDOR_ID = "2341"
    PRODUCT_ID = "0043"
    SERIAL_NUMBER = "12345"
    for port in list(list_ports.comports()):
        print ("USB VID:PID= %s:%s SNR=%s"%(VENDOR_ID, PRODUCT_ID, SERIAL_NUMBER))  
            #if port[2] == "USB VID:PID= %s:%s SNR=%s"%(self.VENDOR_ID, self.PRODUCT_ID, self.SERIAL_NUMBER):
        if port[2].find(VENDOR_ID+":"+PRODUCT_ID) != -1 :   
            #if port[2] == "USB VID:PID="+self.VENDOR_ID+":"+self.PRODUCT_ID+" SNR="+self.SERIAL_NUMBER :
            return port[0]
        
if __name__ == '__main__':
    print("Lancement");
    board = Arduino('COM3', Arduino_Uno_2_In,Arduino_Uno_2_Out)
    print("Lecture JSON");
    OpenBJsonConfig(Arduino_Uno_2_In, Arduino_Uno_2_Out, board)
    print("Exec scenario ")
    s1 = Scenario(board)
    s1.run()
