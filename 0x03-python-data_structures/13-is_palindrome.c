#include "lists.h"
/**
* betty comentary
*/
int is_palindrome(listint_t **head)
{
	listint_t *first, *end;
	int band = 0; 
	size_t len = 0, count = 0;
	
	if (!head)
		return (band);
	else if (*head == NULL)
		band = 1;
	else
	{
		first = *head;
		end = reversed_list(head);
		len = len_list(head);

		while(first != NULL)
		{
			if (first->n == end->n)
				count++;
			first = first->next;
			end = end->next;
		}
		band = (count == len) ? 1 : 0;
	}
	return (band); 
}
/**
* betty comentarys
*/
listint_t *reversed_list(listint_t **head)
{
	listint_t *new_head, *tmp;
	
	if (!head || *head == NULL)
		return (NULL);

	if((*head)->next == NULL)
	return (*head);

	new_head = reversed_list(&((*head)->next));
	tmp = new_head;

	while (tmp->next != NULL)
	tmp = tmp->next;	
	tmp->next = *head;
	(*head)->next = NULL;

	return (new_head);
}
/**
* betty comentarys
*/
size_t len_list (listint_t **head)
{
	listint_t *tmp = *head;
	size_t len = 0;
	
	if (!head || *head == NULL)
		return (0);

	while(tmp != NULL)
	{
		tmp = tmp->next;
		len++;
	}
	return (len);
}
