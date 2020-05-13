#! /usr/bin/python3.6


class BaseKnowledge:

    def __init__(self, com_object):
        self.com_object = com_object

    @property
    def comment(self):
        return self.com_object.Comment

    @comment.setter
    def comment(self, text):
        self.com_object.Comment = text

    @property
    def name(self):
        return self.com_object.Name

    @name.setter
    def name(self, text):
        self.com_object.Rename(text)
