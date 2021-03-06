#!/usr/bin/env python

import can
from can.bus import BusState


def receive_all():
    """Receives all messages and prints them to the console until Ctrl+C is pressed."""

    with can.interface.Bus(
        bustype="robotell", channel="COM13", bitrate=500000
    ) as bus:
        # bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
        # bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=250000)

        # set to read-only, only supported on some interfaces
        
        
        #bus.state = BusState.ACTIVE###################### linha com defeito
        ############################verificar o q é busState

        input("PAUSA")
        try:
            while True:
                msg = bus.recv(0.1)
                if msg is not None:
                    print(msg.data)
                                 
        except KeyboardInterrupt:
            print("interrupcao")
            # exit normally


if __name__ == "__main__":
    receive_all()
