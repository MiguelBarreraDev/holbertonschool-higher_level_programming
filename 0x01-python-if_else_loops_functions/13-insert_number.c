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
	listint_t *new, *tmp_head, *prev_node;

	tmp_head = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	while (tmp_head)
	{
		if (tmp_head->n > number)
		{
			break;
		}
		prev_node = tmp_head;
		tmp_head = tmp_head->next;
	}
	new->next = tmp_head;
	prev_node->next = new;

	return (*head);
}
