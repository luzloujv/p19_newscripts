from starter2 import *
reload(track_info)


#
# Define tracks, including track location and build information.
# The constructor also registers each one in track_info.tracks
#

track_info.track('u601',
                 sim_directory=dl.sims['u201'],
                 target_frame = 125,
                 mountain_top = "datasets_small/u301_mountain_tops_take_9.h5",
                 peak_fname = 'datasets_small/u301_0125_peaklist.h5',
                 track_file = "%s/u600/u601_every_10_all_prim.h5"%dl.coresets['ourset'],
                 bad_particles="datasets_small/u501_bad_particles.h5",
                 mode_fname = "browser_data/core_formation_mode_new_u601.h5",
                 frame_list = "every_ten",
                 field_list = track_info.field_lists['most_things'])

track_info.track('u602',
                 sim_directory=dl.sims['u202'],
                 target_frame = 118,
                 mountain_top = "datasets_small/u302_mountain_tops_take_9.h5",
                 peak_fname = 'datasets_small/u302_0118_peaklist.h5',
                 track_file = "%s/u600/u602_every_10_all_prim.h5"%dl.coresets['ourset'],
                 mode_fname = "browser_data/core_formation_mode_new_u602.h5",
                 frame_list = "every_ten",
                 field_list = track_info.field_lists['most_things'])

track_info.track('u603',
                 sim_directory=dl.sims['u203'],
                 target_frame = 107,
                 mountain_top = "datasets_small/u303_mountain_tops_take_9.h5",
                 peak_fname = 'datasets_small/u303_0107.h5',
                 track_file = "%s/u600/u603_every_10_all_prim.h5"%dl.coresets['ourset'],
                 mode_fname = "browser_data/core_formation_mode_new_u603.h5",
                 frame_list = "every_ten",
                 field_list = track_info.field_lists['most_things'])
