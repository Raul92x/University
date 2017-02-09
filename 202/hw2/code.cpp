//Raul Diaz
//Homework #2
//this program takes the capital letter characters that are
//input in and outputs it into morsecode

#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Code
{
public:
	Code();                                       // Constructor
	string decode(vector<char> message);          // decodes the message 

private:
	vector<string> codewords;           // this is a codeword vector parallel to A-Z, this one will contain the morsecode
	vector<char> alpha;                 // this is the vector for characters A-Z
	vector<char>  alphacode();          // this function returns a vector - A B C ...
	vector<string>  morsecode();        // this function returns vector containing morse code
	string decode(char c);              // returns the codeword/morsecode for character c
};

Code::Code()
{
	alpha = alphacode();				//alpha is now the vector of characters A-Z
	codewords = morsecode();			//codewords is now the vecotr that contains the morsecode
}

string Code::decode(vector<char> message)
{
	string temp;
	for (int i = 0; i<message.size(); i++)
	{
		temp += decode(message[i]);    //where the magic happens uses decode(char c) function/ char c = message[i]
	}
	return temp;
}

string Code::decode(char c)			   //char c= message[i]
{
	for (int i = 0; i<codewords.size(); i++)
	{
		if (c == alpha[i]) 					//checks if char c is equal to one of the characters in alpha[i]/alphacode[i]
		{
			return codewords[i];			//it then takes what is equal to alphacode[i] and sends it to codewords/morsecode() to find the corresponding symbols
		}
	}
}

vector<char> Code::alphacode()
{                                       // This returns a vector containing the alphabet A-Z and " " and "."
	vector<char> temp;
	for (char c = 'A'; c <= 'Z'; c++)	//enters the letters
		temp.push_back(c);
	temp.push_back(' ');				//enters the space
	temp.push_back('.');				//enters the period.
	return temp;						//this the same as typing temp[0]='A';temp[1]='B'; ... temp[25]='Z';temp[26]=' ';temp[27]='.'
}

vector<string> Code::morsecode()
{                                       // This function returns a vector containing the morse code
	vector<string> temp(28);			//compares c/message[i]
	temp[0] = " .-";
	temp[1] = " -...";
	temp[2] = " -.-.";
	temp[3] = " -..";
	temp[4] = " . ";
	temp[5] = " ..-.";
	temp[6] = " --.";
	temp[7] = " ....";
	temp[8] = " ..";
	temp[9] = " .---";
	temp[10] = " -.-";
	temp[11] = " .-..";
	temp[12] = " --";
	temp[13] = " -.";
	temp[14] = " ---";
	temp[15] = " .--.";
	temp[16] = " --.--";
	temp[17] = " .-.";
	temp[18] = " ...";
	temp[19] = " -";
	temp[20] = " ..-";
	temp[21] = " ...-";
	temp[22] = " .--";
	temp[23] = " -..-";
	temp[24] = " -.--";
	temp[25] = " --..";
	temp[26] = " .......";
	temp[27] = " x";
	return temp;
}


int main()
{
	vector<char> codemessage;		//the message vector
	string temp1;					//temp for storing each code letter
	getline(cin, temp1);			//get the input
	for (int i = 0; i <temp1.length(); i++)
	{
		codemessage.push_back(temp1[i]);
	}
	Code C;
	cout << C.decode(codemessage) << endl;  //prints morsecode after decoding it
}