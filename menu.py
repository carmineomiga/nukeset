import nuke

tb = nuke.toolbar("Nodes")
m = tb.addMenu("Omiga", icon="icon_O.png")
m.addMenu("Draw")
m.addCommand("Draw/timecode_burnin", "nuke.createNode('timecode_burnin')")