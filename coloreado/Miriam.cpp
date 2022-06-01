#include  <cstdlib> 
#include  <iostream> 
#include  <conio.h> 
#include  <windows.h> 
#include  <stdio.h> 
#include  <stdlib.h> 
#define vertices 500
#define nodos 300

using namespace std;

struct  orden{
int  grado; //representa el numero  de conexiones
int  color; // representa el valor del numero
int  n;  //representa el numero  de vertice 
};
typedef struct  orden ver;

int B[nodos];//,ad[vertices][vertices];

//Ordenamos Mediante el Metodo de Ordenacion: Inserccion
void OrdenarMayaMen(int n, ver v[])
{
    int i,k;
    int aux,aux1;
    for(i=1;i < n;i++)
    {
            aux=v[i].grado;
            aux1=B[i];
            k=i-1;
            while(k >=0 && aux > v[k].grado)
            {
                v[k+1].grado=v[k].grado;
                B[k+1]=B[k];
                k=k-1;
            }
            v[k+1].grado=aux;
            B[k+1]=aux1;
    }
}

void IngresarMatriz(int ad[][vertices],int nds, int arst)//Es  para guardar la matriz de  Adyacencias :P
{   
  int i,j,nodoi,nodof; 
  
  for(i=0;i < nds;i++)
   { for(j=0;j < nds;j++)
        { ad[i][j]=0;}
   }
   
  //Llenamos la  matriz
  for(i=0;i < arst;i++)  
   { cout << "\n\n\tArista " << i+1 << "\n";
     cout << "\tN. inicio: ";
     cin >> nodoi;
     cout << "\tN. termino: ";
     cin >> nodof;   
     
     ad[nodoi-1][nodof-1]=1;
     ad[nodof-1][nodoi-1]=1;
   } 
  
   //Matriz de Adyacencia    
  /* for(i=0;i < nds;i++)
     { for(j=0;j < nds;j++)
         ad[i][j]=ad[i][j]; 
     
      }*/
}


void Greedy(int ad[][vertices],int nds)//,int  ad[vertices][vertices])
{ 
  ver v[nds];
  int i,j,aux,zz,max=1;   

  //Etapa de  Coloracion
   for(i=0;i < nds;i++)
    {v[i].color=1;
     zz=0;
     aux=1;
     while(aux==1)
      {for(j=0;j < nds;j++)
         { if(ad[j][i]==1)
            {if(v[i].color==v[j].color)
               { zz=1;}
            }
         }
         if(zz==1)
           {aux=1;
            zz=0;
            v[i].color++;
           }
         else
            {aux=0;}
            if(v[i].color   >   max)
              { max=v[i].color;}
       }
     }

  cout << "\n\tAlgoritmo Voraz \n" << "\tmaxcolor= " << max << "\n";

  //Se imprime el  conjunto de  vertices  de  cada color    
  for(i=0;i < max;i++)
  {printf("\t  %c= { ",'a'+i);
    for(j=0;j < nds;j++)
     { if(v[j].color==i+1)
         cout << " " << j+1;        
     }
    cout << "  }\n";
  }

}



int main(int argc, char *argv[])
{
  int i,j,cant_nodos,cant_aristas,ad[vertices][vertices];
  char s,N,n;
  do{  
  cout << "\n\t\tCOLOREADO DE GRAFOS\n";

  cout << "\n\n\t Ingrese Datos \n"; 
  cout << "\n\t Numuero de Nodos: ";
  cin >> cant_nodos;
  cout << "\t Cantidad de Aristas: ";
  cin >> cant_aristas;  
  
  //Aqui se  crea la matriz de  adyacencia
  IngresarMatriz(ad,cant_nodos,cant_aristas);//,ad);
    
  //Se colorea vertice  a  vertice en  el  orden inicial
  Greedy(ad,cant_nodos);//,ad);
  
 cout << "\n\tSi desea continuar presione cualquier tecla \n\tSi no escriba 'n' o 'N': ";
 s=getch();
 system("cls");
  }while(s!='N' && s!='n');
 cout << "Hasta Luego!!!!";
 Sleep(1600);
 exit(0);    
  
 cout << "\n\n";
 system ("PAUSE");
}
