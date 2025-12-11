import geomie3d

def separate_rays(rays: list[geomie3d.utility.Ray], nparallel: int):
    """
    separate the rays into roughly list[shape(nparallel, nrays/nparallel)]

    Parameters
    ----------
    rays: list[geomie3d.utility.Ray]
        a list of rays to separate
    
    nparallel : int
        the number of groups

    Returns
    -------
    list[list[geomie3d.utility.Ray]]
        list of rays in list[shape(nparallel, nrays/nparallel)]
    """
    rays_ls = []
    nrays = len(rays)
    interval = nrays/nparallel
    for i in range(nparallel):
        start = int(interval*i)
        end = int(interval*(i+1))
        rays_ls.append(rays[start:end])
    return rays_ls

def gen_rays(grid_xyzs: list[list[float]], ndirs: int) -> list[geomie3d.utility.Ray]:
    """
    generate rays for each mrt point

    Parameters
    ----------
    grid_xyzs : list[list[float]]
        list[shape(npts, 3)] the mrt grids to calc the MRT.

    ndirs: int
        The number of rays for each grid point.

    Returns
    -------
    list[geomie3d.utility.Ray]
        the rays generated for projection. Each ray has an attribute grid_id to identify it for later mrt calculations.
    """
    unitball = geomie3d.d4pispace.tgDirs(ndirs)
    #create the rays for each analyse pts
    rays = []
    for cnt,xyz in enumerate(grid_xyzs):
        for dix in unitball.getDirList():
            ray = geomie3d.create.ray(xyz, [dix.x, dix.y, dix.z], attributes = {'grid_id': cnt})        
            rays.append(ray)
    return rays