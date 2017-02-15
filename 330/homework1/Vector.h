//Vector.h
//Raul Diaz
//KV, after T. Budd
#include <cassert>
#include <algorithm>
using namespace std;

template <class T>
class Vector
{
   public:
	
	typedef T * iterator;
	
     Vector()
	: myCapacity(0), mySize(0), buffer(0)
     {
     }

     Vector(unsigned int sz)
	: buffer(0), mySize(0)
	{
		buffer = new T[sz];
		myCapacity = sz;
		mySize = sz;
	}

     Vector(unsigned int sz, T initial)
	: buffer(0)
	{
		resize(sz);
		fill(buffer, buffer+mySize, initial);
	}

	//copy constructor;
	Vector(Vector<T>&);


	//DESTRUCTOR
	~Vector() { delete [] buffer;}


     T front() {return buffer[0];}
     T back() {return buffer[mySize-1];}




     void reserve(unsigned int newCapacity);

     // copy, complete this member function from book;
     // will reserve array space of size sz



	iterator begin(){return buffer;}
	iterator end(){return buffer + mySize;}
 
     bool empty() { return mySize == 0;}

     unsigned int size() { return mySize;}
     unsigned int capacity() { return myCapacity;}

     

     void push_back (T);
     void pop_back() {mySize--;}

     void erase(unsigned int);
     void insert(unsigned int, int);

     void resize(unsigned int newSize)
     {
	reserve(newSize);
	mySize = newSize;
     }

	T& operator [](unsigned int index) {return buffer[index];}

   private:
     unsigned int myCapacity;
     unsigned int mySize;

     T * buffer;
};


template <class T>
Vector<T>::Vector(Vector<T>& v)
{
	buffer = 0;
	
	resize(v.size());
	//copy from beginning of v, to the end of v,
	// starting at the beginning of this new vector (buffer);	
	//use generic algorithm "copy" in <algorithm> of STL;	
	copy(v.begin(), v.end(), begin());

}





template <class T>
void Vector<T>::push_back(T val)
{
	if (mySize >= myCapacity)
		reserve(myCapacity+5);

	buffer[mySize++] = val;
	//buffer[mySize] = val;		other version to 
	//mySize++;			write it
}


template <class T>
void Vector<T>::reserve(unsigned int newCapacity)
{
	if (buffer == 0)
	{
		mySize==0;
		myCapacity==0;
	}
	//dont do anything if already large enough
	if (newCapacity <= myCapacity)
	return;
	T * newBuffer = new T [newCapacity];
	assert (newBuffer);
	//copy values into buffer
	copy(buffer, buffer + mySize, newBuffer);
	myCapacity = newCapacity;

	delete[] buffer;
	buffer = newBuffer;
}



template <class T>
void Vector<T>::erase(unsigned int index)
{
	//before doing anything what if index is out of range?...do nothing(not you..the program)
	if (index >= mySize)
		return;
	//what if index is at last position? ... do pop_back;
	if (index == mySize-1)
	{
		pop_back();
		return;
	}

	//what if index is 0?
	//now move into general case;
	//for i starting at index, and going up to (and including) mySize-2, but no further, do 
	//buffer[i] = buffer [i+1]
	//then do one pop_back;

	for (int i = index; i <= mySize-2; i++)
	{
		buffer[i] = buffer [i+1]; 
	}
	pop_back();
	return;
}


template <class T>
void Vector<T>::insert(unsigned int index, int newval)
{
	//before doing anything check and handle easy cases...
	//for the general case do...
	//push_back the rightmost element of vector;
	push_back(buffer[mySize-1]);
	//for i starting at mySize -2. going down to index + 1, do
	//buffer[i] = buffer[i+1];
	for (int i = mySize - 2; i >= index+1; i--)
	{

		buffer[i] = buffer [i-1];

	}

	//finish with buffer[index] = newval
	buffer[index] = newval;

}
