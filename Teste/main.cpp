#include <iostream>


/* run this program using the console pauser or add your own getch, system("pause") or input loop */


float pesoideal(char genero, float altura)
if( genero == 'm' ){
	return 72.7 * altura - 58
}
else if( genero == 'f' )
	return 62.1 * altura -58
}

main(){
char r = 's' ;
float altura;
char genero;
while( r == 's'){
	std::cout << "Digite seu genero(m/f) :\n"
	std::cin >> genero;
	std::cout << "Digite sua altura :"
	std::cin >> altura;

	std::cout << "Seu peso ideal e "<<pesoideal" em kg"
	std::cout << "Deseja continuar ? (s/n) :"
	std::cin >> r
}
	
	
}

		
	return 0;
}
