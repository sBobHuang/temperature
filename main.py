def on_button_pressed_a():
    basic.show_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string(Obloq.Obloq_http_get("input?id=1&val=1", 10000))
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_number(0)
Obloq.Obloq_http_setup(SerialPin.P2,
    SerialPin.P1,
    "tzcoder-1",
    "tzcoder.cn",
    "192.168.31.2",
    8080)
music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
basic.show_string("Hello!")