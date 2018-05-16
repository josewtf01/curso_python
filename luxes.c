

// CONFIG1H
#pragma config FOSC = INTOSCIO  // Oscillator Selection (Internal oscillator)

// CONFIG2H
#pragma config WDTEN = OFF      // Watchdog Timer Enable bits (WDT disabled in hardware (SWDTEN ignored))
#pragma config WDTPS = 32768    // Watchdog Timer Postscaler (1:32768)
#include <xc.h>
#include "F:\\flex_lcd.h"
#include <delays.h>
#include <math.h>
#include <stdio.h>
#include <plib/adc.h>

float voltaje;

unsigned int i=0;
int axu ;
int luxes_fi;
float polinomio(float v);
int main(void) {
    //OSCCON = 0x33;

    TRISB=0;            // Configure Port B as output port
    ANSELB = 0x00;
    TRISD = 0;
    ANSELD = 0x00;
    TRISE = 0;
    ANSELE = 0x00;
    PORTB=0x00;
    PORTD=0x00;
    PORTE=0x00;



 OpenADC(ADC_FOSC_64 &
 ADC_LEFT_JUST &
 ADC_16_TAD,
 ADC_CH0 &
 ADC_INT_OFF &
 ADC_REF_VDD_VDD &
 ADC_REF_VDD_VSS,
 14);
 //Retardo de 50 Tcy
 Delay10TCYx(5);

    //inicializar pantalla
    while(1)
    {
 ConvertADC();
 while(BusyADC());
    axu = (ADRESH<<2)+(ADRESL>>6);

    voltaje = (5.0/1023.0)*axu;
    voltaje = 5.0 - voltaje;

luxes_fi = (int)polinomio(voltaje);
unsigned char lux[16] ;
sprintf(lux, "%d", luxes_fi);
Lcd_Init();     //inicializamos el lcd
Lcd_Cmd(LCD_CLEAR);     //limpiamos lcd
Lcd_Cmd(LCD_CURSOR_OFF);    //apagamos el cursor
__delay_ms(100);        //esperamos 100ms
Lcd_Out2(1, 1, lux);
Lcd_Out(2,4,"luxes");
    }

    return 0;
}

float polinomio(float v)
{   float cal;
    cal = -5.8022*pow(v,5);
    cal = cal + 103.7205*pow(v,4);
    cal = cal -740.6238*pow(v,3);
    cal = cal + 2689.5423*pow(v,2);
    cal = cal - 5167.9907*v;
    cal = cal + 4482.3913;
    return cal;
}
// https://mkmekatronika.wordpress.com/2013/06/23/6-curso-xc8-manejo-de-lcd/
// https://electrosome.com/adc-pic-microcontroller-mplab-xc8/
// https://en.wikipedia.org/wiki/Bitwise_operations_in_C
// https://unasguiasmas.com/2014/07/03/03-conversion-de-analogico-a-digital-con-libreria-adc-h-de-c18/
// https://stackoverflow.com/questions/19952200/scanf-printf-double-variable-c
// https://unasguiasmas.com/2014/03/20/01-libreria-xlcd-para-el-manejo-de-displays-lcd/
// http://ww1.microchip.com/downloads/en/DeviceDoc/MPLAB_C18_Libraries_51297f.pdf
// https://www.youtube.com/watch?v=FHfUyxJ-uj0&t=6s
// http://picguides.com/beginner/adc.php
// https://en.wikipedia.org/wiki/Hitachi_HD44780_LCD_controller
// https://www.sparkfun.com/datasheets/LCD/HD44780.pdf
// https://www.youtube.com/watch?v=hZRL8luuPb8&t=2s
// https://robosumo.wordpress.com/2013/03/26/understanding-timing-and-delays-on-the-pic18f4620/
// https://need4bits.wordpress.com/2012/06/30/simulacion-en-mplab-ide/
// https://need4bits.wordpress.com/2012/08/02/simulacion-en-isis-proteus/
// https://need4bits.wordpress.com/2012/08/18/asmp04_control-de-un-lcd-pic18f4550-asm/
// http://picfernalia.blogspot.mx/2012/07/conversor-adc.html
// http://www.cplusplus.com/reference/cstdio/sprintf/
// https://www.sparkfun.com/datasheets/LCD/ADM1602K-NSW-FBS-3.3v.pdf
//
//
