radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    if (receivedNumber == 1) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        music.playTone(262, music.beat(BeatFraction.Quarter))
    } else if (receivedNumber == 2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            `)
        music.playTone(262, music.beat(BeatFraction.Whole))
    } else {
        basic.clearScreen()
    }
    
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_long_pressed() {
    radio.sendNumber(2)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    radio.sendNumber(1)
})
