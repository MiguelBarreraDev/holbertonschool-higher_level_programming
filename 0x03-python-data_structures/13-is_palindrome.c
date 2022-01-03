#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *first = *head;
	listint_t *end = *head;
	listint_t *tmp = NULL;
	int len = 0, ver = 0;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (end->next != NULL)
	{
		end = end->next;
		len++;
	}
	if (len % 2 != 0)
	{
		len -= 1;
	}
	while(ver < len/2)
	{		
		if (first->n != end->n)
		{
			return (0);
		}
		first = first->next;
		tmp = first;
		while(tmp->next != end)
		{
			tmp = tmp->next;
		}
		end = tmp;
		ver++;
	}
	return (1); 
}
