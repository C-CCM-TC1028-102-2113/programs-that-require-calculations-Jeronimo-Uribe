def main():
    #escribe tu código abajo de esta línea
    pass

   #Peso
pesoi=float(input('Dame el peso inicial: '))
pesof=float(input('Dame el peso final: '))
meses=int(input('Dame la cantidad de meses: '))
pesob=pesoi-pesof
pesobm=pesob/meses
print('Lo que debes bajar por mes es: %0.2f' %pesobm) 

if __name__ == '__main__':
    main()
