#include <Python.h>

void print_list_info(PyObject *list_obj) {
    printf("List info:\n");
    printf("  Type: %s\n", Py_TYPE(list_obj)->tp_name);
    printf("  Length: %zd\n", PyList_Size(list_obj));
}

void print_bytes_info(PyObject *bytes_obj) {
    printf("Bytes info:\n");
    printf("  Type: %s\n", Py_TYPE(bytes_obj)->tp_name);
    printf("  Length: %zd\n", PyBytes_Size(bytes_obj));
}
