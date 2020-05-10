#! /usr/bin/python3.6

from pywintypes import com_error
from pycatia.exception_handling import CATIAApplicationException
from pycatia.knowledge_interfaces import parameterset


class ParameterSets:
    def __init__(self, parameter_sets):
        self.parameter_sets = parameter_sets

    @property
    def name(self):
        return self.parameter_sets.Name

    def count(self):
        return self.parameter_sets.Count

    def create_new_set(self, set_name):
        return self.parameter_sets.CreateSet(set_name)

    def is_item(self, index):
        """

        :param str/int index: parametersets name or parameter number
        :return: bool
        """
        try:
            if self.parameter_sets.Item(index):
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

        return parameterset.ParameterSet(self.parameter_sets.Item(index))

    def get_items(self):
        """
        :return: list(Parameter())
        """
        parm_sets = []

        for i in range(self.parameter_sets.Count):
            parm_set = parameterset.ParameterSet(self.parameter_sets.Item(i + 1))
            parm_sets.append(parm_set)

        return parm_sets

    def get_item_names(self):
        """
        :return: list
        """

        names = []

        for i in range(self.parameter_sets.Count):
            name = self.parameter_sets.Item(i + 1).name
            names.append(name)

        return names
