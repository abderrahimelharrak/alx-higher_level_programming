import ctypes

libe = ctypes.CDLL('./libPyList.so')
libe.print_python_list_info.argtypes = [ctypes.py_object]
le = ['hello', 'World']
libe.print_python_list_info(le)
del le[1]
libe.print_python_list_info(le)
le = le + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
libe.print_python_list_info(le)
le = []
libe.print_python_list_info(le)
le.append(0)
libe.print_python_list_info(le)
le.append(1)
le.append(2)
le.append(3)
le.append(4)
libe.print_python_list_info(le)
le.pop()
libe.print_python_list_info(le)
