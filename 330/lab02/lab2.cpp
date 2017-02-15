//raul diaz
//lab2
//oct 09, 2013

#include <iostream>
#include "Vector.h"

using namespace std;


void sieve(Vector<int> &values);


int main()
{

	Vector<int> primes;


	for (int i = 0; i <= 100; i++)
	{
		primes.push_back(i);
	}


	sieve(primes);

	for (int a = 0; a < primes.size(); a++)
	{
		cout << primes[a] << " ";
	}
	cout<< endl;
}





void sieve(Vector<int> &values)
{
	unsigned int max = values.size();
	int i;
	
	for(i = 0; i < max; i++)
		values[i] = i;
	
	for(i =2; i*i <= max; i++)
	{	
		if (values[i] != 0)
		{
			for(int j = i + i; j < max; j += i)
				values[j] = 0;
		}
	}
}

