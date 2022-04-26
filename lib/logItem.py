#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:刘海超
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author:刘海超

from mainGUI import levelIndex, tagIndex, dateIndex, positionIndex, messageIndex


class LogItem(object):
    def __init__(self, level, tag, date, position, message):
        self.level = level
        self.tag = tag
        self.date = date
        self.position = position
        self.message = message

    def getText(self, column):
        if column is levelIndex:
            return self.level
        elif column is tagIndex:
            return self.tag
        elif column is dateIndex:
            return self.date
        elif column is positionIndex:
            return self.position
        elif column is messageIndex:
            return self.message
