import visa
import time

rm = visa.ResourceManager()
default_target = 'USB0::0x0957::0x1725::MY49110442::INSTR'
SQUARES = 4
THRESHOLD = 3
OUT_OF_RANGE = 100.0
Y_SQUARES = 10


class Probe:
    scale_x = None
    scale_y = None
    channel = None

    def __init__(self, channel , inst):
        self.channel = channel
        self.inst = inst
        self.scale_y = self.get_scale_y()
        #print("initial scale y = " , self.scale_y)

    def set_scale_y(self, target):
        #print("setting scale y =", target)
        self.scale_y = target
        target = target / 4
        self.inst.write(":CHAN" + str(self.channel) + ":SCAL " + str(target))

    def get_scale_y(self):
        if not self.scale_y:
            v = self.inst.query(":CHAN" + self.channel + ":SCAL?")
            print(v)
            self.scale_y = float(v)*4

        return self.scale_y

    def get_amplitude(self):
        self.inst.write(":MEASURE:SOURCE CHANNEL" + str(self.channel))
        ans = float(self.inst.query(":MEASure:VAMPlitude?")) / 2.0
        if ans > OUT_OF_RANGE:
            return -1
        return ans

    def adjust(self):

        current = self.get_amplitude()
        size = self.get_scale_y()
        #print(current, size)

        if current == -1 or current > size * 2.0/4.0:
            self.set_scale_y(size * 1.1)
            #print("too much")
        elif current < size * 1.0 / 4.0:
            self.set_scale_y(size * 0.9)
            #print("too small")
        else:
            return 1
        return 0


class Oscilloscope:
    inst = None
    probes = dict()

    def __init__(self):
        pass

    def connect(self, target = default_target):
        self.inst = rm.open_resource(target)

        self.probes["1"] = Probe("1", self.inst)
        self.probes["2"] = Probe("2", self.inst)

        #v = self.inst.query(":CHAN"+str(1)+":SCAL?")
        #print(v)

    def set_scale_X(self, target):
        self.inst.write(":TIM:SCAL " + str(target / Y_SQUARES))

    def set_scale_Y(self, target, channel):
        self.probes[channel].set_scale_y(target)

    def get_amplitude(self, channel):
        return self.probes[channel].get_amplitude()

    def update(self):
        end = 1
        for i in self.probes.keys():
            if not self.probes[i].adjust():
                end = 0
        return end

    def ratio2to1(self):
        v = self.inst.query("MEASure:VRATio? CHAN2,CHAN1")
        return float(v)

    def phase2to1(self):
        v = self.inst.query("MEASure:PHASe? CHAN2,CHAN1")
        return float(v)

    def close(self):
        self.inst.close()



