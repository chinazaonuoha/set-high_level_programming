#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the list.
 * Return: 0 if no cycle, 1 if a cycle exists.
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

/* If list is empty or has only one node, no cycle is possible */
if (list == NULL || list->next == NULL)
return (0);

while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
return (1);
}
return (0);
}
