//Raul Diaz
//hw2
//11/4/2013
#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <time.h>


using namespace std; 
// prototype, (function decleration)
void rand_seed();
int rand_int(int, int);

template <class T>
void mergeSort(vector<T> & s);
template <class Itr>
void m_sort(Itr start, unsigned int left, unsigned int right);
template <class T>
void mergeSortlist(list<T> & a);
template <class Itr>
void m_sortlist(std::_List_iterator<int>, int, std::_List_iterator<int>);

// main funtion;
int main()
{
	int next;
	vector<int> vec;

	rand_seed();
	
	for (int i = 1; i <= 10; i++)
		vec.push_back(rand_int(1,100));

	cout << endl << "vector with random integers:" << endl;
	for (int i = 0; i < vec.size(); i++)
		cout << vec[i] << " ";
	cout << endl;


	mergeSort(vec);
	cout << "sorted:" << endl;
	for (int i = 0; i < vec.size(); i++)
		cout << vec[i] << " ";
	cout << endl << endl;


	list<int> mylist;
	cout << "linked list with random integers:" << endl;
	for (int i = 1; i <= 10; i++)
		mylist.push_front(rand_int(1,100));
	list<int>::iterator itr;
	for (itr=mylist.begin(); itr != mylist.end(); ++itr)
	{
		cout << " " << *itr;
	}

	cout << endl;

	cout << "sorted:" << endl;
	mylist.sort();
	for (itr=mylist.begin(); itr != mylist.end(); ++itr)
	{
		cout << " " << *itr;
	}
	cout << endl << endl;

}


// function definitions
void rand_seed()
{
	int seed = static_cast<int>(time(0));
	srand(seed);
}


// random integer between a and b;
int rand_int(int a, int b)
{
	return a + rand() % (b - a + 1);
}


//mergesort functions
template <class T>
void mergeSort(vector<T> & s)
{
	m_sort(s.begin(), 0, s.size());
}

template <class Itr>
void m_sort(Itr start, unsigned int left, unsigned int right)
{
	if (left + 1 < right)
	{
		unsigned int center = (right + left) / 2;
		m_sort (start, left, center);
		m_sort (start, center, right);
		inplace_merge (start + left, start + center, start + right);
	}
}
