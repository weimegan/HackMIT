#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:14:38 2019

@author: isabellequaye
"""

draw_letter = {" ": , "A": upsidedownL_shell() + right_bar() + straight_bar(), "B": C_shell() + right_bar() + straight_bar(), "C": C_shell(), "D": , "E": C_shell() + right_bar(), "F": upsidedownL_shell() + right_bar(), "G": C_shell() + "D2" + right_bar() + "U2" + "L1" + "R1" + "D2" + left_bar() + "U2", "H": straight_bar() + right_bar() + straight_bar(), "I": straight_bar(), "J": , "K": straight_bar() + "R1" + "U2" + "D2" + "R1" + "D2" + "U2" + left_bar(), "L": L_shell(), "M": ,}
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

