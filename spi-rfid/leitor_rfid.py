#!/bin/env python3

from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

leitorRfid = SimpleMFRC522()

def main():
    try:
        while True:
            print("----------------------------")
            print("Aproxime o cartao do leitor:")
            cardid, text = leitorRfid.read()
            print("ID do cartao: ", cardid)
            print("Dados:")
            print(text)
            sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        raise

if __name__ == "__main__":
    main()
