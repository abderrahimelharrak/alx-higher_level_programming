#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int sizze = PyList_Size(p);
	int x;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", sizze);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (x = 0; x < sizze; x++)
		printf("Element %i: %s\n", x, Py_TYPE(obj->ob_item[i])->tp_name);
}
