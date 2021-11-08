from game import constants
from game.point import Point
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
        
    Attributes:
    """

    def __init__(self):
        """HandleCollisionsAction class constructor        
        Args:
            self -  Instance of HandleCOllisionAction
        """

    def execute(self, cast):
        """Executes the action using the given actors.  
        * Ball colliding with the paddle, bricks or edges of the screen
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        paddle = cast["paddle"][0] # only one instance        
        balls = cast["ball"]
        score = cast["score"][0] # only one instance
        bricks = cast["brick"]
        message = cast["message"][0]

        live_ball_count = cast["live-ball-count"][0]

        for ball in balls:

            ball_position = ball.get_position()
            ball_x = ball_position.get_x()
            ball_y = ball_position.get_y()

            paddle_position = paddle.get_position()
            paddle_x_start = paddle_position.get_x()
            paddle_x_end = paddle_x_start + constants.PADDLE_LENGTH

            # IMMINENT BALL on PADDLE collision            
            # for a more realistic bounce, it should bounce before collision and never overlap                     

            if ball_x in range (paddle_x_start,paddle_x_end) and ball_y == constants.PADDLE_Y_LEVEL - 1:
                ball.bounce("up")

            # make ball bounce off the top of the screen
            elif ball_y in [0,1]:
                ball.bounce("down")

            # make ball bounce off the left and right edges of the screen
            elif ball_x in [0,1]:
                ball.bounce("down-right")

            elif ball_x in [constants.MAX_X-1, constants.MAX_X]:
                ball.bounce("down-left")

            # kill balls that hit the kill zone, or bounce them if in Zen Mode
            elif ball.get_text() != "x" and ball_y >= constants.GAME_OVER_Y:
                
                if not constants.ZEN_MODE:
                    ball.set_velocity(Point(0,0))
                    ball.set_text("x")
                    
                    live_ball_count.count = live_ball_count.count - 1
                    if live_ball_count.count == 0:
                        message.lose()
                else:
                    ball.bounce("up")

            else:
                # BALL on BRICK collision
                for brick in bricks:
                    brick_position = brick.get_position()
                    if ball_position.equals(brick_position):
                            
                        # add points
                        score.add_points(1)
                        score.refresh()

                        # make ball bounce
                        ball.bounce()

                        # destroy brick
                        cast['brick'].remove(brick)
                        
                        current_score = score.get_score()
                        if current_score == 280:
                            message.win()
                        
                        break






 

 
