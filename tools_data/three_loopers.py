from starter2 import *
reload(looper)


if 'looper1' not in dir():
    file_list=glob.glob(dl.every_ten['u05'])
    looper1=looper.core_looper(directory=dl.sims['u05'])
    for nfile,fname in enumerate(file_list):
        looper1.load_loop(fname)
        print( "File %d of %d"%(nfile,len(file_list)))
    thtr = looper1.tr
    looper1.out_prefix='u201'
    thtr.sort_time()
'''
if 'looper2' not in dir():
    looper2=looper.core_looper(directory=dl.sims['u202'])
    file_list=glob.glob(dl.every_ten['u202'])
    for nfile,fname in enumerate(file_list):
        looper2.load_loop(fname)
        print( "File %d of %d"%(nfile,len(file_list)))
    looper2.out_prefix='u202'

if 'looper3' not in dir():
    looper3=looper.core_looper(directory=dl.sims['u203'])
    file_list=glob.glob(dl.every_ten['u203'])
    for nfile,fname in enumerate(file_list):
        looper3.load_loop(fname)
        print( "File %d of %d"%(nfile,len(file_list)))
    looper3.out_prefix='u203'
'''
