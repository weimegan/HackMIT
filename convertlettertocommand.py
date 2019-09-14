#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:14:38 2019

@author: isabellequaye
"""

draw_letter = {}
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

