#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nod = *head, *new_l;

	new_l = malloc(sizeof(listint_t));
	if (new_l == NULL)
		return (NULL);
	new_l->n = number;

	if (nod == NULL || nod->n >= number)
	{
		new_l->next = nod;
		*head = new_l;
		return (new_l);
	}

	while (nod && nod->next && nod->next->n < number)
		nod = nod->next;

	new_l->next = nod->next;
	nod->next = new_l;

	return (new_l);
}
