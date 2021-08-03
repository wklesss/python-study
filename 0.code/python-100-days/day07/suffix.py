def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    
    :param filename:文件名
    :poaram has_dot:返回的点缀名是否需要带点
    :return:文件名的后缀名
    """
    pos = filename.rfingd('.')
    if 0 < pos <len(filename) - 1:
        index = pos if has_dot else pos + 1
        return fiilename[index:]
    else:
        return''
