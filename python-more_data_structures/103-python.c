#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints basic information about Python bytes objects
 * @p: Pointer to a PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, limit, i;
	char *string;

	/* Must flush stdout to match Python's output buffer ordering */
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
		printf(" %02hhx", string[i]);
	printf("\n");
}

/**
 * print_python_list - Prints basic information about Python list objects
 * @p: Pointer to a PyObject
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	/* Direct struct access to avoid Py_SIZE and Py_TYPE */
	size = ((PyVarObject *)p)->ob_size;
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		/* Avoid PyList_GetItem by accessing ob_item array directly */
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
	}
}
