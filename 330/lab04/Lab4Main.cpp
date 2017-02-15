//Raul Diaz
//Lab4

// Lab4Main.cpp
// KV, October 2013, to test Lab4List.h

// attempt the addition of reverse and circular list iterators;

#include "Lab4List.h"
#include <iostream>

using namespace std;

int main()
{
  int n;
  List<int> mylst;

  cout << endl;
  cout << "How many values is your list? ";
  cin >> n;
  cout << endl;

  int next;
  for (int i = 1; i <= n; i++)
    {
      cout << "[integer] ";
      cin >> next;

      mylst.push_back(next);
    }

  List<int>::iterator itr = mylst.begin();

  cout << endl << endl;

  for (; itr != mylst.end(); ++itr) //itr++)
    cout << *itr << " ";

  cout << endl << endl;

  //... testing reverse iterator ...

  List<int>::riterator ritr = mylst.rbegin();

  for (; ritr != mylst.rend(); ritr++)
    cout << *ritr << " ";

  cout << endl << endl;
  

  //... testing circular iterator ...

  List<int>::circulator citr = mylst.cbegin();

  for (int i = 1; i <= 15; i++)
    {
      cout << *citr << " ";

      citr++;
    }

  cout << endl << endl;
  

  return 0;
}
