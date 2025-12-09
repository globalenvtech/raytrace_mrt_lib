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