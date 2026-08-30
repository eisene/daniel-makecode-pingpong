let mySprite = sprites.create(img`
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    . . . . . . 2 2 2 . . . . . . . 
    `, SpriteKind.Player)
let enemysprite = sprites.create(img`
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    . . . . . . 8 8 8 . . . . . . . 
    `, SpriteKind.Enemy)
let ball = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . 1 1 1 . . . . . . . . 
    . . . . 1 1 1 1 1 . . . . . . . 
    . . . . 1 1 1 1 1 . . . . . . . 
    . . . . 1 1 1 1 1 . . . . . . . 
    . . . . . 1 1 1 . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Projectile)
mySprite.setPosition(10, 60)
enemysprite.setPosition(150, 60)
mySprite.setStayInScreen(true)
enemysprite.setStayInScreen(true)
ball.setBounceOnWall(true)
info.setScore(0)
let enemyscore = 0
let direction = randint(1, 2)
let gone = false
forever(function () {
    if (controller.down.isPressed()) {
        mySprite.y += 2
    } else if (controller.up.isPressed()) {
        mySprite.y += -2
    }
})
forever(function () {
    if (direction == 1 && gone == false) {
        gone = true
        ball.setVelocity(50, randint(50, -50))
    } else if (direction == 2 && gone == false) {
        gone = true
        ball.setVelocity(50, randint(50, -50))
    }
})
forever(function () {
    if ((mySprite.overlapsWith(ball) || enemysprite.overlapsWith(ball)) && direction == 1) {
        direction = 2
        pause(500)
    } else if ((mySprite.overlapsWith(ball) || enemyscore.overlapsWith(ball)) && direction == 2) {
        direction = 1
        pause(500)
    }
})
