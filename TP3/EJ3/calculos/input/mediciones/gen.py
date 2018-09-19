import visa

default_target = 'USB0::0x0957::0x0407::MY44021604::0::INSTR'

## experimental
target_b = 'USB0::0x164E::0x13EC::TW00009775::0::INSTR'

rm = visa.ResourceManager()


class Gen:
    inst = None
    instB = None

    def __init__(self):
        pass

    def connect(self, target= default_target):
        self.inst = rm.open_resource(target)
        #if target_b:
        #    self.instB = rm.open_resource(target_b)

    def set_sine(self, freq, amp):
        self.inst.write("APPL:SIN " + str(freq) + ", " + str(amp))
        if self.instB:
            self.instB.write("APPL:SIN " + str(freq) + ", " + str(amp))

    def close(self):
        if self.inst:
            self.inst.close()


