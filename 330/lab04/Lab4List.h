//Raul Diaz
//Lab4


// Lab4List.h
// after Timothy Budd, Data Structures in C++
// linked list basics only; not complete
// to be worked on in in Lab4;

//#pragma once
#ifndef LIST4_H_
#define LIST4_H_

#include <algorithm>
using namespace std;

// forward declaration of classes used
// by class List

template <class T> class Link;
template <class T> class ListIterator;
template <class T> class RListIterator;
template <class T> class ListCirculator;

template <class T>
class List
{
public:

	typedef ListIterator<T> iterator;
	typedef RListIterator<T> riterator;
	typedef ListCirculator<T> circulator;

	List();
	List(const List<T>& l);
	~List();

	bool empty() const;

	T& back() const;
	T& front() const;
	//void push_front(const T & x);
	void push_back(const T & x);
	//void pop_front();
	void pop_back(); 

	// iterators to beginning and back of linked list;
	iterator begin() const;
	iterator end() const;

	riterator rbegin() const;  
	riterator rend() const;    

	circulator cbegin() const;


protected:

	Link<T> * firstLink;
	Link<T> * lastLink;
};

// helper class for class List; notice the
// private interface and data members;
// notice the friend declaration that allow
// class List to access class Link's data 
// members directly;
template <class T>
class Link
{
private:
	Link(const T & x)
		: value(x), nextLink(0), prevLink(0)
	{}

	Link(const Link<T>& other)
		:value (other.value)
	{
		nextLink = other.nextLink;
		prevLink = other.prevLink;
	}

	~Link();

	T value;
	Link<T>* nextLink;
	Link<T>* prevLink;
	Link<T>* firstLink;

	friend class List<T>;
	friend class ListIterator<T>;
	friend class RListIterator<T>;
	friend class ListCirculator<T>;

};

// implements a "sliding window" over the
// Links of a List;
template <class T>
class ListIterator
{
 public:
        typedef ListIterator<T> iterator;

        ListIterator() : currentLink(0)
	{}

	ListIterator(Link<T> * alink)
	{
		currentLink = alink;
	}
	ListIterator(const ListIterator<T>& other)
	{
		currentLink = other.currentLink;
	}

	// dereference iterator; gets value of of Link pointed to;
	T & operator*() { return currentLink->value;}

	// define class specific assignment, and comparison (equal, not equal)
	ListIterator<T> & operator=(const ListIterator<T> & rhs);
	bool operator==(const iterator & rhs) const;
	bool operator!=(const iterator & rhs) const;

	// T. Budd has the ++ and -- operators backwards
	// regarding pre- and post-increment;

	ListIterator<T>& operator++(); // pre-increment; ++itr
	ListIterator<T> operator++(int); // post-increment; itr++

protected:

	Link<T> * currentLink; 

    // T.Budd includes pointer to List iterated over;
	// this is not necessary;

	friend class List<T>;
};


// turn this into reverse iterator RListIterator ... lab4

template <class T>
class RListIterator
{
 public:
        typedef RListIterator<T> riterator;

        RListIterator() : currentLink(0)
	{}

	RListIterator(Link<T> * alink)
	{
		currentLink = alink;
	}
	RListIterator(const ListIterator<T> & other)
	{
		currentLink = other.currentLink;
	}

	// dereference iterator; gets value of of Link pointed to;
	T & operator*() { return currentLink->value;}

	// define class specific assignment, and comparison (equal, not equal)
	RListIterator<T> & operator=(const RListIterator<T> & rhs);
	bool operator==(const riterator & rhs) const;
	bool operator!=(const riterator & rhs) const;

	// T. Budd has the ++ and -- operators backwards
	// regarding pre- and post-increment;

	RListIterator<T> & operator++(); // pre-increment; ++itr
	RListIterator<T> operator++(int); // post-increment; itr++

protected:

	Link<T> * currentLink; 

    // T.Budd includes pointer to List iterated over;
	// this is not necessary;

	friend class List<T>;
};



template <class T>
class ListCirculator
{
 public:
        typedef ListCirculator<T> circulator;

        ListCirculator() : currentLink(0), firstLink()
{}
	ListCirculator(Link<T> * alink)
	{
		currentLink = alink;
	}
	ListCirculator(const ListIterator<T> & other)
	{
		currentLink = other.currentLink;
	}

	// dereference iterator; gets value of of Link pointed to;
	T & operator*() { return currentLink->value;}

	// define class specific assignment, and comparison (equal, not equal)
	ListCirculator<T> & operator=(const ListCirculator<T> & rhs);
	bool operator==(const circulator & rhs) const;
	bool operator!=(const circulator & rhs) const;

	// T. Budd has the ++ and -- operators backwards
	// regarding pre- and post-increment;

	ListCirculator<T>& operator++(); // pre-increment; ++itr
	ListCirculator<T> operator++(int); // post-increment; itr++

protected:
	Link<T> * currentLink;
	Link<T> * firstLink; 

    // T.Budd includes pointer to List iterated over;
	// this is not necessary;

	friend class List<T>;
};



// constructors and member functions of class List<T>

template <class T>
List<T>::List()
: firstLink(0), lastLink(0)
{}

// copy constructor; T. Budd does not have it, but
// it is important for the compilation of our programs;
template <class T>
List<T>::List(const List<T>& other)
{
	firstLink = 0;
	lastLink = 0;

	if (!other.empty())
	{
		iterator start = other.begin();
		iterator stop = other.end();

		firstLink = new Link<T>(*start);
		Link<T>* current = firstLink;
		++start;

		while (start != stop)
		{
			T value = *start;
			Link<T>* newlink = new Link<T>(value);
			newlink->prevLink = current;
			current->nextLink = newlink;
			
			current = newlink;
			++start;
			
		}
		lastLink = current;
	}
}

// destructor; absolutely necessary to avoid
// memory leaks;
template <class T>
List<T>::~List()
{
	Link<T>* first = firstLink;
	while (first != 0)
	{
		Link<T> * next = first->nextLink;

		first->nextLink = 0; // unhook Link<T> first
		first->prevLink = 0; // then delete
		delete first;
		
		first = next;
	}
}

template <class T>
bool List<T>::empty() const
{
	return firstLink == 0;
}

template <class T>
T& List<T>::back() const
{
	return lastLink->value;
}


template <class T>
T& List<T>::front() const
{
	return firstLink->value;
}

template <class T>
void List<T>::push_back(const T & x)
{
	Link<T> * newback = new Link<T>(x);

	if (empty())
	{
		firstLink = newback;
		lastLink = newback;
	}
	else
	{
		lastLink->nextLink = newback;
		newback->prevLink = lastLink;
		lastLink = newback;
	}
}

template <class T>
void List<T>::pop_back()
{
	if (firstLink == 0)
		return;

	Link<T>* save = lastLink;

	lastLink = lastLink->prevLink;
	
	if (lastLink != 0)
		lastLink->nextLink = 0;
	else
		firstLink = 0;

	save->prevLink = 0;
	delete save;

}

template <class T>
ListIterator<T> List<T>::begin() const
{
	return ListIterator<T>(firstLink);
}


template <class T>
ListIterator<T> List<T>::end() const
{
	return ListIterator<T>(0);
}


template <class T>
RListIterator<T> List<T>::rbegin() const
{
	return RListIterator<T>(lastLink);
}


template <class T>
RListIterator<T> List<T>::rend() const
{
	return RListIterator<T>(firstLink);
}

template <class T>
ListCirculator<T> List<T>::cbegin() const
{
	return ListCirculator<T>(firstLink);
}


template <class T>
Link<T>::~Link()
{
	if (nextLink != 0)
		delete nextLink;
	if (prevLink != 0)
		delete prevLink;
}

// member functions of class ListIterator<T>

template <class T>
ListIterator<T> & ListIterator<T>::operator=(const ListIterator<T> & rhs)
{
	currentLink = rhs.currentLink;
	return *this;
}

template <class T>
bool ListIterator<T>::operator==(const iterator & rhs) const
{
  return currentLink == rhs.currentLink;
	
}

template <class T>
bool ListIterator<T>::operator!=(const iterator & rhs) const
{
  return currentLink != rhs.currentLink;
}

// ++itr ; returns iterator after being advanced; 
template <class T>
ListIterator<T>&  ListIterator<T>::operator++()
{
	currentLink = currentLink->nextLink;
	return *this;
}

// itr++; returns a clone of the current iterator;
// then advances;
template <class T>
ListIterator<T> ListIterator<T>::operator++(int)
{
	ListIterator<T> clone(currentLink);
	currentLink = currentLink->nextLink;
	return clone;
}


template <class T>
RListIterator<T> & RListIterator<T>::operator=(const RListIterator<T> & rhs)
{
	currentLink = rhs.currentLink;
	return *this;
}

template <class T>
bool RListIterator<T>::operator==(const riterator & rhs) const
{
  return currentLink == rhs.currentLink;
	
}

template <class T>
bool RListIterator<T>::operator!=(const riterator & rhs) const
{
  return currentLink != rhs.currentLink;
}

// ++itr ; returns iterator after being advanced; 
template <class T>
RListIterator<T>&  RListIterator<T>::operator++()
{
	currentLink = currentLink->nextLink;
	return *this;
}

// itr++; returns a clone of the current iterator;
// then advances;
template <class T>
RListIterator<T> RListIterator<T>::operator++(int)
{
	RListIterator<T> clone(currentLink);
	currentLink = currentLink->nextLink;
	return clone;
}


template <class T>
ListCirculator<T>& ListCirculator<T>::operator++()
{
	currentLink = currentLink->firstLink;
	return *this;
}


template <class T>
ListCirculator<T> ListCirculator<T>::operator++(int)
{
	ListCirculator<T> clone(currentLink);
	currentLink = currentLink->firstLink;
	return clone;
}


#endif









