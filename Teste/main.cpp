#include <iostream>
#include <cstdlib>

float pesoideal(char genero, float altura) {
    if (genero == 'm') {
        return 72.7 * altura - 58;
    } else if (genero == 'f') {
        return 62.1 * altura - 58;
    } else {
        return -1;
    }
}

int main() {
    char r = 's';
    float altura;
    char genero;

    while (r == 's') {
        std::cout << "Digite seu genero (m/f): ";
        std::cin >> genero;

        std::cout << "Digite sua altura (em metros): ";
        std::cin >> altura;

        float resultado = pesoideal(genero, altura);

        if (resultado != -1) {
            std::cout << "Seu peso ideal e " << resultado << " kg\n";
        } else {
            std::cout << "Genero inválido. Use 'm' para masculino ou 'f' para feminino.\n";
        }

        std::cout << "Deseja continuar? (s/n): ";
        std::cin >> r;
        
        system("CLS");
    }

    return 0;
}


