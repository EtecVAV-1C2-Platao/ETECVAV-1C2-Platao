#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int main() {
    int num;
    char r;
    while(r == 's'){
    
    
    	string dias[7] = {
        "Domingo", 
        "Segunda-Feira", 
        "Ter�a-Feira", 
        "Quarta-Feira", 
        "Quinta-Feira", 
        "Sexta-Feira", 
        "S�bado"
    	};

    	cout << "Digite um numero (1 a 7): ";
    	cin >> num;

    	if (num >= 1 && num <= 7) {
        cout << "O dia da semana �: " << dias[num - 1] << endl;
    	} else {
        cout << "N�mero inv�lido. Digite de 1 a 7." << endl;
    	}
   	 	cout << "Deseja continuar (s/n)? :";
    	cin >> r;
    	system ("CLS")

    
}
	return 0
}
