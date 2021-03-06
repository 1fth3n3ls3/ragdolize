# -*- coding: utf-8 -*-
"""This module has the utils for particles visualization in maya

MIT License

Copyright (c) 2020 Mauro Lopez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFT
"""
from maya import cmds
from maya.api import OpenMaya as om

class Body(object):
    """maya particle representation 
    """
    def __init__(self, name, position=None, rotation=None):
        self.name = name
        self.setup()
        if position:
            cmds.xform(self.name, ws=1, t=position)
        if rotation:
            cmds.xform(self.name, ws=1, ro=rotation)
        self._position = cmds.xform(self.name, q=1, ws=1, t=1)
        self._rotation = cmds.xform(self.name, q=1, ws=1, ro=1)
        self._matrix = cmds.xform(self.name, q=1, ws=1, m=1)

    def setup(self):
        """to be overweitten by the instances
        """
        pass

    @property
    def position(self):
        self._position = cmds.xform(self.name, q=1, ws=1, t=1)
        return self._position

    @position.setter
    def position(self, pos):
        self._position = om.MVector(pos)
        cmds.xform(self.name, ws=1, t=pos)

    @property
    def rotation(self):
        self._rotation = cmds.xform(self.name, q=1, ws=1, ro=1)
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        self._rotation = om.MVector(rotation)
        cmds.xform(self.name, ws=1, ro=rotation)

    @property
    def matrix(self):
        self._matrix = cmds.xform(self.name, q=1, ws=1, m=1)
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        cmds.xform(self.name, ws=1, m=matrix)


class Sphere(Body):
    """represent a particles as a polySphere
    """
    def __init__(self, name, position, radius=0.1):
        self.radius = radius
        super(Sphere, self).__init__(name, position)


    def setup(self):
        if cmds.objExists(self.name):
            return self.name
        self.name = cmds.polySphere(radius=self.radius, n=self.name)[0]
        return self.name


class Cube(Body):
    """represent a particles as a polyCube
    """
    def __init__(self, name, position, radius=0.2):
        self.radius = radius
        super(Cube, self).__init__(name, position)


    def setup(self):
        if cmds.objExists(self.name):
            return self.name
        self.name = cmds.polyCube(w=self.radius, h=self.radius, d=self.radius, n=self.name)[0]
        return self.name



class Segment(Body):
    def __init__(self, position, radius, length):
        super(Segment, self).__init__(position, radius)
        self.length = length
