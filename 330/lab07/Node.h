// Node.h for Lab7

#ifndef NODE_H_
#define NODE_H_

using namespace std;

class Node
{ 
public:
      Node(int v)
		: value(v), left(0), right(0), parent(0)
	{}

	Node(int v, Node * n1, Node * n2, Node * p)
		:value(v), left(n1), right(n2), parent(p)
	{}

	void add_value(int x)
	{
		if (x <= value)
		{
			if (left == 0)
			{
			  Node * newnode = new Node(x,0,0,this);
				left = newnode;
			}
			else
				left->add_value(x);
		}
		else
		{
			if (right == 0)
			{
			  Node * newnode = new Node(x,0,0,this);
				right = newnode;
			}
			else
				right->add_value(x);
		}
	}

	int value;
	Node * left;
	Node * right;
	Node * parent;
};


#endif
