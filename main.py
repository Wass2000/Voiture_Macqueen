def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_icon(IconNames.HAPPY)

def on_forever():
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 90)
    maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
    maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 15 and maqueen.ultrasonic(PingUnit.CENTIMETERS) != 0:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 70)
        basic.pause(500)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 70)
        basic.pause(500)
basic.forever(on_forever)
