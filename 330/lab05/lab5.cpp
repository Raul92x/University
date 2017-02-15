//Raul Diaz
//lab5
//10/30/2013

#include <iostream>

using namespace std;

int div7(int);
int exes(int);
int sqr(int);
int pyrmd(int);
int opscount = 0;

int main()
{
	opscount = 0;
	int n=0;
	for (int i=0; i<10; i++)
	{
	n = n+5;
	div7(n);
	cout << " opscount:" << opscount << endl;
	}


	opscount = 0;
	for (int i=0; i<10; i++)
	{
	int a = 0;
	a = a+5;
	exes(a);
	cout << "opscount:" << opscount << endl;
	}


	opscount = 0;
	for (int i=0; i<10; i++)
	{
	int b = 0;
	b = b+5;
	sqr(b);
	cout<< "opscount: " << opscount << endl;
	}

	opscount = 0;
	for (int i=0; i<10; i++)
	{
	int c = 0;
	c = c+5;
	pyrmd(c);
	cout<< "opscount: " << opscount << endl;
	}
}



int div7 (int n)
{
	n = n/7;
	opscount++;
	for (int i = 0; i < 5; i++)
	{
		cout << n;
	}

	opscount++;
	return opscount;
}


int exes (int a)
{
	for (int i=0; i<a; i++)
		cout<< "x ";
		cout<< endl;
	opscount++;
	opscount++;
	opscount++;

	return opscount;
}



int sqr (int b)
{
	int j=0;
	while(j < b)
	{
		for (int i=0; i<b; i++)
			cout<< "x ";
			cout<< endl;
		j++;
		opscount++;
		opscount++;
	}

	return opscount;
}



int pyrmd(int c)
{
	int k=0;
	int x = 0;
	int y = 0;
	while (k<c)
	{
		x = x+c;
		y = x/c;

		for (int i=0; i<y; i++)
		{			
			cout<< "x ";
		}
		cout<< endl;
		k++;
		opscount++;
		opscount++;
	}
	opscount++;
	opscount++;

	return opscount;
}
