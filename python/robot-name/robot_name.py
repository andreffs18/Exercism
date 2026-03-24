from random import sample
from string import ascii_uppercase, digits
from typing import Optional


class Robot(object):
    """A Robot with a randomly generated unique name.

    Each robot has a name following the pattern of two uppercase letters
    followed by three digits (e.g., 'AB123', 'XY789').
    """

    name: Optional[str] = None

    def __init__(self) -> None:
        """
        Initialize a new Robot with a randomly generated name.
        """
        self.reset()

    def reset(self) -> None:
        """
        Reset the robot to factory settings, generating a new random name.

        This method wipes the robot's name and assigns a new unique one.
        """
        self.name = self._generate_new_name()

    def _generate_new_name(self) -> str:
        """
        Generate a new unique robot name.

        Creates a name with the format: 2 uppercase letters + 3 digits.
        Ensures the new name is different from the current name.

        Returns:
            str: A new unique robot name (e.g., 'AB123').
        """
        letters = "".join(sample(ascii_uppercase, 2))
        numbers = "".join(sample(digits, 3))
        new_name = "{}{}".format(letters, numbers)

        if not self.name:
            return new_name

        if self.name == new_name:
            return self._generate_new_name()

        return new_name
