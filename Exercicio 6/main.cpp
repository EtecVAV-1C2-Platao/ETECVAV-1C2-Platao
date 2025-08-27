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
        "Terça-Feira", 
        "Quarta-Feira", 
        "Quinta-Feira", 
        "Sexta-Feira", 
        "Sábado"
    	};

    	cout << "Digite um numero (1 a 7): ";
    	cin >> num;

    	if (num >= 1 && num <= 7) {
        cout << "O dia da semana é: " << dias[num - 1] << endl;
    	} else {
        cout << "Número inválido. Digite de 1 a 7." << endl;
    	}
   	 	cout << "Deseja continuar (s/n)? :";
    	cin >> r;
    	system ("CLS")

    
}
	return 0
}
