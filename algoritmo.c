#include<stdio.h>

int main()
{
int luxes[101];
float voltajes[51];
unsigned int i = 0;

for (i=0;i<51;i++){luxes[i] = i *10;}

voltajes[0] = 5.0;
voltajes[1] = 4.53;
voltajes[2] = 4.22;
voltajes[3] = 3.96;
voltajes[4] = 3.74;
voltajes[5] = 3.55;
voltajes[6] = 3.38;
voltajes[7] = 3.24;
voltajes[8] = 3.1;
voltajes[9] = 2.98;
voltajes[10] = 2.87;
voltajes[11] = 2.77;
voltajes[12] = 2.68;
voltajes[13] = 2.59;
voltajes[14] = 2.51;
voltajes[15] = 2.44;
voltajes[16] = 2.37;
voltajes[17] = 2.31;
voltajes[18] = 2.25;
voltajes[19] = 2.19;
voltajes[20] = 2.13;
voltajes[21] = 2.08;
voltajes[22] = 2.04;
voltajes[23] = 1.99;
voltajes[24] = 1.95;
voltajes[25] = 1.9;
voltajes[26] = 1.86;
voltajes[27] = 1.83;
voltajes[28] = 1.79;
voltajes[29] = 1.76;
voltajes[30] = 1.72;
voltajes[31] = 1.69;
voltajes[32] = 1.66;
voltajes[33] = 1.63;
voltajes[34] = 1.6;
voltajes[35] = 1.58;
voltajes[36] = 1.55;
voltajes[37] = 1.53;
voltajes[38] = 1.5;
voltajes[39] = 1.48;
voltajes[40] = 1.46;
voltajes[41] = 1.43;
voltajes[42] = 1.41;
voltajes[43] = 1.39;
voltajes[44] = 1.37;
voltajes[45] = 1.35;
voltajes[46] = 1.34;
voltajes[47] = 1.32;
voltajes[48] = 1.3;
voltajes[49] = 1.28;
voltajes[50] = 1.27;
float voltaje;
voltaje = 3.6461;
voltaje = 5.0 - voltaje;
int indice = 0;
for(i=0;i<51;i++){
    if(voltaje > voltajes[i]){
        indice = i;
        break;
    }
}
float calculo;
calculo = ((voltaje*(i*20)/voltajes[i])+(voltaje*((i-1)*20)/voltajes[i-1]))/2;
printf("%f \n",calculo);
int luxes_fi;
luxes_fi = (int)calculo;
printf("%d\n",luxes_fi);
return 0;
}
