#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = transcript()
        t.grade1 = 90
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        t.final_grade = 99
        self.response.write("Tommy's final grade is " + str(t.final_grade))

        s = transcript()
        s.grade1 = 45
        s.grade2 = 80
        s.quiz1 = 66
        s.quiz2 = 76
        s.cal_grade()
        self.response.write("<br> Sally's final grade is " + str(s.final_grade))

class transcript(object):
    def __init__(self):
        self.grade1 = 0                 #Public
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self.__final_grade = 0          #Private

    @property
    def final_grade(self):
        return self.__final_grade

    @final_grade.setter
    def final_grade(self, new_final_grade):
        self.__final_grade = new_final_grade

    def cal_grade(self):
        self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam)/5



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
