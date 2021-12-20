#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (!list)
		return (0);

	turtle = list;
	hare = list;
	while (turtle->next != NULL && hare->next->next != NULL)
	{
		turtle = turtle->next;
		hare = hare->next->next;

		if (hare == turtle)
			return (1);
	}
	return (0);
}
