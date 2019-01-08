"""
  Enum to represent the temperature units that the
  user will be able to choose from in the command line. (Celcius and Fahrenheit)
"""

from enum import Enum

class BaseEnum(Enum):
  def _generate_next_value_(name, start, count, last_value):
    return name
