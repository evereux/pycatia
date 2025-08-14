#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.general_knowledge_interfaces.expert_report_object import ExpertReportObject
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class ExpertReportObjects(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     ExpertReportObjects
                | 
                | Represents the collection of (succeeded or failed) report
                | objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ExpertReportObject)
        self.expert_report_objects = com_object

    @property
    def count_fail(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CountFail() As long (Read Only)
                | 
                |     Returns the number of failed tuples in the failed tuples collection. It is
                |     redundant with Collection.Count for ExpertCheckRuntime.Failures collection. For
                |     ExpertCheckRuntime.Succeeds collection, it will fail.
                | 
                |     Example:
                |         This example retrieves in ObjectNumber the number of tuples currently
                |         gathered in MyCollection.
                | 
                |          ObjectNumber = MyCollection.CountFail

        :rtype: int
        """

        return self.expert_report_objects.CountFail

    @property
    def count_succeed(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CountSucceed() As long (Read Only)
                | 
                |     Returns the number of succeeded tuples in the succeeded tuples collection.
                |     It is redundant with Collection.Count for ExpertCheckRuntime.Succeeds
                |     collection. For ExpertCheckRuntime.Failures collection, it will
                |     fail.
                | 
                |     Example:
                |         This example retrieves in ObjectNumber the number of tuples currently
                |         gathered in MyCollection.
                | 
                |          ObjectNumber = MyCollection.CountSucceed

        :rtype: int
        """

        return self.expert_report_objects.CountSucceed

    def fail_item(self, i_index: cat_variant) -> ExpertReportObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func FailItem(CATVariant iIndex) As ExpertReportObject
                | 
                |     Retrieves a report failed component from a failed tuples collection, using
                |     its index or its name from the Check collection. It is redundant with
                |     ExpertReportObjects.Item for ExpertCheckRuntime.Failures collections. For
                |     ExpertCheckRuntime.Succeeds collections, it will fail.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Report component to retrieve from the
                |             collection of Report Components. As a numerics, this index is the rank of the
                |             Report component in the collection. The index of the first component in the
                |             collection is 1, and the index of the last component is Count. As a string, it
                |             is the name you assigned to the component using the
                |             
                | 
                |         AnyObject.Name property or when creating the component.
                |         
                |     Returns:
                |         The retrieved Report component

        :param cat_variant i_index:
        :rtype: ExpertReportObject
        """
        return ExpertReportObject(self.expert_report_objects.FailItem(i_index))

    def item(self, i_index: cat_variant) -> ExpertReportObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As ExpertReportObject
                | 
                |     Retrieves a Report component using its index or its name from the Check
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                | 
                |             The index or the name of the Report component to retrieve from the
                |             collection of Report Components. As a numerics, this index is the rank of the
                |             Report component in the collection. The index of the first component in the
                |             collection is 1, and the index of the last component is Count. As a string, it
                |             is the name you assigned to the component using the
                |             
                | 
                |         AnyObject.Name property or when creating the
                |         component.
                | 
                |     Returns:
                |         The retrieved Report component

        :param cat_variant i_index:
        :rtype: ExpertReportObject
        """
        return ExpertReportObject(self.expert_report_objects.Item(i_index))

    def succeed_item(self, i_index: cat_variant) -> ExpertReportObject:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func SucceedItem(CATVariant iIndex) As ExpertReportObject
                | 
                |     Retrieves a report component from a succeeded tuples collection, using its
                |     index or its name from the Check collection. It is redundant with
                |     ExpertReportObjects.Item for ExpertCheckRuntime.Succeeds collections. For
                |     ExpertCheckRuntime.Failures collections, it will fail.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Report component to retrieve from the
                |             collection of Report Components. As a numerics, this index is the rank of the
                |             Report component in the collection. The index of the first component in the
                |             collection is 1, and the index of the last component is Count. As a string, it
                |             is the name you assigned to the component using the AnyObject.Name property
                |             or when creating the component.
                |         
                |     Returns:
                |         The retrieved Report component

        :param cat_variant i_index:
        :rtype: ExpertReportObject
        """
        return ExpertReportObject(self.expert_report_objects.SucceedItem(i_index))

    def __repr__(self):
        return f'ExpertReportObjects(name="{self.name}")'
