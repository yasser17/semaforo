const int boton = 2, roja = 3, amarilla = 4, verde = 5, timbre = 6;
const int tiempoAntirebote = 10;
unsigned long milisAnterior = 0, intervalo = 2000;

int contador = 0;
int estadoBoton;
int estadoBotonAnterior;
int estadoLuzRoja = 0, estadoLuzAmarilla = 0, estadoLuzVerde = 0;

boolean antirebote(int pin)
{
  boolean estado;
  boolean estadoAnterior;

  do {
    estado = digitalRead(pin);
    if(estado != estadoAnterior) 
    {
      contador = 0;    
      estadoAnterior = estado;
    }else{
      contador++;
    }
    delay(1);
  } while(contador < tiempoAntirebote);
  return estado;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(roja, OUTPUT);
  pinMode(amarilla, OUTPUT);
  pinMode(verde, OUTPUT);
  pinMode(timbre, OUTPUT);
  pinMode(boton, INPUT);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  digitalWrite(roja, LOW);
  digitalWrite(timbre, HIGH);
  estadoLuzRoja = 1;
  digitalWrite(amarilla, HIGH);
  digitalWrite(verde, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long milisAhora = millis();
  
  if(Serial.available() != 0)
  {
    char valor = Serial.read();
    if(valor == 'P')
    {
      digitalWrite(roja, HIGH);
      digitalWrite(amarilla, HIGH);
      digitalWrite(verde, HIGH);
      estadoLuzRoja = 0;
      estadoLuzAmarilla = 0;
      estadoLuzVerde = 0;
      delay(2000);
      digitalWrite(roja, LOW);
      estadoLuzRoja = 1;
    }
    if(valor == 'R')
    {
      digitalWrite(roja, HIGH);
      digitalWrite(amarilla, HIGH);
      digitalWrite(verde, HIGH);
      estadoLuzRoja = 0;
      estadoLuzAmarilla = 0;
      estadoLuzVerde = 0;
      delay(1000);
      digitalWrite(roja, LOW);
      digitalWrite(timbre, LOW);
      delay(1000);
      digitalWrite(roja, HIGH);
      digitalWrite(timbre, HIGH);
      delay(500);
      digitalWrite(roja, LOW);
      digitalWrite(timbre, LOW);
      delay(1000);
      digitalWrite(roja, HIGH);
      digitalWrite(timbre, HIGH);
      delay(500);
      digitalWrite(roja, LOW);
      digitalWrite(timbre, LOW);
      delay(1000);
      digitalWrite(roja, HIGH);
      digitalWrite(timbre, HIGH);
      delay(500);
      digitalWrite(roja, LOW);
      delay(1000);
      digitalWrite(roja, HIGH);
      delay(500);
      digitalWrite(roja, LOW);
      delay(1000);
      digitalWrite(roja, HIGH);
      delay(500);
      digitalWrite(roja, LOW);
      delay(1000);
      digitalWrite(roja, HIGH);
      delay(500);
      digitalWrite(roja, LOW);
      delay(1000);
      digitalWrite(roja, HIGH);
      delay(500);
      digitalWrite(roja, LOW);
      delay(1000);
      digitalWrite(roja, HIGH);
      delay(500);
      digitalWrite(roja, LOW);
      delay(1000);
      digitalWrite(roja, HIGH);
      delay(500);
      digitalWrite(roja, LOW);
      delay(1000);
      digitalWrite(roja, HIGH);
    }
    if(valor == 'A')
    {
      digitalWrite(roja, HIGH);
      digitalWrite(amarilla, HIGH);
      digitalWrite(verde, HIGH);
      estadoLuzRoja = 0;
      estadoLuzAmarilla = 0;
      estadoLuzVerde = 0;
      delay(1000);
      digitalWrite(amarilla, LOW);
      digitalWrite(timbre, LOW);
      delay(1000);
      digitalWrite(amarilla, HIGH);
      digitalWrite(timbre, HIGH);
      delay(500);
      digitalWrite(amarilla, LOW);
      digitalWrite(timbre, LOW);
      delay(1000);
      digitalWrite(amarilla, HIGH);
      digitalWrite(timbre, HIGH);
      delay(500);
      digitalWrite(amarilla, LOW);
      digitalWrite(timbre, LOW);
      delay(1000);
      digitalWrite(amarilla, HIGH);
      digitalWrite(timbre, HIGH);
      delay(500);
      digitalWrite(amarilla, LOW);
      delay(1000);
      digitalWrite(amarilla, HIGH);
      delay(500);
      digitalWrite(amarilla, LOW);
      delay(1000);
      digitalWrite(amarilla, HIGH);
      delay(500);
      digitalWrite(amarilla, LOW);
      delay(1000);
      digitalWrite(amarilla, HIGH);
      delay(500);
      digitalWrite(amarilla, LOW);
      delay(1000);
      digitalWrite(amarilla, HIGH);
      delay(500);
      digitalWrite(amarilla, LOW);
      delay(1000);
      digitalWrite(amarilla, HIGH);
      delay(500);
      digitalWrite(amarilla, LOW);
      delay(1000);
      digitalWrite(amarilla, HIGH);
      delay(500);
      digitalWrite(amarilla, LOW);
      delay(1000);
      digitalWrite(amarilla, HIGH);
    }
    if(valor == 'V')
    {
      digitalWrite(roja, HIGH);
      digitalWrite(amarilla, HIGH);
      digitalWrite(verde, HIGH);
      estadoLuzRoja = 0;
      estadoLuzAmarilla = 0;
      estadoLuzVerde = 0;
      delay(1000);
      digitalWrite(verde, LOW);
      digitalWrite(timbre, LOW);
      delay(1000);
      digitalWrite(verde, HIGH);
      digitalWrite(timbre, HIGH);
      delay(500);
      digitalWrite(verde, LOW);
      digitalWrite(timbre, LOW);
      delay(1000);
      digitalWrite(verde, HIGH);
      digitalWrite(timbre, HIGH);
      delay(500);
      digitalWrite(verde, LOW);
      digitalWrite(timbre, LOW);
      delay(1000);
      digitalWrite(verde, HIGH);
      digitalWrite(timbre, HIGH);
      delay(500);
      digitalWrite(verde, LOW);
      delay(1000);
      digitalWrite(verde, HIGH);
      delay(500);
      digitalWrite(verde, LOW);
      delay(1000);
      digitalWrite(verde, HIGH);
      delay(500);
      digitalWrite(verde, LOW);
      delay(1000);
      digitalWrite(verde, HIGH);
      delay(500);
      digitalWrite(verde, LOW);
      delay(1000);
      digitalWrite(verde, HIGH);
      delay(500);
      digitalWrite(verde, LOW);
      delay(1000);
      digitalWrite(verde, HIGH);
      delay(500);
      digitalWrite(verde, LOW);
      delay(1000);
      digitalWrite(verde, HIGH);
      delay(500);
      digitalWrite(verde, LOW);
      delay(1000);
      digitalWrite(verde, HIGH);
    }
  }
  
  estadoBoton = digitalRead(boton);
  if(estadoBoton != estadoBotonAnterior)
  {
    if(antirebote(boton))
    {
        Serial.println("pulsacion");
    }
  }
  estadoBotonAnterior = estadoBoton;

  if(milisAhora - milisAnterior > intervalo)
  {
    
    milisAnterior = milisAhora;
    if(estadoLuzRoja == 1)
    {
      digitalWrite(roja, HIGH);
      digitalWrite(amarilla, LOW);
      estadoLuzRoja = 0;
      estadoLuzAmarilla = 1;
    }else if ( estadoLuzAmarilla == 1 )
    {
      digitalWrite(amarilla, HIGH);
      digitalWrite(verde, LOW);
      estadoLuzAmarilla = 0;
      estadoLuzVerde = 1;
    }else{
      digitalWrite(verde, HIGH);
      digitalWrite(roja, LOW);
      estadoLuzVerde = 0;
      estadoLuzRoja = 1;
    }
  }
}

