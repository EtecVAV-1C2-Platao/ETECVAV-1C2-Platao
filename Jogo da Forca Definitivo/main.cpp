#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cctype>
using namespace std;

int main(int argc, char *argv[]){
    int numsorteado, tolletras, acertos, erros, tentativas;
    bool achou;
    char palavras[20][20]={"celular","smartphone","iphone","samsung","motorola",
                          "xiaomi","android","ios","tela","touchscreen",
                          "portatil","eletronico","chip","camera","Touchscreen",
                          "mensagem","ligacao","aparelho","wi fi","bluetooth"};
    char palavraSO[20], mascara[20], chute;
    char r = 'S';
    
    srand(time(NULL));
    
    while (r=='S'||r=='s'){
          acertos=0;
          erros=0;
          tentativas=6; 
          
          
          numsorteado = rand() % 20;
          strcpy(palavraSO,palavras[numsorteado]);
          tolletras=strlen(palavraSO);
          
          for(int i = 0; i < tolletras; i++){
                  mascara[i]='-';
          }
          mascara[tolletras]='\0';    
          
          while(tentativas>0 && acertos < tolletras){
             std::cout<<"JOGO DA FORCA\n";
             std::cout<<"Palavra: "<<mascara<<"\n";
             std::cout<<"Digite uma letra aleatoria: ";
             std::cin>>chute;
             
             achou=false;
             
             for(int i=0; i<tolletras; i++){
                 if(tolower(palavraSO[i])==tolower(chute)){
                     if (mascara[i]=='-'){
                        mascara[i]=palavraSO[i];
                        acertos++;
                        achou=true;
                     } 
                 }
             }
             
             if(!achou){
             erros++;
             tentativas--;
             std::cout<<"Esta letra nao tem na palavra\n";
    
                 if (erros == 1) {
                     std::cout << "  _______     \n";
                     std::cout << " |/      |    \n";
                     std::cout << " |       O    \n";
                     std::cout << " |            \n";
                     std::cout << " |            \n";
                     std::cout << " |            \n";
                     std::cout << "_|___         \n";
                 }
                
                 if (erros == 2) {
                    std::cout << "  _______     \n";
                     std::cout << " |/      |    \n";
                     std::cout << " |       O    \n";
                     std::cout << " |       |    \n";
                     std::cout << " |       |    \n";
                     std::cout << " |            \n";
                     std::cout << "_|___         \n";
                 }
                
                  if (erros == 3) {
                      std::cout << "  _______     \n";
                      std::cout << " |/      |    \n";
                      std::cout << " |       O    \n";
                      std::cout << " |      /|    \n";
                      std::cout << " |       |    \n";
                      std::cout << " |            \n";
                      std::cout << "_|___         \n";
                  }
                    
                  if (erros == 4) {
                      std::cout << "  _______     \n";
                      std::cout << " |/      |    \n";
                      std::cout << " |       O    \n";
                      std::cout << " |      /|\\  \n";
                      std::cout << " |       |    \n";
                      std::cout << " |            \n";
                      std::cout << "_|___         \n";
                  }
                   
                  if (erros == 5) {
                      std::cout << "  _______     \n";
                      std::cout << " |/      |    \n";
                      std::cout << " |       O    \n";
                      std::cout << " |      /|\\  \n";
                      std::cout << " |       |    \n";
                      std::cout << " |      /     \n";
                      std::cout << "_|___         \n";
                  }
                 
                  if (erros == 6) {
                      std::cout << "  _______     \n";
                      std::cout << " |/      |    \n";
                      std::cout << " |       O    \n";
                      std::cout << " |      /|\\  \n";
                      std::cout << " |       |    \n";
                      std::cout << " |      / \\  \n";
                      std::cout << "_|___         \n";

                  }
                } else {
                 std::cout<<"Acertou miseravi\n";
                }
                   
                if(acertos == tolletras){
                   std::cout<<"Parabens, voce acertou a palavra: "<<palavraSO<<"\n";
                }else{
                      
                 if(tentativas==0){
                        std::cout<<"Foi derrotado, a palavra era: "<<palavraSO<<"\n";
                 }
                }         
              }
          std::cout<<"Deseja continuar(S/N)?: ";
          std::cin>>r;          
          } 
	 return 0;
}
