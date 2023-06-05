#include "lists.h"
#include <stdio.h>
#include <stdbool.h>

/**
 * check_cycle - checks for a cycle in singly linked list
 * @list: param from linkedlist
 *
 * Return: Returns 1 for a cycle, else 0
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
	{
		return (0);
	}

	while (1)
	{
		if (fast->next != NULL && fast->next->next != NULL)
		{
			fast = fast->next->next;
			slow = slow->next;

			if (fast == slow)
			{
				return (1);
			}
		}
		else
		{
			return (0);
		}
	}

}
