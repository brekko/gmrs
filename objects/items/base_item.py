#!/usr/bin/python -u
# -*- coding: utf-8 -*-

""" base_item.py This is the base class for all items """

from objects.attributes.base_attribute import BaseAttribute
from objects.attributes.elemental_attributes import ElementalAttributes

class BaseItem:
    description = ""
    name = ""

    health = BaseAttribute(0, "Health")
    mana = BaseAttribute(0, "Mana")
    energy = BaseAttribute(0, "Energy")
    rage = BaseAttribute(0, "Rage")
    attack = BaseAttribute(0, "Attack")
    defence = BaseAttribute(0, "Defence")
    crit_chance = BaseAttribute(0, "Crit. chance")
    crit_dodge = BaseAttribute(0, "Crit. dodge")
    crit_power = BaseAttribute(0, "Crit. power")
    crit_defence = BaseAttribute(0, "Crit. defence")
    attack_speed = BaseAttribute(0, "Attack speed")
    movement_speed = BaseAttribute(0, "Movement speed")
    healing_bonus = BaseAttribute(0, "Healing bonus")

    elemental_attributes = ElementalAttributes()

    sub_items = []

    def __init__(self, item_description):
        self.description = item_description

    def __add__(self, other):
        tempItem = BaseItem()
        tempItem.health = self.health + other.health
        tempItem.mana = self.mana + other.mana
        tempItem.energy = self.energy + other.energy
        tempItem.rage = self.rage + other.rage
        tempItem.attack = self.attack + other.attack
        tempItem.defence = self.defence + other.defence
        tempItem.crit_chance = self.crit_chance + other.crit_chance
        tempItem.crit_dodge = self.crit_dodge + other.crit_dodge
        tempItem.crit_power = self.crit_power + other.crit_power
        tempItem.crit_defence = self.crit_defence + other.crit_defence
        tempItem.attack_speed = self.attack_speed + other.attack_speed
        tempItem.movement_speed = self.movement_speed + other.movement_speed
        tempItem.healing_bonus = self.healing_bonus + other.healing_bonus
        tempItem.elemental_attributes = self.elemental_attributes + other.elemental_attributes
        return tempItem

    def __sub__(self, other):
        tempItem = BaseItem()
        tempItem.health = self.health - other.health
        tempItem.mana = self.mana - other.mana
        tempItem.energy = self.energy - other.energy
        tempItem.rage = self.rage - other.rage
        tempItem.attack = self.attack - other.attack
        tempItem.defence = self.defence - other.defence
        tempItem.crit_chance = self.crit_chance - other.crit_chance
        tempItem.crit_dodge = self.crit_dodge - other.crit_dodge
        tempItem.crit_power = self.crit_power - other.crit_power
        tempItem.crit_defence = self.crit_defence - other.crit_defence
        tempItem.attack_speed = self.attack_speed - other.attack_speed
        tempItem.movement_speed = self.movement_speed - other.movement_speed
        tempItem.healing_bonus = self.healing_bonus - other.healing_bonus
        tempItem.elemental_attributes = self.elemental_attributes - other.elemental_attributes
        return tempItem

    def globalsum(self, list_subitems):
        tempItem = BaseItem()
        for each_item in list_subitems:
            tempItem = tempItem + self.globalsum(each_item);
        return tempItem

    def GetGlobalAttributes(self):
        tempItem = BaseItem()

        tempItem = tempItem + self.globalsum(self.sub_items)

        return tempItem