def on_received_number(receivedNumber):
    if receivedNumber == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
    elif receivedNumber == 2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            """)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    else:
        basic.clear_screen()
radio.on_received_number(on_received_number)

def on_logo_long_pressed():
    radio.send_number(2)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_logo_pressed():
    radio.send_number(1)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
