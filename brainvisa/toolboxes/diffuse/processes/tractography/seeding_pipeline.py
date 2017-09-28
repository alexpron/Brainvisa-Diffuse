
from brainvisa.processes import *
from copy import copy



userLevel = 2
name = 'Seeding Pipeline'


signature = Signature()




def initialization(self):

    #Pipeline GRAPH
    eNode = SelectionExecutionNode(self.name, parameterized=self)

    eNode.addChild('SeedsFromMesh',
                   ProcessExecutionNode('seeds_from_mesh', selected=True))
    eNode.addChild('RVolumicSeeds',
                   ProcessExecutionNode('random_seeds_from_mask', selected=False))
    eNode.addChild('VolumicSeeds',
                   ProcessExecutionNode('seeds_from_mask', selected=False))

    self.setExecutionNode(eNode)



