from starter2 import *
import matplotlib.image as mpimg

import data_locations as dl
reload(dl)
plt.close('all')

file_list=glob.glob('%s/*h5'%dl.sixteen_frame)
out_prefix = 'CHANGE_THIS_PREFIX'

if 'this_looper' not in dir():
    this_looper=looper.core_looper(directory=dl.enzo_directory)
    for nfile,fname in enumerate(file_list):
        this_looper.load_loop(fname)
        print( "File %d of %d"%(nfile,len(file_list)))
    thtr = this_looper.tr
    all_cores = np.unique(thtr.core_ids)
    rm = rainbow_map(len(all_cores))

for core_id in all_cores:
        asort =  np.argsort(thtr.times)
        n0=asort[0]
        tsorted = thtr.times[asort]
        fig,ax=plt.subplots(1,1)
        ms = trackage.mini_scrubber(thtr,core_id)
        density = thtr.c([core_id],'density')
        tmap=rainbow_map(ms.ntimes)
        norm = mpl.colors.Normalize()
        norm.autoscale( np.log10(density[:,n0]))
        cmap = mpl.cm.jet
        color_map = mpl.cm.ScalarMappable(norm=norm,cmap=cmap)

        for npart in list(range(ms.nparticles))[::100]:
            c = color_map.to_rgba(np.log10(density[npart,n0]))
            #ax.plot( tsorted, density[npart,asort],c='k',linestyle=':',marker='*')
            ax.plot( tsorted, density[npart,asort],c=c,linewidth=.1)#linestyle=':')
        ax.plot(tsorted, density.mean(axis=0)[asort],c='k')

        t0 = thtr.times[asort][0]
        t1 = thtr.times[asort][-1]
        rho0 =1.1 #10 # np.mean(density[:,asort[0]])
        rho1 = density.max() # np.mean(density[:,asort[-1]])
        alpha = 1.8
        tc =t1*(1-(rho1/rho0)**(-1./alpha))**-0.5
        G=1 #np.pi*4#1620./(4*np.pi)
        tff_global = np.sqrt(3*np.pi/(32*G*1))
        tff_local = np.sqrt(3*np.pi/(32*G*rho0))
        #tc=tff_local #kludge
        rhot = rho0*(1-(tsorted/tc)**2)**-alpha
        rho_c = 3*np.pi/(32*G*tc**2)

        ok = np.isnan(rhot)==False
        ax.plot( tsorted[ok], rhot[ok], c='r',label=r'$tc/tff = %0.2e$'%(tc/tff_local))
        #ax.text( tsorted[0], rho1, r'$tc = %0.2e \rho_c = %0.2e$'%(tc,rho_c))
        #ax.text( tsorted[0], 0.5*rho1, 
        ax.legend(loc=0)
        axbonk(ax,xscale='linear',yscale='log',xlabel='t',ylabel=r'$\rho$')
        oname = "test2/%s_density_4_c%04d"%(out_prefix,core_id)
        fig.savefig(oname)
#           for i,n in enumerate(asort):
#               timeline=plt.plot( [tsorted[i]]*2,[1,1e8],c=[0.5]*3,linewidth=0.1)
#               timetext=plt.text( tsorted[i], 1e8, 'n=%d'%thtr.frames[n])
#               outname = 'image_tracks/rho_t_fit2_c%04d_s%04d.png'%(core_id,i)
#               plt.yscale('log')
#               plt.savefig(outname)
#               timeline[0].remove()
#               timetext.remove()

#               print('saved '+outname)

#               frame = thtr.frames[n]
#               frame = i #you suck.
#               basedir = "/home/dcollins/RESEARCH2/Paper19_47_overlap/0000_density_tracks/x/ALL"
#               core_dir = "%s/c%04d"%(basedir,core_id)
#               image = "%s/test_full_particles_c%04d_n%04d_Projection_x_density.png"%(core_dir,core_id,frame)
#               img1 = mpimg.imread(image) 
#               img2 = mpimg.imread(outname) 
#               both = np.zeros( [ max([img1.shape[0],img2.shape[0]]), img1.shape[1]+img2.shape[1],4])
#               both[ 0:img1.shape[0] , 0:img1.shape[1]]=img1
#               both[ 0:img2.shape[0] , img1.shape[1]:]=img2
#               oname2 = "image_tracks/density_2_c%04d_n%04d"%(core_id,frame)
#               print(oname2)
#               plt.imsave(oname2,both)

