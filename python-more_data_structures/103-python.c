#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: Pointer to a PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, limit, i;
	char *string;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);

	limit = (size >= 10) ? 10 : size + 1;
	printf("  first %zd bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02hhx", (unsigned char)string[i]);
	printf("\n");
}

/**
 * print_python_list - Prints basic information about a Python list object
 * @p: Pointer to a PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;
	const char *type_name;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		type_name = item->ob_type->tp_name;

		printf("Element %zd: %s\n", i, type_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
