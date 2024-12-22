# -*- coding: utf-8 -*-
from generator.project import random_string
from model.project import Project

testdata = [Project(name=random_string("=name1=", 10),
                    description=random_string("=description1 =", 10))]

