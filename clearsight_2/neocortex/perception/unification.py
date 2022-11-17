# Uses Entity-Action-Event and Space-Timeline-Universe (EAE-STU) syntax to understand the real world

# Timeline
#  -> Events
#      -> Entities, Actions

class Timeline:
    def __init__(self, *events):
        self.events = events

class Entity:
    def __init__(self, parent=None, **properties):
        self.properties = properties
        self.parent = parent

    def daughter(self, **propertiesOverride):
        newProperties = self.properties
        for propName in propertiesOverride.keys():
            newProperties[propName] = propertiesOverride[propName]
        return Entity(self, **newProperties)

class Action:
    def __init__(self, parent, actor=None, target=None, *verbs, **effects):
        self.actor = actor
        self.target = target
        self.verbs = verbs
        self.parent = parent
        self.effects = effects

    def enact(self, *effectBlacklist):
        for effect in self.effects.keys():
            if effect in self.target.properties.keys():
                self.target.properties[effect]

class Event:
    def __init__(self, actors, actions, targets, time, **properties):
        self.actors = actors
        self.actions = actions
        self.targets = targets
        self.properties = properties
        self.time = time