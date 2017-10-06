#!/usr/bin/python -u
# -*- coding: utf-8 -*-

""" base_character.py This is the base class for all items """

from objects.attributes.gender import Gender

class BaseCharacter:
    description = ""
    name = ""
    age = 0
    gender = Gender.UNDEFINED

    body_slots = {}

    def add_slot(self, slot_name, item=None):
        self.body_slots[slot_name] = item

    def remove_slot(self, slot_name):
        del self.body_slots[slot_name]


