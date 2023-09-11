#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: success
 */
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *currente = *head;
	listint_t *nexte = NULL;

	while (currente)
	{
		nexte = currente->next;
		currente->next = previous;
		previous = currente;
		currente = nexte;
	}

	*head = previous;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: success
 */
int is_palindrome(listint_t **head)
{
	listint_t *slower = *head, *faster = *head, *tmp = *head, *dupp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		faster = faster->next->next;
		if (!faster)
		{
			dupp = slower->next;
			break;
		}
		if (!faster->next)
		{
			dupp = slower->next->next;
			break;
		}
		slower = slower->next;
	}

	reverse_listint(&dupp);

	while (dupp && tmp)
	{
		if (tmp->n == dupp->n)
		{
			dupp = dupp->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dupp)
		return (1);

	return (0);
}
