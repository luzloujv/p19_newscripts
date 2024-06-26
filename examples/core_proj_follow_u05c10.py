from starter2 import *
import xtra_energy
import data_locations as dl
import loop_tools
reload(dl)

reload(looper)
reload(loop_apps)
reload(loop_tools)

if 'this_simname' not in dir():
    this_simname = 'u05'

output_base = "%s_cores"%this_simname
core_list =  [10]
frame_list = list(range(1,121))+[125]
fields = []# ['x','y','z','density']
derived = []

if 'this_looper' not in dir():
    this_looper = looper.core_looper(directory= dl.sims[this_simname],
                                     sim_name = this_simname,
                                     out_prefix = this_simname,
                                     target_frame = dl.target_frames[this_simname],
                                     frame_list = frame_list,
                                     core_list =  core_list,
                                     fields_from_grid=fields,
                                     derived = derived
                                  )
    this_looper.plot_directory = "/home/dccollins/PigPen"
    this_looper.get_target_indices(h5_name=dl.peak_list[this_simname],
                                     bad_particle_list=dl.bad_particles.get(this_simname,None))
    this_looper.get_tracks()
    #this_looper.make_snapshots()

loop_apps.core_proj_follow(this_looper,axis_list=[0], 
                           zoom=False, grids=False, particles=False, moving_center=True, frame_list=[1])
