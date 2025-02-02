"""Anonymizer module."""

from abc import ABC, abstractmethod


class BaseAnonymizer(ABC):
    """Base Anonymizer."""

    @abstractmethod
    def anonymize(self, text):
        """
        :param str text: Data that must be anonymized
        """
