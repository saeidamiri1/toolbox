def file_parts(path0):
    file_name=os.path.basename(path0)
    file_path=os.path.dirname(path0)
    file_ext=file_name.split('.')[-1]
    file_base=file_name.split('.')[-2]
    return(file_path,file_name,file_base,file_ext)
    
def reload_frompath(module0,path0): 
    import sys
    from importlib import reload
    sys.path.append(path0)
    exec(f"import {source}")
    exec(f"reload {source}")

# path0='/home/samamiri/runs/samamiri/general_files/VeParser/VeParser/'
# module0='source'
# reload_frompath(module0,path0)
#################
def is_newer_b(a, bfiles):
    """
    check that all b files have been modified more recently than a
    """
    try:
        basestring
    except NameError:
        basestring = str
    if isinstance(bfiles, basestring):
        bfiles = [bfiles]
    if not os.path.exists(a): return False
    if not all(os.path.exists(b) for b in bfiles): return False
    atime = os.stat(a).st_mtime # modification time
    for b in bfiles:
        if atime > os.stat(b).st_mtime:
            # print('yes')
            return False
    return True
# a='~/file1.py'
# bfiles='~/note.sh'
# is_newer_b(a, bfiles)

