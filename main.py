def on_player4_button_up_pressed():
    characterAnimations.run_frames(mySprite4,
        [img("""
                . . . . . . c c c . . . . . . .
                . . . . . . c 5 b c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f f f f f f f f f f . .
                . . f f f f f f f f f f f f . .
                . . . f f f f f f f f f f . . .
                . . . e e f f f f f f f e . . .
                . . e b f b 5 b b 5 b c b e . .
                . . e e f 5 5 5 5 5 5 f e e . .
                . . . . c b 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . c c . . . . . .
                . . . . . . . c 5 c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f f f f f f f f f f . .
                . . f f f f f f f f f f f f . .
                . . . f f f f f f f f f f . . .
                . . . e b e e f f f f b b e . .
                . . . e b b e b b 5 5 f e e . .
                . . . . c e e 5 5 5 5 5 f . . .
                . . . . . f f f f f f f . . . .
                """),
            img("""
                . . . . . . . c c c . . . . . .
                . . . . . . c b 5 c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f f f f f f f f f f . .
                . . f f f f f f f f f f f f . .
                . . . f f f f f f f f f f . . .
                . . . e e f f f f f f e e . . .
                . . e b c b 5 b b 5 b f b e . .
                . . e e f 5 5 5 5 5 5 f e e . .
                . . . . c b 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . c c . . . . . . . .
                . . . . . . c 5 c . . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f f f f f f f f f f . .
                . . f f f f f f f f f f f f . .
                . . . f f f f f f f e e f . . .
                . . e b b f e e e e e b e . . .
                . . e e f 5 5 b b e b b e . . .
                . . . f 5 5 5 5 5 e e c . . . .
                . . . . f f f f f f f . . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_UP, Predicate.MOVING))
controller.player4.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player4_button_up_pressed)

def on_player3_button_b_pressed():
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . . . . . . . . . .
                . . . . . f f f f . . . .
                . . . f f f f f f f f . .
                . . f f f f f f c f f f .
                f f f f f f f c c f f f c
                f f f f c f f f f f f f c
                . c c c f f f e e f f c c
                . f f f f f e e f f c c f
                . f f f b f e e f b f f f
                . f f 4 1 f 4 4 f 1 4 f f
                . . f e 4 4 4 4 4 e e f e
                . f e f b 7 7 7 e 4 4 4 e
                . e 4 f 7 7 7 7 e 4 4 e .
                . . . f 6 6 6 6 6 e e . .
                . . . f f f f f f f . . .
                . . . f f f . f f f . . .
                """),
            img("""
                . . . . . . . . . . . . .
                . . . . f f f f . . . . .
                . . f f f f f f f f . . .
                . f f f c f f f f f f . .
                c f f f c c f f f f f f f
                c f f f f f f f c f f f f
                c c f f e e f f f c c c .
                f c c f f e e f f f f f .
                f f f b f e e f b f f f .
                f f 4 1 f 4 4 f 1 4 f f .
                e f e e 4 4 4 4 4 e f . .
                e 4 4 4 e 7 7 7 b f e f .
                . e 4 4 e 7 7 7 7 f 4 e .
                . . e e 6 6 6 6 6 f . . .
                . . . f f f f f f f . . .
                . . . f f f . f f f . . .
                """)],
        100,
        False)
    sprites.destroy(mySprite6, effects.ashes, 5000)
controller.player3.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player3_button_b_pressed)

def on_player2_button_b_pressed():
    animation.run_image_animation(mySprite2,
        [img("""
                .............2..2.......
                ....ffffff...2..2......2
                ..ffeeee99f..2......222.
                .ffeeeef9999.2......2...
                .feeeffeeeef...cc.......
                .ffffee9999ef.cdc.......
                .fe999ffffe9fcddc.22....
                fffffffeeeffcddc....2222
                ffe44ebf44ecddc.........
                fee4d41fddecdc..........
                .feee4dddedccc...2......
                ..ffee44e4dde.....2.....
                ...f999944ee.......22...
                ...f9999e9f.........2...
                ...f444455f.............
                ....ffffff..............
                .....fff................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                .................2......
                .......fff.......2......
                ....fffff9f......2......
                ..ffeeeee999f....2.....2
                .ffeeeeee999ff....2..22.
                .feeeefffeeeef....2..2..
                .fffffeee9999ef...2.....
                fffe999fffffe9f.........
                fffffffffeeefff.....cc..
                fefe44ebbf44eef...ccdc..
                .fee4d4bbfddef..ccddcc..
                ..feee4dddddfeecdddc....
                ...f9999999eeddcdcc..222
                ...f444445e44ddccc......
                ...ffffffffeeee.....2...
                ...fff...ff......2..2.22
                ....................2...
                .....................2..
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                .......ff.......5.......
                ....ffff99f.....5.......
                ..ffeeeef9ff....5.......
                .ffeeeeef999f...5.......
                .feeeeffeeeef...5...55.5
                .fffffee9999ef......5..5
                fffe9999fffe9f.....55..5
                ffffffffeeefff....55..5.
                fefe44ebf44eef...55...5.
                .fee4d4bfddef...55...5..
                ..feee4dddee.c..5.......
                ...f9999eeddeccccccc....
                ...f444e44ddecddddd.....
                ...fffffeeee.ccccc...5..
                ..ffffffff...c.......55.
                ..fff..ff....55.......55
                ..........55.5...5..5..5
                .........55.....5....5..
                .......55.......5.......
                ......5........5........
                ...555.......55.........
                ...5........55..........
                ...........55...........
                ...........5............
                """),
            img("""
                ....ffffff..............
                ..ffeeeef9f.............
                .ffeeeef9999............
                .feeeffeeeef............
                .ffffee99999f...........
                .fe999ffffe9f...........
                fffffffeeefff...........
                ffe44ebf44eef...........
                fee4d41fddef............
                .feee4ddddf....ffffff...
                ..fdde444ef..ff.....f...
                ..fdde999cc.ff..2222.f..
                ...eef999dc.f.222..22f..
                ...f4444cddc..2.....2f..
                ....fffffcddc.2....22f..
                .....fff..cddc.....2.f..
                ........f..cdc.....2.f..
                .......ff2..cc....22f...
                .......f.2.......22.f...
                ......ff.22222222..ff...
                .......ff......fffff....
                ........fffffff.........
                ........................
                ........................
                """)],
        500,
        False)
    sprites.destroy(mySprite7, effects.fire, 5000)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_player1_button_up_pressed():
    characterAnimations.run_frames(mySprite,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f f 2 f e f . .
                . . f f f 2 f e e 2 2 f f f . .
                . . f e 2 f f e e 2 f e e f . .
                . f f e f f e e e f e e e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . . e f f f f f f f f 4 e . .
                . . . 4 f 2 2 2 2 2 e d d 4 . .
                . . . e f f f f f f e e 4 . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e f 2 f f f 2 f 2 e f . .
                . . f f f 2 2 e e f 2 f f f . .
                . . f e e f 2 e e f f 2 e f . .
                . f f e e e f e e e f f e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f e . . .
                . . 4 d d e 2 2 2 2 2 f 4 . . .
                . . . 4 e e f f f f f f e . . .
                . . . . . . . . . f f f . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_UP, Predicate.MOVING))
controller.player1.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player1_button_up_pressed)

def on_player2_button_down_pressed():
    characterAnimations.loop_frames(mySprite,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 9 9 f f f . . . .
                . . . f f f 9 9 9 9 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 9 9 9 9 9 9 e e f . .
                . . f e 9 f f f f f f 9 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 9 9 9 9 9 9 f 4 e . .
                . . 4 d f 9 9 9 9 9 9 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 9 9 f f f . . . .
                . . . f f f 9 9 9 9 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 9 9 9 9 9 9 e e f . .
                . . f e 9 f f f f f f 9 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 9 9 9 9 9 9 f 4 e . .
                . . 4 d f 9 9 9 9 9 9 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 9 9 f f f . . . .
                . . . f f f 9 9 9 9 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 9 9 9 9 9 9 e e f . .
                . f f e 9 f f f f f f 9 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . . f e 4 d d d d 4 e f e . .
                . . f e f 9 9 9 9 e d d 4 e . .
                . . e 4 f 9 9 9 9 e d d e . . .
                . . . . f 4 4 5 5 f e e . . . .
                . . . . f f f f f f f . . . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 9 9 f f f . . . .
                . . . f f f 9 9 9 9 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f e e 9 9 9 9 9 9 e f f . .
                . f f e 9 f f f f f f 9 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . e f e 4 d d d d 4 e f . . .
                . . e 4 d d e 9 9 9 9 f e f . .
                . . . e d d e 9 9 9 9 f 4 e . .
                . . . . e e f 5 5 4 4 f . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . . . . f f f . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_DOWN, Predicate.MOVING))
controller.player2.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player2_button_down_pressed)

def on_player4_button_down_pressed():
    characterAnimations.run_frames(mySprite,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . c c . . . . . . . .
                . . . . . . c 5 c . . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . . f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . e e e b b b b b e f f . . .
                . . e b b e e e e e b f e . . .
                . . e b b e 5 b b e b f e . . .
                . . e e c 5 5 5 5 e e f . . . .
                . . . . f f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . c c . . . . . .
                . . . . . . . c 5 c . . . . . .
                . . . . c c c 5 5 c c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f f . .
                . . f f f b f e e f b f f f . .
                . . f f f 1 f b b f 1 f f f . .
                . . . f e e e b b b b f f . . .
                . . . e b b e e e e f b b e . .
                . . . e b b e b b 5 5 f e e . .
                . . . . c e e 5 5 5 5 5 f . . .
                . . . . . f f f f f f f . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_DOWN, Predicate.MOVING))
controller.player4.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player4_button_down_pressed)

def on_player3_button_right_pressed():
    characterAnimations.run_frames(mySprite3,
        [img("""
                . . . . . . . . . . . . .
                . . . f f f f f f . . . .
                . f f f f f f f f f . . .
                . f f f f f f c f f f . .
                f f f f c f f f c f f f .
                f c f f c c f f f c c f f
                f c c f f f f e f f f f f
                f f f f f f f e e f f f .
                f f e e f b f e e f f f .
                f f e 4 e 1 f 4 4 f f . .
                . f f f e 4 4 4 4 f . . .
                . 4 4 4 e e e e f f . . .
                . e 4 4 e 7 7 7 7 f . . .
                . f e e f 6 6 6 6 f f . .
                . f f f f f f f f f f . .
                . . f f . . . f f f . . .
                """),
            img("""
                . . . . . . . . . . . . .
                . . . f f f f f f . . . .
                . f f f f f f f f f . . .
                . f f f f f f c f f f . .
                f f f f c f f f c f f f .
                f c f f c c f f f c c f f
                f c c f f f f e f f f f f
                f f f f f f f e e f f f .
                f f e e f b f e e f f . .
                . f e 4 e 1 f 4 4 f f . .
                . f f f e e 4 4 4 f . . .
                . . f e 4 4 e e f f . . .
                . . f e 4 4 e 7 7 f . . .
                . f f f e e f 6 6 f f . .
                . f f f f f f f f f f . .
                . . f f . . . f f f . . .
                """),
            img("""
                . . . f f f f f . . . . .
                . f f f f f f f f f . . .
                . f f f f f f c f f f . .
                f f f f c f f f c f f . .
                f c f f c c f f f c c f f
                f c c f f f f e f f f f f
                f f f f f f f e e f f f .
                f f e e f b f e e f f . .
                . f e 4 e 1 f 4 4 f . . .
                . f f f e 4 4 4 4 f . . .
                . . f e e e e e f f . . .
                . . e 4 4 e 7 7 7 f . . .
                . . e 4 4 e 7 7 7 f . . .
                . . f e e f 6 6 6 f . . .
                . . . f f f f f f . . . .
                . . . . f f f . . . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_RIGHT, Predicate.MOVING))
controller.player3.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player3_button_right_pressed)

def on_player2_button_up_pressed():
    characterAnimations.loop_frames(mySprite2,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 9 9 f f f f f . .
                . . f f e 9 e 9 9 e 9 e f f . .
                . . f e 9 f 9 f f 9 f 9 e f . .
                . . f f f 9 9 e e 9 9 f f f . .
                . f f e f 9 f e e f 9 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 9 9 9 9 9 9 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 9 9 f f f f . . .
                . . f f e 9 e 9 9 e 9 e f f . .
                . . f e 9 f 9 f f f 9 f e f . .
                . . f f f 9 f e e 9 9 f f f . .
                . . f e 9 f f e e 9 f e e f . .
                . f f e f f e e e f e e e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . . e f f f f f f f f 4 e . .
                . . . 4 f 9 9 9 9 9 e d d 4 . .
                . . . e f f f f f f e e 4 . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 9 9 f f f f f . .
                . . f f e 9 e 9 9 e 9 e f f . .
                . . f e 9 f 9 f f 9 f 9 e f . .
                . . f f f 9 9 e e 9 9 f f f . .
                . f f e f 9 f e e f 9 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 9 9 9 9 9 9 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 9 9 f f f f . . .
                . . f f e 9 e 9 9 e 9 e f f . .
                . . f e f 9 f f f 9 f 9 e f . .
                . . f f f 9 9 e e f 9 f f f . .
                . . f e e f 9 e e f f 9 e f . .
                . f f e e e f e e e f f e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f e . . .
                . . 4 d d e 9 9 9 9 9 f 4 . . .
                . . . 4 e e f f f f f f e . . .
                . . . . . . . . . f f f . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_UP, Predicate.MOVING))
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def on_player2_button_right_pressed():
    characterAnimations.run_frames(mySprite2,
        [img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 9 f . . .
                . . . f f e e e e f 9 9 9 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 9 9 9 9 e f .
                . . . f e 9 9 9 f f f f e 9 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 9 9 9 f . . .
                . . . . . e d d e 9 9 9 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 9 f . . .
                . . . f f e e e e f 9 9 9 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 9 9 9 9 e f .
                . . . f e 9 9 9 f f f f e 9 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e e e d d d f . . .
                . . . . . f 4 d d e 4 e f . . .
                . . . . . f e d d e 9 9 f . . .
                . . . . f f f e e f 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """),
            img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 9 f . . .
                . . . f f e e e e f 9 9 9 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 9 9 9 9 e f .
                . . . f e 9 9 9 f f f f e 9 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 9 9 9 f . . .
                . . . . . e d d e 9 9 9 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 9 f . . .
                . . . f f e e e e f 9 9 9 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 9 9 9 9 e f .
                . . . f e 9 9 9 f f f f e 9 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . 4 d d e 4 4 4 e f . . .
                . . . . e d d e 9 9 9 9 f . . .
                . . . . f e e f 4 4 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_RIGHT, Predicate.MOVING))
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_right_pressed)

def on_player2_button_left_pressed():
    characterAnimations.run_frames(mySprite2,
        [img("""
                . . . . f f f f f f . . . . . .
                . . . f 9 f e e e e f f . . . .
                . . f 9 9 9 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 9 9 9 9 e e f f f f . . .
                . f 9 e f f f f 9 9 9 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 9 f e e e e f f . . . .
                . . f 9 9 9 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 9 9 9 9 e e f f f f . . .
                . f 9 e f f f f 9 9 9 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d e e e e e f . . .
                . . . f e 4 e d d 4 f . . . . .
                . . . f 9 9 e d d e f . . . . .
                . . f f 5 5 f e e f f f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """),
            img("""
                . . . . f f f f f f . . . . . .
                . . . f 9 f e e e e f f . . . .
                . . f 9 9 9 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 9 9 9 9 e e f f f f . . .
                . f 9 e f f f f 9 9 9 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 9 9 9 e d d 4 . . . . .
                . . . f 9 9 9 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 9 f e e e e f f . . . .
                . . f 9 9 9 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 9 9 9 9 e e f f f f . . .
                . f 9 e f f f f 9 9 9 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e d d 4 . . . .
                . . . f 9 9 9 9 e d d e . . . .
                . . f f 5 5 4 4 f e e f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_LEFT, Predicate.MOVING))
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_left_pressed)

def on_player3_button_down_pressed():
    characterAnimations.run_frames(mySprite3,
        [img("""
                . . . . f f f f . . . . .
                . . f f f f f f f f . . .
                . f f f f f f c f f f . .
                f f f f f f c c f f f c .
                f f f c f f f f f f f c .
                c c c f f f e e f f c c .
                f f f f f e e f f c c f .
                f f f b f e e f b f f f .
                . f 4 1 f 4 4 f 1 4 f . .
                . f e 4 4 4 4 4 4 e f . .
                . f f f e e e e f f f . .
                f e f b 7 7 7 7 b f e f .
                e 4 f 7 7 7 7 7 7 f 4 e .
                e e f 6 6 6 6 6 6 f e e .
                . . . f f f f f f . . . .
                . . . f f . . f f . . . .
                """),
            img("""
                . . . . . . . . . . . . .
                . . . . . f f f f . . . .
                . . . f f f f f f f f . .
                . . f f f f f f c f f f .
                f f f f f f f c c f f f c
                f f f f c f f f f f f f c
                . c c c f f f e e f f c c
                . f f f f f e e f f c c f
                . f f f b f e e f b f f f
                . f f 4 1 f 4 4 f 1 4 f f
                . . f e 4 4 4 4 4 e e f e
                . f e f b 7 7 7 e 4 4 4 e
                . e 4 f 7 7 7 7 e 4 4 e .
                . . . f 6 6 6 6 6 e e . .
                . . . f f f f f f f . . .
                . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . .
                . . . . f f f f . . . . .
                . . f f f f f f f f . . .
                . f f f c f f f f f f . .
                c f f f c c f f f f f f f
                c f f f f f f f c f f f f
                c c f f e e f f f c c c .
                f c c f f e e f f f f f .
                f f f b f e e f b f f f .
                f f 4 1 f 4 4 f 1 4 f f .
                e f e e 4 4 4 4 4 e f . .
                e 4 4 4 e 7 7 7 b f e f .
                . e 4 4 e 7 7 7 7 f 4 e .
                . . e e 6 6 6 6 6 f . . .
                . . . f f f f f f f . . .
                . . . . . . . f f f . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_DOWN, Predicate.MOVING))
controller.player3.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player3_button_down_pressed)

def on_player1_button_right_pressed():
    characterAnimations.run_frames(mySprite,
        [img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e e e d d d f . . .
                . . . . . f 4 d d e 4 e f . . .
                . . . . . f e d d e 2 2 f . . .
                . . . . f f f e e f 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """),
            img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . 4 d d e 4 4 4 e f . . .
                . . . . e d d e 2 2 2 2 f . . .
                . . . . f e e f 4 4 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_RIGHT, Predicate.MOVING))
controller.player1.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_right_pressed)

def on_player4_button_left_pressed():
    characterAnimations.run_frames(mySprite4,
        [img("""
                . . . . . . . c c . . . . . . .
                . . . . . . c 5 c . . . . . . .
                . . . . c c 5 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . . f 5 5 5 5 5 5 5 5 f f . .
                . . . . f e e e f b e e f f . .
                . . . . f e b b f 1 b f f f . .
                . . . . f b b b b b b f f . . .
                . . . . . f e e e e f e e . . .
                . . . . . f 5 b b e b b e . . .
                . . . . f 5 5 5 5 e b b e . . .
                . . . . c b 5 5 5 5 e e . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . c c . . . . . . .
                . . . . . . c c 5 c . . . . . .
                . . . . c c 5 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . . f 5 5 5 5 5 5 5 5 f f . .
                . . . . f e e e f b e e f f . .
                . . . . f e b b f 1 b f f f . .
                . . . . f b b b b e e f f . . .
                . . . . . f e e e b b e f . . .
                . . . . f 5 b b e b b e . . . .
                . . . . c 5 5 5 5 e e f . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . c c . . . . . . .
                . . . . . . c 5 c . . . . . . .
                . . . . c c 5 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . . f 5 5 5 5 5 5 5 5 f f . .
                . . . . f e e e f b e e f f . .
                . . . . f e b b f 1 b f f f . .
                . . . . f b b b b b b f f . . .
                . . . . . f e e e e f e e . . .
                . . . . . f 5 b b e b b e . . .
                . . . . f 5 5 5 5 e b b e . . .
                . . . . c b 5 5 5 5 e e . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . c c . . . . . . .
                . . . . . . c c 5 c . . . . . .
                . . . . c c 5 5 5 c c c . . . .
                . . c c c c 5 5 5 5 c b c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . c 5 5 5 b b b b 5 5 5 f . .
                . . . f 5 5 5 5 5 5 5 5 f f . .
                . . . . f e e e f b e e f f . .
                . . . . f e b b f 1 b f f f . .
                . . . . f b b b b b b f f . . .
                . . . . . f e e e e e b b e . .
                . . . . f 5 5 b b b e b b e . .
                . . . . c 5 5 5 5 5 e e e . . .
                . . . . . f f f f f f . . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_LEFT, Predicate.MOVING))
controller.player4.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player4_button_left_pressed)

def on_life_zero(player2):
    music.play(music.create_song(assets.song("""
            clef
            """)),
        music.PlaybackMode.UNTIL_DONE)
    game.set_game_over_message(False, "GAME OVER!")
mp.on_life_zero(on_life_zero)

def on_player1_button_b_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                ........................
                ....ffffff..............
                ..ffeeeef2f.............
                .ffeeeef222f............
                .feeeffeeeef...cc.......
                .ffffee2222ef.cdc.......
                .fe222ffffe2fcddc.......
                fffffffeeeffcddc........
                ffe44ebf44ecddc.........
                fee4d41fddecdc..........
                .feee4dddedccc..........
                ..ffee44e4dde...........
                ...f222244ee............
                ...f2222e2f.............
                ...f444455f.............
                ....ffffff..............
                .....fff................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                ........................
                .......fff..............
                ....fffff2f.............
                ..ffeeeee22ff...........
                .ffeeeeee222ff..........
                .feeeefffeeeef..........
                .fffffeee2222ef.........
                fffe222fffffe2f.........
                fffffffffeeefff.....cc..
                fefe44ebbf44eef...ccdc..
                .fee4d4bbfddef..ccddcc..
                ..feee4dddddfeecdddc....
                ...f2222222eeddcdcc.....
                ...f444445e44ddccc......
                ...ffffffffeeee.........
                ...fff...ff.............
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                .......ff...............
                ....ffff2ff.............
                ..ffeeeef2ff............
                .ffeeeeef22ff...........
                .feeeeffeeeef...........
                .fffffee2222ef..........
                fffe222ffffe2f..........
                ffffffffeeefff..........
                fefe44ebf44eef..........
                .fee4d4bfddef...........
                ..feee4dddee.c..........
                ...f2222eeddeccccccc....
                ...f444e44ddecddddd.....
                ...fffffeeee.ccccc......
                ..ffffffff...c..........
                ..fff..ff...............
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                ....ffffff..............
                ..ffeeeef2f.............
                .ffeeeef222f............
                .feeeffeeeef............
                .ffffee2222ef...........
                .fe222ffffe2f...........
                fffffffeeefff...........
                ffe44ebf44eef...........
                fee4d41fddef............
                .feee4ddddf.............
                ..fdde444ef.............
                ..fdde22ccc.............
                ...eef22cdc.............
                ...f4444cddc............
                ....fffffcddc...........
                .....fff..cddc..........
                ...........cdc..........
                ............cc..........
                ........................
                ........................
                ........................
                ........................
                ........................
                ........................
                """)],
        500,
        False)
    sprites.destroy(mySprite5, effects.fire, 5000)
controller.player1.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player1_button_b_pressed)

def on_player4_button_right_pressed():
    characterAnimations.run_frames(mySprite4,
        [img("""
                . . . . . . . c c . . . . . . .
                . . . . . . . c 5 c . . . . . .
                . . . . c c c 5 5 5 c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f . . .
                . . f f e e b f e e e f . . . .
                . . f f f b 1 f b b e f . . . .
                . . . f f b b b b b b f . . . .
                . . . e e f e e e e f . . . . .
                . . . e b b e b b 5 f . . . . .
                . . . e b b e 5 5 5 5 f . . . .
                . . . . e e 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . c c . . . . . . .
                . . . . . . c 5 c c . . . . . .
                . . . . c c c 5 5 5 c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f . . .
                . . f f e e b f e e e f . . . .
                . . f f f b 1 f b b e f . . . .
                . . . f f e e b b b b f . . . .
                . . . f e b b e e e f . . . . .
                . . . . e b b e b b 5 f . . . .
                . . . . f e e 5 5 5 5 c . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . c c . . . . . . .
                . . . . . . . c 5 c . . . . . .
                . . . . c c c 5 5 5 c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f . . .
                . . f f e e b f e e e f . . . .
                . . f f f b 1 f b b e f . . . .
                . . . f f b b b b b b f . . . .
                . . . e e f e e e e f . . . . .
                . . . e b b e b b 5 f . . . . .
                . . . e b b e 5 5 5 5 f . . . .
                . . . . e e 5 5 5 5 b c . . . .
                . . . . . f f f f f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . c c . . . . . . .
                . . . . . . c 5 c c . . . . . .
                . . . . c c c 5 5 5 c c . . . .
                . . c c b c 5 5 5 5 c c c c . .
                . c b b 5 b 5 5 5 5 b 5 b b c .
                . c b 5 5 b b 5 5 b b 5 5 b c .
                . . f 5 5 5 b b b b 5 5 5 c . .
                . . f f 5 5 5 5 5 5 5 5 f . . .
                . . f f e e b f e e e f . . . .
                . . f f f b 1 f b b e f . . . .
                . . . f f b b b b b b f . . . .
                . . e b b e e e e e f . . . . .
                . . e b b e b b b 5 5 f . . . .
                . . . e e e 5 5 5 5 5 c . . . .
                . . . . . f f f f f f . . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_RIGHT, Predicate.MOVING))
controller.player4.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player4_button_right_pressed)

def on_player3_button_left_pressed():
    characterAnimations.run_frames(mySprite3,
        [img("""
                . . . . . f f f f f . . .
                . . . f f f f f f f f f .
                . . f f f c f f f f f f .
                . . f f c f f f c f f f f
                f f c c f f f c c f f c f
                f f f f f e f f f f c c f
                . f f f e e f f f f f f f
                . . f f e e f b f e e f f
                . . . f 4 4 f 1 e 4 e f .
                . . . f 4 4 4 4 e f f f .
                . . . f f e e e e e f . .
                . . . f 7 7 7 e 4 4 e . .
                . . . f 7 7 7 e 4 4 e . .
                . . . f 6 6 6 f e e f . .
                . . . . f f f f f f . . .
                . . . . . . f f f . . . .
                """),
            img("""
                . . . . . . . . . . . . .
                . . . . f f f f f f . . .
                . . . f f f f f f f f f .
                . . f f f c f f f f f f .
                . f f f c f f f c f f f f
                f f c c f f f c c f f c f
                f f f f f e f f f f c c f
                . f f f e e f f f f f f f
                . . f f e e f b f e e f f
                . . f f 4 4 f 1 e 4 e f .
                . . . f 4 4 4 e e f f f .
                . . . f f e e 4 4 e f . .
                . . . f 7 7 e 4 4 e f . .
                . . f f 6 6 f e e f f f .
                . . f f f f f f f f f f .
                . . . f f f . . . f f . .
                """),
            img("""
                . . . . . . . . . . . . .
                . . . . f f f f f f . . .
                . . . f f f f f f f f f .
                . . f f f c f f f f f f .
                . f f f c f f f c f f f f
                f f c c f f f c c f f c f
                f f f f f e f f f f c c f
                . f f f e e f f f f f f f
                . f f f e e f b f e e f f
                . . f f 4 4 f 1 e 4 e f f
                . . . f 4 4 4 4 e f f f .
                . . . f f e e e e 4 4 4 .
                . . . f 7 7 7 7 e 4 4 e .
                . . f f 6 6 6 6 f e e f .
                . . f f f f f f f f f f .
                . . . f f f . . . f f . .
                """)],
        500,
        characterAnimations.rule(Predicate.MOVING_DOWN, Predicate.MOVING))
controller.player3.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player3_button_left_pressed)

def on_player3_button_up_pressed():
    pass
controller.player3.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player3_button_up_pressed)

def on_player1_button_left_pressed():
    characterAnimations.run_frames(mySprite,
        [img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d e e e e e f . . .
                . . . f e 4 e d d 4 f . . . . .
                . . . f 2 2 e d d e f . . . . .
                . . f f 5 5 f e e f f f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """),
            img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e d d 4 . . . .
                . . . f 2 2 2 2 e d d e . . . .
                . . f f 5 5 4 4 f e e f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_LEFT, Predicate.MOVING))
controller.player1.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_left_pressed)

def on_player1_button_down_pressed():
    characterAnimations.run_frames(mySprite,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . . f e 4 d d d d 4 e f e . .
                . . f e f 2 2 2 2 e d d 4 e . .
                . . e 4 f 2 2 2 2 e d d e . . .
                . . . . f 4 4 5 5 f e e . . . .
                . . . . f f f f f f f . . . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f e e 2 2 2 2 2 2 e f f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . e f e 4 d d d d 4 e f . . .
                . . e 4 d d e 2 2 2 2 f e f . .
                . . . e d d e 2 2 2 2 f 4 e . .
                . . . . e e f 5 5 4 4 f . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . . . . f f f . . . .
                """)],
        100,
        characterAnimations.rule(Predicate.MOVING_DOWN, Predicate.MOVING))
controller.player1.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player1_button_down_pressed)

statusbar: StatusBarSprite = None
mySprite7: Sprite = None
mySprite6: Sprite = None
mySprite5: Sprite = None
mySprite4: Sprite = None
mySprite3: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(assets.image("""
    Jake
    """), SpriteKind.player)
controller.player1.move_sprite(mySprite)
mySprite2 = sprites.create(assets.image("""
    Jake 2
    """), SpriteKind.player)
controller.player2.move_sprite(mySprite2)
mySprite3 = sprites.create(assets.image("""
    Jeff
    """), SpriteKind.player)
controller.player3.move_sprite(mySprite3)
mySprite4 = sprites.create(assets.image("""
    Jeff2
    """), SpriteKind.player)
controller.player4.move_sprite(mySprite4)
mySprite5 = sprites.create(assets.image("""
    Zombie
    """), SpriteKind.enemy)
mySprite5.follow(mySprite, 5)
mySprite5.x = 30
scene.set_background_image(assets.image("""
    Sort
    """))
info.set_life(3)
mySprite6 = sprites.create(img("""
        ........................
        ........................
        ........................
        ........................
        ..........ffff..........
        ........ff1111ff........
        .......fb111111bf.......
        .......f11111111f.......
        ......fd11111111df......
        ......fd11111111df......
        ......fddd1111dddf......
        ......fbdbfddfbdbf......
        ......fcdcf11fcdcf......
        .......fb111111bf.......
        ......fffcdb1bdffff.....
        ....fc111cbfbfc111cf....
        ....f1b1b1ffff1b1b1f....
        ....fbfbffffffbfbfbf....
        .........ffffff.........
        ...........fff..........
        ........................
        ........................
        ........................
        ........................
        """),
    SpriteKind.player)
mySprite6.follow(mySprite3, 5)
characterAnimations.loop_frames(mySprite6,
    [img("""
            ........................
            ........................
            ........................
            ........................
            ..........fffff.........
            ........ff1111bff.......
            .......fb1111111bf......
            .......f111111111f......
            ......fd1111111ffff.....
            ......fd111dd1c111bf....
            ......fb11fcdf1b1bff....
            ......f11111bfbfbff.....
            ......f1b1bdfcffff......
            ......fbfbfcfcccf.......
            ......ffffffffff........
            .........ffffff.........
            .........ffffff.........
            .........fffffff..f.....
            ..........fffffffff.....
            ...........fffffff......
            ........................
            ........................
            ........................
            ........................
            """),
        img("""
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f1111111dbf......
            ......fd1111111ddf......
            ......fd111111dddf......
            ......fd111ddddddf......
            ......fd111ddddddf......
            ......fd1dddddddbf......
            ......fd1dfbddbbff......
            ......fbddfcdbbcf.......
            .....ffffccddbfff.......
            ....fcb1bbbfcffff.......
            ....f1b1dcffffffff......
            ....fdfdf..ffffffffff...
            .....f.f.....ffffff.....
            ........................
            ........................
            ........................
            ........................
            ........................
            """)],
    500,
    characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT))
mySprite7 = sprites.create(img("""
        ........................
        ........................
        ........................
        ........................
        ..........ffff..........
        ........ff1111ff........
        .......fb111111bf.......
        .......f11111111f.......
        ......fd11111111df......
        ......fd11111111df......
        ......fddd1111dddf......
        ......fbdbfddfbdbf......
        ......fcdcf11fcdcf......
        .......fb111111bf.......
        ......fffcdb1bdffff.....
        ....fc111cbfbfc111cf....
        ....f1b1b1ffff1b1b1f....
        ....fbfbffffffbfbfbf....
        .........ffffff.........
        ...........fff..........
        ........................
        ........................
        ........................
        ........................
        """),
    SpriteKind.player)
mySprite7.follow(mySprite2, 5)
characterAnimations.loop_frames(mySprite7,
    [img("""
            ........................
            ........................
            ........................
            ........................
            ..........fffff.........
            ........ff1111bff.......
            .......fb1111111bf......
            .......f111111111f......
            ......fd1111111ffff.....
            ......fd111dd1c111bf....
            ......fb11fcdf1b1bff....
            ......f11111bfbfbff.....
            ......f1b1bdfcffff......
            ......fbfbfcfcccf.......
            ......ffffffffff........
            .........ffffff.........
            .........ffffff.........
            .........fffffff..f.....
            ..........fffffffff.....
            ...........fffffff......
            ........................
            ........................
            ........................
            ........................
            """),
        img("""
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f1111111dbf......
            ......fd1111111ddf......
            ......fd111111dddf......
            ......fd111ddddddf......
            ......fd111ddddddf......
            ......fd1dddddddbf......
            ......fd1dfbddbbff......
            ......fbddfcdbbcf.......
            .....ffffccddbfff.......
            ....fcb1bbbfcffff.......
            ....f1b1dcffffffff......
            ....fdfdf..ffffffffff...
            .....f.f.....ffffff.....
            ........................
            ........................
            ........................
            ........................
            ........................
            """)],
    500,
    characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT))
statusbar2 = statusbars.create(20, 4, StatusBarKind.health)
statusbar2.attach_to_sprite(mySprite7)
statusbar2.follow(mySprite7)

def on_forever():
    global statusbar
    music.play(music.create_song(assets.song("""
            Safe
            """)),
        music.PlaybackMode.UNTIL_DONE)
    statusbar = statusbars.create(20, 7, StatusBarKind.health)
    statusbar.set_label("HP")
    statusbar.attach_to_sprite(mySprite)
    statusbar.set_color(7, 7, 2)
    statusbar.follow(mySprite)
    characterAnimations.set_character_animations_enabled(mySprite, True)
forever(on_forever)
