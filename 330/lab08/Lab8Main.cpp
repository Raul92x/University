// Lab8Main.cpp
#include "Set.h"
#include <iostream>
#include <vector>

using namespace std;

int main()
{
  Set<int> myset;
  int next;

  for (int i = 1; i<= 5; i++)
    {
      cout << endl;
      cout << "[integer] ";
      cin >> next;
      myset.insert(next);
    }

  vector<int> allvals;
  cout << endl << endl;
  myset.print(allvals);
  cout << endl << endl;
  
  // now remove the values from the set
  // one by one ...

  for (int i = 0; i < allvals.size(); i++)
    {
      cout << endl;
      cout << "removing value " << allvals[i] << endl;

      myset.erase(allvals[i]);

      vector<int> rest; // dummy vector; needed by print
      myset.print(rest);
    }
  cout << endl << endl;
  return 0;
}



