#include <iostream>
#include <cstdlib>

using namespace std;

const char* verificarOrdem(int numeros[], int tamanho) {
    bool crescente = true;
    bool decrescente = true;

    for (int i = 0; i < tamanho - 1; ++i) {
        if (numeros[i] < numeros[i + 1]) {
            decrescente = false;
        } else if (numeros[i] > numeros[i + 1]) {
            crescente = false;
        }
    }

    if (crescente) {
        return "Ordem Crescente";
    } else if (decrescente) {
        return "Ordem Decrescente";
    } else {
        return "Nao Ordenado";
    }
}

int main() {
    char continuar;

    do {

        system("cls");

        int numeros[5];

        cout << "Digite 5 numeros: " << endl;
        for (int i = 0; i < 5; ++i) {
            cin >> numeros[i];
        }

        cout << "Numeros digitados: ";
        for (int i = 0; i < 5; ++i) {
            cout << numeros[i] << " ";
        }
        cout << endl;

        const char* ordem = verificarOrdem(numeros, 5);
        cout << "A ordem dos numeros e: " << ordem << endl;

        cout << "Deseja continuar? (s/n): ";
        cin >> continuar;

    } while (continuar == 's' || continuar == 'S');

    return 0;
}

