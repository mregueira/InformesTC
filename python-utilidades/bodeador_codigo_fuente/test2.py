import visa
import time
rm = visa.ResourceManager()
print(rm.list_resources())

inst = rm.open_resource('USB0::0x0957::0x0407::MY44013178::INSTR')

while 1:
    for i in range(1000):
        inst.write("FREQuency " + str(i * 10) )
        time.sleep(0.01)

