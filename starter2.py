
#
# ALl the other things that aren't standard python packages.
#

from starter1 import *
#so we can import things from sub directories
path_list= ["./tools_data", "./tools_pdf", "./testing",\
            "./tools", "./tools_tracks", "./trash"]
for directory in path_list:
    if directory not in sys.path:
        sys.path += [directory]

import yt

import data_locations as dl

import pyximport
pyximport.install(setup_args={'include_dirs': np.get_include()})
import particle_ops as particle_ops
import particle_grid_mask as particle_grid_mask

import looper
reload(looper)

import trackage
reload(trackage)
import tracks_read_write as trw
reload(trw)
from davetools import *
import loop_apps
reload(loop_apps)



