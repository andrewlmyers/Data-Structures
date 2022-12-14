#include <stdio.h>
#include <stdlib.h>

// Define a node struct for a doubly linked list
typedef struct node
{
    // The data stored in this node
    int data;
    // Pointers to the previous and next nodes in the list
    struct node *prev;
    struct node *next;
} node;
// Define a List struct
typedef struct List
{
    // Pointers to the first and last nodes in the list
    node *head;
    node *tail;
} List;

// Append a new node to the end of the list
void append(List *list, int data)
{
    // Create a new node
    node *new_node = malloc(sizeof(node));
    new_node->data = data;
    new_node->prev = NULL;
    new_node->next = NULL;

    // If the list is empty, set the new node as the head and tail
    if (list->head == NULL)
    {
        list->head = new_node;
        list->tail = new_node;
    }
    // Otherwise, append the new node to the end of the list
    else
    {
        // Set the new node's prev pointer to the current tail
        new_node->prev = list->tail;

        // Set the current tail's next pointer to the new node
        list->tail->next = new_node;

        // Set the new node as the new tail of the list
        list->tail = new_node;
    }
}

// Remove node based on index
void remove(List *list, int index)
{
    // If the list is empty, there's nothing to remove
    if (list->head == NULL)
    {
        return;
    }

    // Find the node at the specified index
    int i = 0;
    node *current_node = list->head;
    while (i < index && current_node != NULL)
    {
        current_node = current_node->next;
        i++;
    }

    // If the index is out of bounds, do nothing
    if (current_node == NULL)
    {
        return;
    }

    // If the node to remove is the head of the list, set the next node as the new head
    if (current_node == list->head)
    {
        list->head = current_node->next;
    }

    // If the node to remove is the tail of the list, set the previous node as the new tail
    if (current_node == list->tail)
    {
        list->tail = current_node->prev;
    }

    // If the node to remove is not the head or tail, update the prev and next pointers of the surrounding nodes
    if (current_node != list->head && current_node != list->tail)
    {
        current_node->prev->next = current_node->next;
        current_node->next->prev = current_node->prev;
    }

    // Free the memory allocated for the node
    free(current_node);
}

node *search(List *list, int data)
{
    // Start at the head of the list
    node *current_node = list->head;

    // Iterate through the list until we find the value or reach the end
    while (current_node != NULL && current_node->data != data)
    {
        current_node = current_node->next;
    }

    // Return the node if we found it, or NULL if we reached the end without finding it
    return current_node;
}
