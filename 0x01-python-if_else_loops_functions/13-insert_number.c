#include "lists.h"
/**
 * insert_node - functions that add new node in the single linked list
 * @head: address of the single linked list
 * @number: member for adding to the new node
 *
 * Return: Address of the new node it if success. NULL it if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *after, *new = NULL;
	/*---- start - new node ----*/
	new = malloc(sizeof(listint_t *));
	if (!new)
		return (NULL);
	new->n = number;
	/*---- end - new node ----*/
	current = *head;
	after = current->next;
	if (current == NULL || current->n > number)
	{
		new->next = current;
		*head = new;
		return (*head);
	}
	else if (number > current->n && number < after->n)
	{
		new->n =number;
		current->next = new;
		new->next = after;
		return (new);
	}
	if (!after)
		return (NULL);
	return (insert_node(&after, number));
}
