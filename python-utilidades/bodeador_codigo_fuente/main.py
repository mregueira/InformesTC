import visa
import time
import gen
import osc

rm = visa.ResourceManager()
print(rm.list_resources())

inst = rm.open_resource("USB0::0x0957::0x0407::MY44021604::0::INSTR")

#inst.write(":MEASURE:SOURCE CHANNEL1")

#v = inst.query(":MEASure:VAMPlitude?")

#v = inst.write(":CHAN1:SCAL 1")

#print(v)

#inst.close()

# import osc
#
# micro = 10**(-6)
# #
# osc1 = osc.Oscilloscope()
# # #
# osc1.connect("USB0::0x0957::0x1725::MY49110441::INSTR")

#osc1.set_scale_Y(100, "1")

#print(osc1.get_amplitude("1") )
#osc1.set_scale_X( 100 * micro )
# end = 0
# while not end:
#     if osc1.update() == 1:
#         end = 1
# osc1.close()
k = 10**3

gen1 = gen.Gen()
gen1.connect()

gen1.set_sine(10*k, 5)

# import osc
# #
# osc1 = osc.Oscilloscope()
# osc1.connect()
#
# print(osc1.ratio2to1())
# #
# osc1.close()