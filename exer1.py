"""
To confirm that your landsat_helpers module works
correctly, this script must print the following output

Scene 1: {'path': '116', 'year': '2015', 'day': '249', 'row': '046'}
Scene 2: {'path': '220', 'year': '2015', 'day': '225', 'row': '194'}
Scene 3: {'path': '117', 'year': '2015', 'day': '016', 'row': '048'}
"""

import landsat_helpers

scene1 = 'LC81160462015249LGN00'
scene2 = 'LC82201942015225LGN00'
scene3 = 'LC81170482015016LGN00'

print "Scene 1: %s" % landsat_helpers.get_scene_details(scene1)
print "Scene 2: %s" % landsat_helpers.get_scene_details(scene2)
print "Scene 3: %s" % landsat_helpers.get_scene_details(scene3)
