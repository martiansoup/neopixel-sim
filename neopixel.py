import simulator

GRB = "0"

class NeoPixel:
    def __init__(self, pin, num, brightness=1, auto_write=False, pixel_order=GRB):
        print("New strip @pin{} x{}".format(pin, num))
        self.pin = pin
        self.num = num
        self.lights = []
        for i in range(num):
            self.lights.append((0,0,0))
        simulator.lights.append(self)
        assert not auto_write, "auto_write not supported"

    def __setitem__(self, key, value):
        assert key < self.num, "index outside range"
        self.lights[key] = value
        #print("Led{}\t-> {}".format(key, value))

    def fill(self, value):
        for i in range(self.num):
            self.lights[i] = value

    def show(self):
        simulator.render(self)
