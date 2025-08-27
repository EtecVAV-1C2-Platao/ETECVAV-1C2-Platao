#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;


int contarVogais(const char* nome) {
    int contador = 0;
    for (int i = 0; i < strlen(nome); ++i) {
        char letra = tolower(nome[i]);
        if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u') {
            contador++;
        }
    }
    return contador;
}

int contarConsoantes(const char* nome) {
    int contador = 0;
    for (int i = 0; i < strlen(nome); ++i) {
        char letra = tolower(nome[i]);
        if ((letra >= 'a' && letra <= 'z') && !(letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u')) {
            contador++;
        }
    }
    return contador;
}

int main() {
    char nome[100];
    char continuar;

    do {
    	
        system("cls"); 

        cout << "Digite o nome completo: ";
        cin.ignore(); 
        cin.getline(nome, 100);

        int vogais = contarVogais(nome);
        int consoantes = contarConsoantes(nome);

        cout << "Quantidade de vogais: " << vogais << endl;
        cout << "Quantidade de consoantes: " << consoantes << endl;

        cout << "Deseja continuar? (s/n): ";
        cin >> continuar;

    } while (continuar == 's' || continuar == 'S');

    return 0;
}
