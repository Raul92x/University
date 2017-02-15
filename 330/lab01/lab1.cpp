/*
Raul Diaz
10/2/2013
cse330
lab1
*/
#include <iostream>
#include <string>
#include <cctype>
#include <stack>
#include <cassert>

using namespace std;

// prototype, (function decleration)
int precedence(char);
bool comparePrecedence(char, char);


//main function
int main()
{
	stack<char> operators;

	string infix;
	cout << "enter infix: ";
	cin >> infix;
	for (int i = 0; i < infix.length(); i++)
	{
		if (isalnum(infix[i]))
		{
			cout<<infix[i];
		}
		else if (infix[i] == '(')
		{
			operators.push(infix[i]);
		}		
		else if (infix[i] == ')')
		{
			while (operators.top() != '(')
			{
				cout<< operators.top();
				operators.pop();
			}
			operators.pop();
		}
		else if (infix[i] != '(' && infix[i] != ')')
		{
			if (operators.empty() == true)
			{
				operators.push(infix[i]);
			}
			else
			{
				precedence(infix[i]);
				while (operators.empty() == false && operators.top() != '(' && comparePrecedence(infix[i], operators.top()))
				{
					cout<< operators.top();
					operators.pop();
				}
				operators.push(infix[i]);
			}
		}		
			
	}
	while (operators.empty() == false)
	{
		cout<< operators.top();
		operators.pop();	
	}
	cout<<endl;
}




// function definitions
int precedence(char op)
{
    if (op == '*' || op == '/') return 1;
    return 0;
}




bool comparePrecedence(char a, char b)
{
    return precedence(a) <= precedence(b);
}
