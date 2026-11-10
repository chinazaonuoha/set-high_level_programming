#include <Python.h>
#include <stdio.h>


/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: a PyObject
 * return: void
 * You are not allowed to use the following macros/functions:
* Py_SIZE
* Py_TYPE
* PyList_GetItem
* PyBytes_AS_STRING
* PyBytes_GET_SIZE
 */

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);

    if (size < 10)
        printf("  first %zd bytes: ", size + 1);
    else
        printf("  first 10 bytes: ");

    for (i = 0; i < size && i < 10; i++)
        printf("%02x%c", (unsigned char)string[i], i == size - 1 || i == 9 ? '\n' : ' ');
}


