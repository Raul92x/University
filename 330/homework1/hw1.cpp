//Raul Diaz
//HW1
//Oct 16, 2013

#include <iostream>
#include "Vector.h"

using namespace std;

void sieve(Vector<int> &values);

int main()
{

	Vector<int> primes;

	cout << "pick number from 1 to 100: "<< endl;
	int p;
	cin >> p;
	if (p<1 || p>100 )
	{
		cout << "error number out of range" << endl;
		return 0;
	}

	for (int i = 0; i <= p; i++)
	{
		primes.push_back(i);
	}


	sieve(primes);

	//erases all 0's 
	int i = 0;
	while (i < primes.size())
	{
		if (primes[i] == 0)
		{
			primes.erase(i);
		}
		else
		{
			i++;
		}
	}



	//print out primes
	cout << endl << "prime numbers: " << endl;
	for (int a = 0; a < primes.size(); a++)
	{
		cout << primes[a] << " ";
	}
	cout<< endl;

	//insert the negative of the difference between 2 consecutive primes
	for (int i = primes.size() - 1; i >= 1; i--)
	{
		int n = primes[primes.size()-i-1] - primes[primes.size()-i];
		primes.insert(primes.size()- i, n);
	}

	//print out the negative between the 2 primes
	cout << endl << "difference of primes value in between them: " << endl;
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
