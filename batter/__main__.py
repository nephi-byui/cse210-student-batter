import random
from game import constants
from game.director import Director
from game.actor import Actor, Ball
from game.score import Score
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    # paddle
    paddle = Actor()
    cast["paddle"] = [paddle]

    x = int(constants.MAX_X / 2)
    y = int(constants.PADDLE_Y_LEVEL)
    position = Point(x, y)    
    paddle.set_text("=" * constants.PADDLE_LENGTH)
    paddle.set_position(position)
    

    # bricks
    cast["brick"] = []
    for x in range(5, 75):
        for y in range(2, 6):
            position = Point(x, y)
            brick = Actor()
            brick.set_text("*")
            brick.set_position(position)
            cast["brick"].append(brick)

    # ball
    ball = Ball()
    cast["ball"] = [ball]

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity = Point(1, -1)
    
    ball.set_text("O")
    ball.set_position(position)
    ball.set_velocity(velocity)
  

    # score object
    score = Score()
    cast["score"] = [score]
    x = 1
    y = 0
    position = Point(x, y)
    score.score = 0
    score.set_position(position)
    score.set_text(f"Score: {score.score}")

    # walls
    wall = Actor()
    cast["wall"] = [wall]
    x = 0
    y = 1
    position = Point(x, y)
    wall.set_position(position)
    wall.set_text("" * constants.MAX_X)

    
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_acition]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)