#!/usr/bin/python -u
# -*- coding: utf-8 -*-

""" elemental_attributes.py This is the base class for elemental attributes """

from objects.attributes.base_attribute import BaseAttribute

class ElementalAttributes:
    fire_power = BaseAttribute(0, "Fire power", "")
    water_power = BaseAttribute(0, "Water power", "")
    earth_power = BaseAttribute(0, "Earth power", "")
    wind_power = BaseAttribute(0, "Wind power", "")
    light_power = BaseAttribute(0, "Light power", "")
    dark_power = BaseAttribute(0, "Dark power", "")

    fire_resistence = BaseAttribute(0, "Fire resistence", "")
    water_resistence = BaseAttribute(0, "Water resistence", "")
    earth_resistence = BaseAttribute(0, "Earth resistence", "")
    wind_resistence = BaseAttribute(0, "Wind resistence", "")
    light_resistence = BaseAttribute(0, "Light resistence", "")
    dark_resistence = BaseAttribute(0, "Dark resistence", "")

    def __add__(self, other):
        tempItem = ElementalAttributes()
        tempItem.fire_power = self.fire_power + other.fire_power
        tempItem.water_power = self.water_power + other.water_power
        tempItem.earth_power = self.earth_power + other.earth_power
        tempItem.wind_power = self.wind_power + other.wind_power
        tempItem.light_power = self.light_power + other.light_power
        tempItem.dark_power = self.dark_power + other.dark_power
        tempItem.fire_resistence = self.fire_resistence + other.fire_resistence
        tempItem.water_resistence = self.water_resistence + other.water_resistence
        tempItem.earth_resistence = self.earth_resistence + other.earth_resistence
        tempItem.wind_resistence = self.wind_resistence + other.wind_resistence
        tempItem.light_resistence = self.light_resistence + other.light_resistence
        tempItem.dark_resistence = self.dark_resistence + other.dark_resistence
        return tempItem

    def __sub__(self, other):
        tempItem = ElementalAttributes()
        tempItem.fire_power = self.fire_power - other.fire_power
        tempItem.water_power = self.water_power - other.water_power
        tempItem.earth_power = self.earth_power - other.earth_power
        tempItem.wind_power = self.wind_power - other.wind_power
        tempItem.light_power = self.light_power - other.light_power
        tempItem.dark_power = self.dark_power - other.dark_power
        tempItem.fire_resistence = self.fire_resistence - other.fire_resistence
        tempItem.water_resistence = self.water_resistence - other.water_resistence
        tempItem.earth_resistence = self.earth_resistence - other.earth_resistence
        tempItem.wind_resistence = self.wind_resistence - other.wind_resistence
        tempItem.light_resistence = self.light_resistence - other.light_resistence
        tempItem.dark_resistence = self.dark_resistence - other.dark_resistence
        return tempItem

