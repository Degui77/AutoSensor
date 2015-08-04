#!/usr/bin/python
# -*- coding:utf-8 -*-

def fin_sc_ino(num):
	arduino_ino = open('arduino_script'+num+'.ino','a')
	arduino_ino.write(""" 
}; //etiquetas --> campo "nombre"

int pines[] = {***}; // pines anaógicos--> configurado por el usuarios
		     //Ej. int pines[] = {0, 1, 2};

int nsenact = sizeof(pines)/sizeof(int);

void setup() {
  Serial.begin(19200); // baudrate  19200 

  /*añadir inicilizacion si fuese necesarios de pines digitales*/

}

float lectura (int pin){
  float tmp = 0;
  
  float r = analogRead(pin);
  
  /*Apartir de aqui lo tiene que implementar 
  para ajustarse a la funcionalidad*/
  
  /*para separar las distintas operaciones serparar conclusulas if*/ 
  
  //Ej. Para un sensor de temperatura LM35:
  if (pin == A0) {
    return 5.0/1024*r*100;
  }

  if (pin == A2){
	r = analogRead(A2);
	return ((long)r*1000*10)/((long)15*10*(1024-r)); 
  } 

   return tmp;
}

void loop() {
  
    if (Serial.available() > 0){
      String msg = Serial.readStringUntil('\\n');
      
      for (int i = 0; i < nsenact; i++){
        if (etiqueta[i] == msg){
          Serial.print(String(lectura(pines[i]))+'\\n');
        }
     }
  }

}
""")
	arduino_ino.close()
	
