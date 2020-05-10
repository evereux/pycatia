#! /usr/bin/python3.7
from pywintypes import com_error
from pycatia.exception_handling import CATIAApplicationException
from pycatia.knowledge_interfaces import parameterset


class ParameterSets:
    def __init__(self, parametersets):
        self.parametersets = parametersets

    @property
    def name(self):
        return self.parametersets.Name

    def count(self):
        return self.parametersets.Count

    def create_new_set(self, set_name):
        return self.parametersets.CreateSet(set_name)

    def is_item(self, index):
        """

        :param str/int index: parametersets name or parameter number
        :return: bool
        """
        try:
            if self.parametersets.Item(index):
                return True
        except com_error:
            return False

    def get_item_by_index(self, index):
        """

        :param str/int index: parametersets name or parameter number
        :return: item
        """
        if not self.is_item(index):
            raise CATIAApplicationException(f'Could not find parameter name "{index}".')

        return parameterset.ParameterSet(self.parametersets.Item(index))

    def get_items(self):
        """
        :return: list(Parameter())
        """
        sets = []

        for i in range(self.parametersets.Count):
            set = parameterset.ParameterSet(self.parametersets.Item(i + 1))
            sets.append(set)

        return sets

    def get_item_names(self):
        """
        :return: list
        """

        names = []

        for i in range(self.parametersets.Count):
            name = self.parametersets.Item(i + 1).name
            names.append(name)

        return names
