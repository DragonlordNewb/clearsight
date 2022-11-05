
# "Any sufficiently advanced technology is indistinguishable from magic."
#  - Arthur C. Clarke

# "Magic is just technology that most people don't immediately understand.
#  It's not magic, we just can't tell the difference."
#  - Lux Bodell

# Copyright 2022-2023 Lux Bodell.
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

import math

# The Timeline object represents the organization of events over a linear
# function of time. In other words, it represents the flow of time as an object
# containing events which alter the properties of Entities. It's bound to
# exactly one Spacefield.
class Timeline:
    def __init__(self, *events):
        self.events = events
        self.entities = []

# The Event object represents a literal event at a certain point in time that
# alters the properties of Entities. It is bound to one or more Timelines, and
# it alters the properties of Entities in that Timeline.
class Event:
    def __init__(self, space, time, radius, **propertyChanges):
        # The propertyChanges argument represents a dictionary, where the keys
        # are the keys of properties of Entities that are affected by this
        # Event, and the values are functions that correspond to the changes
        # incurred by the Event on those properties.

        self.propertyChanges = propertyChanges

        # Ensure that the space argument was a Spacefield
        if isinstance(space, Spacefield):
            self.space = space
        else:
            raise TypeError("invalid argument for Universe; space must be a Spacefield, not a " + str(space.__name__))

        # Ensure that the time argument was a Timeline
        if isinstance(time, Timeline):
            self.time = time
        else:
            raise TypeError("invalid argument for Universe; time must be a Timeline, not a " + str(time.__name__))

        self.time.events.append(self)

# The MasterPoint object is an object that can represent a point of arbitrary
# dimensions. Used only internally.
class MasterPoint:
    def __init__(self, *coordinates, parentSpacefield=None):
        self.dimension = len(coordinates)
        self.coordinates = dimensions
        self.parentSpacefield = parentSpacefield
        if self.dimension != self.parentSpacefield.dimension:
            raise ValueError("invalid dimension of point; must match parent Spacefield dimension")

# The Spacefield object represents an infinite n-dimensional space with the
# metric (R^n, d) where d is the standard distance formula in Euclidean space.
# It represents the spacial organization of Entities in a Universe. It's bound
# to exactly one Timeline.
class Spacefield:
    def __init__(self, dimension):
        self.dimension = dimension
        self.points = []
        self.locations = []

    def point(self, *coordinates):
        newPoint = MasterPoint(*coordinates, self)
        self.points.append(newPoint)
        return newPoint

    def distance(self, point1, point2):
        return math.sqrt(sum([
            (point2.coordinates[n] - point1.coordinates[n]) ** 2 for n in range(len(point1.coordinates))
            ]))

# The Location object represents a finite location in a Spacefield that can
# have certain properties bound to it. It can be altered by Events as well.
class Location:
    def __init__(self, parentSpacefield, *coordinates, **properties):
        self.space = parentSpacefield
        self.space.locations.append(self)
        self.location = self.spacefield.point(*coordinates)
        self.properties = properties
        self.entities = []

# The Entity is an object bound to at exactly one Spacefield and Timeline and
# represents a real object with arbitrary properties that can be changed over
# the course of time by Events on the Timeline that it's bound to. Must be bound
# to a Universe.
class Entity:
    def __init__(self, universe, location, *events, **properties):
        self.properties = properties
        self.universe = universe
        self.space = self.universe.space
        self.time = self.universe.time
        self.location = location
        self.location.entities.append(self)
        self.id = "entity"

    def generateDaughter(self, newId, *events, **properties):
        # Inherit all properties from the parent
        newProperties = self.properties

        # Inherit properties from the function's arguments
        for key in properties.keys():
            newProperties[key] = properties[key]

        # Add events and properties to the new Entity and set its ID
        daughter = Entity(*events, **newProperties)
        daughter.id = newId

        # Return the daughter
        return daughter

# The Universe object represents a space-time unification that allows for the
# collection of Events and Entities together and representing those objects as
# a real model of a functional universe. May or may not represent an actual
# cosmos.
class Universe:
    def __init__(self, space, time, *entities):
        # Ensure that the space argument was a Spacefield
        if isinstance(space, Spacefield):
            self.space = space
        else:
            raise TypeError("invalid argument for Universe; space must be a Spacefield, not a " + str(space.__name__))

        # Ensure that the time argument was a Timeline
        if isinstance(time, Timeline):
            self.time = time
        else:
            raise TypeError("invalid argument for Universe; time must be a Timeline, not a " + str(time.__name__))

        # Ensure that everything supplied by the entities argument is an actual
        # entity.
        self.entities = []
        for entity in entities:
            if isinstance(entity, Entity):
                self.entities.append(entity)
            else:
                raise TypeError("invalid argument for Universe; *entities must be a list of Entities, not " + str(entity.__name__))


# The Multiverse object is a representation of a Multiverse, in the sense that
# it is a collection of Universes from which other Universes can be interpolated
# and extrapolated using different courses of events, specifically regarding
# alternate Universes in the most common sense of the term and the prediction of
# new outcomes from different initial conditions.
class Multiverse:
    def __init__(self, *universes):
        # Ensure that everything supplied in the *universes argument are all
        # Universes

        self.universes = []
        for universe in universes:
            if isinstance(universe, Universe):
                self.universes.append(universe)
            else:
                raise TypeError("invalid argument for Multiverse; *universes must be a list of Universes, not " + str(universe.__name__))
