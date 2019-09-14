#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:14:38 2019

@author: isabellequaye
"""

def straight_bar():
    return "U2D4U2"

def right_bar():
    return "R2"

def left_bar():
    return "L2"

def C_shell():
    return "U2D4U4" + right_bar() + left_bar() + "D4" + right_bar() + left_bar() + "U2"

def L_shell():
    return "U2D4" + right_bar() + left_bar() + "U2"

def upsidedownL_shell():
    return "D2U4" + right_bar() + left_bar() + "D2"

def forth_back():
    return right_bar() + left_bar()

def back_forth():
    return left_bar() + right_bar()
def up_down(x,y):
    return "U"+ str(x) + "D" + str(y)
def down_up(x,y):
    return "D"+ str(x) + "U" + str(y)

def display_commands(inp):
    out = []
    for i in inp.upper():
        out += [draw_letter[i][j:j+2] for j in range(0, len(draw_letter[i])-2,2)]
    return out

draw_letter = {" ": right_bar() + right_bar(), "A": upsidedownL_shell() + right_bar() + straight_bar(), "B": C_shell() + right_bar() + straight_bar(), "C": C_shell(), "D": "D2" + left_bar() + "U2" + right_bar() + "U2D2", "E": C_shell() + right_bar(), "F": upsidedownL_shell() + right_bar(), "G": C_shell() + "D2" + right_bar() + "U2L1R1D2" + left_bar() + "U2", "H": straight_bar() + right_bar() + straight_bar(), "I": straight_bar(), "J": "D2" + right_bar() + "U4D2", "K": straight_bar() + "R1U2D2R1D2U2" + left_bar(), "L": L_shell(), "M": straight_bar() + "U2" + right_bar() + "D3U3" + right_bar() + "D4U2"}
draw_letter["N"] = straight_bar() +  "U2" + right_bar() + "D4U2"
draw_letter["O"] = draw_letter["N"] + "D2"+ back_forth() + "U2"
draw_letter["P"] = upsidedownL_shell() + right_bar() + "U2" + "D2"
draw_letter["Q"] = draw_letter["O"] + "D2L1U2D4U2R1U2"
draw_letter["R"] = draw_letter["P"] + "L1D2U2R1"
draw_letter["S"] = "U2" + forth_back() + "D2" + right_bar() + "D2" + back_forth() + "U2"
draw_letter["T"] = straight_bar() + "U2L1R2L1D2"
draw_letter["U"] = "U2D4" + right_bar() + "U4D2"
draw_letter["V"] = "U2D4R1U4D2"
draw_letter["W"] = draw_letter["U"]+ draw_letter["U"]
draw_letter["X"] = right_bar() + down_up(2,2) + left_bar() + up_down(2,2) + right_bar() + up_down(2,2) + left_bar() + down_up(2,2) + right_bar()
draw_letter["Y"] = up_down(2,2) + right_bar() + up_down(2,4) + "U2"
draw_letter["Z"] = right_bar() + "U2" + back_forth() + "D2" + left_bar() + "D2" + forth_back() + "U2R2"

print(display_commands("yeet"))