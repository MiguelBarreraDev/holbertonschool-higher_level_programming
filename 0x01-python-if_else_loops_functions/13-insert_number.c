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

	if (!head || *head == NULL || (*head)->next == NULL)
		return (NULL);

	current = *head;
	after = current->next
	if (number > current->n && number < after->n)
	{
		new = malloc(sizeof(listint_t *));
		if (!new)
			return (NULL);
		new->n =number;
		current->next = new;
		new->next = after;
		return (new);
	}
	if (!after)
		return (NULL);
	return (insert_node(&after, number));
}
