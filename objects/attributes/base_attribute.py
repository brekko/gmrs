#!/usr/bin/python -u
# -*- coding: utf-8 -*-

""" base_attributes.py This is the base class for all attributes """

class BaseAttribute:
    description = ""
    name = ""
    value = 0
    min_value = -100
    max_value = 100
    enabled = True

    def __init__(self, att_value, att_name, att_description=""):
        self.value = att_value
        self.att_name = att_name
        self.description = att_description

    def set_value(self, att_value):
        if self.min_value <= att_value <= self.max_value:
            self.value = att_value

    def get_value(self):
        return self.value

    def set_min(self, new_value):
        if new_value>self.max_value:
            self.min_value = new_value
            if self.min_value>self.value:
                self.value = self.min_value
        else:
            raise ValueError("Min value must be less then or equal to max value.")

    def set_max(self, new_value):
        if new_value<self.min_value:
            self.max_value = new_value
            if self.max_value<self.value:
                self.value = self.max_value
        else:
            raise ValueError("Max value must be greater then or equal to min value.")

    def inc(self, step):
        if self.value+step<=self.max_value:
            self.value = self.value+step
        else:
            self.value = self.max_value

    def dec(self, step):
        if self.value-step>=self.min_value:
            self.value = self.value-step
        else:
            self.value = self.min_value
