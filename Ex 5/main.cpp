#include <iostream>
#include <string>
#include <cctype>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	string palavra;
	char r ='s';
	while (r == 's' || r == 'S'){
		
		std::cout <<"Digite uma palavra: ";
		std::cin>>palavra;
		
		for (int i = 0; i < (int)palavra.length(); i++){
			palavra [i] = tolower (palavra [i]);
		}
		
		int tamanho = palavra.length();
		bool palindromo = true;
		
		for (int i=0; i<tamanho/2; i++){
			if (palavra [i] !=palavra [tamanho-1-i]){
				palindromo = false;
				break;
			}
		}
		if (palindromo){
			std::cout<<"A palavra e um palindromo"<<endl;
		}else{
			std::cout<<"A palavra nao e um palindromo"<<endl;
		}
		std::cout<<"Deseja continuar (S/N)?: ";
		std:: cin >>r;
					
	}
	return 0;
}
