#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{

    int a, b, resultado1, resultado2, resultado3, resultado4;
    char continuar;

 do{
    //pergunta os numeros
    cout << "digite um numero: ";
    cin >> a;
    cout << "digite outro numero: ";
    cin >> b;

    //faz as contas dos numeros
    resultado1=a+b;
    resultado2=a-b;
    resultado3=a/b;
    resultado4=a*b;

    //digita o resultado na tela 
    cout <<"a adicao e: " <<resultado1 << endl;
    cout <<"a subtracao e: " <<resultado2 << endl;
    cout <<"a divisao e: " <<resultado3 << endl;
    cout <<"a multiplicacao e: " <<resultado4 << endl;

    cout <<"quer continuar? (s/n)";
    cin >> continuar;

}while (continuar == 's');
    
    return 0;
}


