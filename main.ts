input.onButtonPressed(Button.A, function () {
    let list: number[] = []
    _️(1, list)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    _️2(2, list)
    basic.showLeds(`
        # # # # #
        # . # . #
        # # # # #
        . # # # .
        # . . . #
        `)
    basic.showLeds(`
        # # # # #
        # . # . #
        # # # # #
        . # # # .
        # . . . #
        `)
    _️3(3, list)
})
function _️ (number: number, _1: any[]) {
    music.playMelody("C5 B A F A G C5 A ", 120)
    basic.showLeds(`
        # # # . .
        # # # . .
        . . # . .
        # # # # #
        . # # # #
        `)
    basic.showIcon(IconNames.Chessboard)
}
function _️3 (number: number, _3: any[]) {
    edubitRgbBit.showColor(0xff0000)
}
function _️2 (number: number, _2: any[]) {
    music.playMelody("C5 B C5 B G F C A ", 120)
    basic.showIcon(IconNames.QuarterNote)
    basic.showIcon(IconNames.EigthNote)
    basic.showIcon(IconNames.QuarterNote)
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        . # # # .
        . . . . .
        `)
}
