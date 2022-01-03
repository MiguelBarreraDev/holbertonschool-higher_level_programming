#include "lists.h"
#include <stdio.h>
/**
* betty comentary
*/
int is_palindrome(listint_t **head)
{
	listint_t *first = *head;
	listint_t *end = *head;
	listint_t *tmp = NULL;
	int len = 0, ver = 0;

	if (*head == NULL)
		return (1);

	while (end != NULL)
	{
		tmp = end;
		end = end->next;
		len++;
	}
	len = (len % 2 == 0) ? len :  (len - 1);
	end = tmp;
	tmp = NULL;
	printf("len -> %d\n", len);
	while(ver < len/2)
	{		
		if (first->n != end->n)
			return (0);
		tmp = first;
		first = first->next;
		while(tmp->next != end)
			tmp = tmp->next;
		end = tmp;
		ver++;
	}
	return (1); 
}
