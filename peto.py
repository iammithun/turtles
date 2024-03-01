# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:17:03 2024

@author: iamrs
"""

import turtle


pen = turtle.Turtle()

def draw_pentagon():
    for _ in range(5):
        pen.forward(100)  
        pen.right(72)


pen.speed(1)

draw_pentagon()

turtle.mainloop()

