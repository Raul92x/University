//Raul Diaz
//hw3.cpp
//11/27/2013
#include <iostream>
#include <vector>
#include <set>
#include <cstdlib>
using namespace std;

void rand_seed();
int rand_int(int, int);
template <class T>
void treesort(vector<T>&);

int main()
{
	set<int> myset;
	set<int>::iterator itr;
	vector<int> vec;
	
	rand_seed();
	for (int i = 1; i <= 10; i++)
		vec.push_back(rand_int(1,100));
	
	cout << endl << "vector with random integers:" << endl;
	for (int i = 0; i < vec.size(); i++)
		cout << vec[i] << " ";
	cout << endl << endl;
	
	treesort(vec);
	
	cout<<endl<<"vector contains: " << endl;
	for (int i = 0; i < vec.size(); i++)
		cout << vec[i] << " ";
	cout << endl << endl;

	return 0;
}

void rand_seed()
{
	int seed = static_cast<int>(time(0));
	srand(seed);
}
int rand_int(int a, int b)
{
	return a + rand() % (b - a + 1);
}

template <class T>
void treesort(vector<T>& vec)
{
	set<int> myset;
	set<int>::iterator itr;

	for (int i = 0; i < vec.size(); i++)
		myset.insert(vec[i]);
	
	cout << "myset contains:" << endl;
	for (itr=myset.begin(); itr!=myset.end(); ++itr)
		cout << *itr << " ";
		cout << endl;

	vec.clear();
	for (itr=myset.begin(); itr!=myset.end(); ++itr)
		vec.push_back(*itr);
}
