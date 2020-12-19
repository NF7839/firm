import pyfirmata

# loopları uzun haliyle yaz

# enum olmaması kötü ya
class ArduinoTypes:
    none = 0
    nano = 1
    mega = 2


class Arduino:
    def __init__(self, pins: list, port: str, arduino_type: ArduinoTypes=0,
                 invert: bool=0, start_state: bool=1):
        
        if arduino_type == ArduinoTypes.nano:
            self.board = pyfirmata.ArduinoNano(port)
        elif arduino_type == ArduinoTypes.mega:
            self.board = pyfirmata.ArduinoMega(port)
        else:
            self.board = pyfirmata.Arduino(port)

        self.start_state = start_state
        self.type = arduino_type
        self.invert = invert
        self.port = port

        self.pin_numbers = pins  # Elimizdeki pinlerin Arduino üzerinde denk geldiği yerler
        # Şimdi bu pinleri de almamız gerekiyor
        
        # yeni başlayanlar için fazla karmaşık
        # self.pins = [(self.board.get_pin(f"d:{pin}:o"), self.board.digital[pin].write(1-start_state if invert else start_state))[0] for pin in pins]
        
        self.pins = []
        for i in pins:
            pin = self.board.get_pin(f"d:{i}:o")
            pin.write(1-start_state if invert else start_state)
            self.pins.append(pin)
            # yorumları yarın yaparım şimdi yazılım zamanı

    def write(self, pin: int, state: bool):
        state = 1-state if self.invert else state
        # müzik açıp gelcem
        try:
            self.pins[self.pin_numbers.index(pin)].write(state) if pin in self.pin_numbers else self.board.digital[pin].write(state)
        except:
            return False
        return True

    def write_all(self, state: bool):
        try:
            # umarım generator gibi davranmıyordur
            if False in [self.write(pin, state) for pin in self.pins]:
                raise Exception
        except:
            return False
        return True

    def __repr__(self):
        return "\n".join(["pin \t>> \tstate"] + [f"{num} \t>> \t{pin.read()}" for num, pin in zip(self.pin_numbers, self.pins)])


