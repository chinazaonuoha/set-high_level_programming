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

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Accessing struct fields directly or via safe C-API functions */
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
