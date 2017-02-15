//Raul Diaz
//11/13/2013
//lab7

#include "Node.h"
#include <iostream>

using namespace std;

void print_node(Node * n)
{
  if (n == 0)
    return;

  if (n->left != 0)
    {
      print_node(n->left);
    }
  cout << n->value << " ";
  if (n->right != 0)
    {
      print_node(n->right);
    }
}

int main()
{
  Node * node1 = new Node(8);
  cout << endl;
  cout << "value in n1: " << node1->value << endl << endl;

  node1->add_value(3);
  node1->add_value(15);
  node1->add_value(23);
  node1->add_value(13);
  node1->add_value(18);
  node1->add_value(26);
  node1->add_value(7);
  node1->add_value(9);
  node1->add_value(1);
  node1->add_value(20);
  node1->add_value(21);
  node1->add_value(6);
  print_node(node1);

  cout << endl << endl;

  return 0;
}
