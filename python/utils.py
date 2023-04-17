def file_parts(path0):
    file_name=os.path.basename(path0)
    file_path=os.path.dirname(path0)
    file_ext=file_name.split('.')[-1]
    file_base=file_name.split('.')[-2]
    return(file_path,file_name,file_base,file_ext)
    
