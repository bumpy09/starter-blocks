def on_button_pressed_a():
    list2: List[number] = []
    _️(1, list2)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    _️2(2, list2)
    basic.show_leds("""
        # # # # #
                # . # . #
                # # # # #
                . # # # .
                # . . . #
    """)
    basic.show_leds("""
        # # # # #
                # . # . #
                # # # # #
                . # # # .
                # . . . #
    """)
    _️3(3, list2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def _️(number: number, _1: List[any]):
    music.play_melody("C5 B A F A G C5 A ", 120)
    basic.show_leds("""
        # # # . .
                # # # . .
                . . # . .
                # # # # #
                . # # # #
    """)
    basic.show_icon(IconNames.CHESSBOARD)
def _️3(number2: number, _3: List[any]):
    edubitRgbBit.show_color(0xff0000)
    edubitRgbBit.show_color(0xff8000)
    edubitRgbBit.show_color(0xffff00)
def _️2(number3: number, _2: List[any]):
    music.play_melody("C5 B C5 B G F C A ", 120)
    basic.show_icon(IconNames.QUARTER_NOTE)
    basic.show_icon(IconNames.EIGTH_NOTE)
    basic.show_icon(IconNames.QUARTER_NOTE)
    basic.show_leds("""
        . . . . .
                . # # # .
                # # # # #
                . # # # .
                . . . . .
    """)