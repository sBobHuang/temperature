input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString(Obloq.Obloq_http_get("input?id=1&val=1", 10000))
    basic.clearScreen()
})
basic.showNumber(0)
Obloq.Obloq_http_setup(SerialPin.P2, SerialPin.P1, "tzcoder-1", "tzcoder.cn", "192.168.31.2", 8080)
music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.Once)
basic.showString("Hello!")
