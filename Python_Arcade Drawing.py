"""
enter pip install arcade in command prompt to install the arcade package
video walkthrough https://vimeo.com/16729602

or for windows use comand py -m pip install arcade
"""

#library imports
import arcade

#constants - variables that don't change - set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_background():
    """
    This function draws the background, specifically the sky and ground
    """
    #draw the sky in the top two-thirds
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      SCREEN_HEIGHT * (1/3),
                                      arcade.color.SKY_BLUE)

    #draw the ground in the bottom third
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT / 3,
                                      0,
                                      arcade.color.DARK_SPRING_GREEN)

def draw_bird(x,y):
    """
    draw a bird using a couple of arcs
    """
    arcade.draw_arc_outline(x,y,20,20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 40, y, 20, 20, arcade.color.BLACK, 90, 180)

def draw_sun(x,y):
    arcade.draw_circle_filled(x + 600, y + 140, 18, arcade.color.YELLOW)

def draw_pine_tree(x,y):
    """
    this function draws a pine tree at the specified location
    """
    #draw the second triangle on top of the triangle below
    arcade.draw_triangle_filled(x + 40, y + 80,
                                x, y - 40,
                                x + 80, y - 40,
                                arcade.color.DARK_GREEN)
    
    #draw the triangle on top of the trunk
    arcade.draw_triangle_filled(x + 40, y,
                                x, y - 100,
                                x + 80, y - 100,
                                arcade.color.DARK_GREEN)

    #draw the trunk
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)

def main():
    """
    this is the main program
    """

    #open the  window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Draw with Functions")

    #start the render  process. this must be done before any drawing commands
    arcade.start_render()

    #call our drawing functions
    draw_background()
    draw_pine_tree(50, 250)
    draw_pine_tree(350,320)
    draw_pine_tree(550,250)
    draw_bird(70, 500)
    draw_bird(470, 550)
    draw_sun(100, 400)

    #finish the render
    #nothing will be drawn without this
    #must happen after all draw commands
    arcade.finish_render()

    #keep the window up until someone closes it
    arcade.run()
"""
if _name_ == "_main_":
    main()
 """

main()
