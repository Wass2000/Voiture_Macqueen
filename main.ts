basic.showIcon(IconNames.Happy)
basic.forever(function () {
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 90)
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    if (maqueen.Ultrasonic(PingUnit.Centimeters) < 15 && maqueen.Ultrasonic(PingUnit.Centimeters) != 0) {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 70)
        basic.pause(500)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 70)
        basic.pause(500)
    }
})
