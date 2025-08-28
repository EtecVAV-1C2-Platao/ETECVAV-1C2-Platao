#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	char r = 's';
	double area;
	double valor;
	while (r == 's' || r == 'S'){
		double soma = 0.0; 
	
		std::cout<< "Escreva o raio de cinco circulos\n ";
	
		for (int i =0; i < 5; i++){
			std::cout<<"Escrva o valor do raio: ";
			std::cin>>valor;
			area = 3.14 * valor * valor;
			soma += area;
		}
		
		std::cout<<"O valor da soma da area de cada circulo e: "<<soma << std::endl;
	
		 std::cout << "Deseja contiuar (S/N)?: ";
		 std::cin >>r;
		 
	}
	return 0;
}
