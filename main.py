def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P2, 1)
    basic.pause(2000)
    pins.digital_write_pin(DigitalPin.P2, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Moisture
    Moisture = pins.analog_read_pin(AnalogPin.P0)
    basic.show_string("" + str((Moisture)))
input.on_button_pressed(Button.B, on_button_pressed_b)

Graph_moisture = 0
Moisture = 0
basic.show_leds("""
    . . . . .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
""")
basic.pause(2000)
basic.clear_screen()

def on_forever():
    global Moisture, Graph_moisture
    Moisture = pins.analog_read_pin(AnalogPin.P0)
    if Moisture > 400:
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(1000)
        pins.digital_write_pin(DigitalPin.P1, 0)
    Graph_moisture = Math.map(Moisture, 750, 350, 0, 25)
    led.plot_bar_graph(Graph_moisture, 25)
    basic.pause(5000)
basic.forever(on_forever)
