# Copyright 2020 D-Wave Systems Inc.
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
import dwavebinarycsp


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # coordinate labels for groups red, green, and blue
        label = "{0},{1}_".format(x, y)
        self.g1 = label + "r"
        self.g2 = label + "g"
        self.g3 = label + "b"


def main:
    # Set up problem
    coordinates = [(0, 0), (1, 1), (2, 4), (3, 2)]

    # Build constraints
    csp = dwavebinarycsp.ConstraintSatisfactionProblem()

    # Apply constraint: node can only be in one group
    choose_one_group = {(0, 0, 1), (0, 1, 0), (1, 0, 0)}
    csp.add_constraint()

    # Apply constraint: nodes in the same group share an edge

    # Bias for short edges

    # Submit problem to solver

    # Visualize problem

