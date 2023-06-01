
def dias_clase(inicio,fin):
    return  [15,20,20,18,17]# Devuelve la cantidad de dias de clase
                            # ordenados de lu a vi por consulta automatica a calendario
                            # el usuario tiene que poder agregar dias no laborables



def calcular(dias_cursada, dias_disponibles, duracion_catedra):   # Calcula todas las combinaciones de dias y                       
    if solucion.count([0,0,0,0,0,0,0,1,1])!=0:   
        solucion.remove([0,0,0,0,0,0,0,1,1]) 
    if dias_cursada==1:                                           # horarios que cumplen y lo guarda en solucion
        for i in range(0,5):            # Prueba de lu a vi
            if (dias_disponibles[i]*1.5*4)>= duracion_catedra:                
                for n in range(4,0,-1):         #Voy bajando la cantidad de horas catedra hasta dar con el minimo
                    if (dias_disponibles[i]*1.5*n)>= duracion_catedra:
                        n-=1
                    else:
                        break                       
                horas_clase=n+1                 # Cantidad minima de horas de clase para 1 dia por semana                
                aprovechamiento=duracion_catedra/(dias_disponibles[i]*1.5* horas_clase)     # Horas de materia/horas de clase
                vector=[0,0,0,0,0,horas_clase,aprovechamiento,dias_cursada,cuatrimestres]          
                vector[i]=1
                solucion.append(vector)                                 #Cargo la nueva solucion hallada
                
   
    if dias_cursada==2:                                           # Calculo para 2 dias
        for i in range(0,4):            # Prueba de lu a ju
            for j in range(i+1,5):      # De ma a vi
                if ((dias_disponibles[i]+dias_disponibles[j])*1.5*4)>= duracion_catedra:                
                    for n in range(4,0,-1):         #Voy bajando la cantidad de horas catedra hasta dar con el minimo
                        if ((dias_disponibles[i]+dias_disponibles[j])*1.5*n)>= duracion_catedra:
                            n-=1
                        else:
                            break                       
                    horas_clase=n+1                 # Cantidad minima de horas de clase para 2 dias por semana                
                    aprovechamiento=duracion_catedra/((dias_disponibles[i]+dias_disponibles[j])*1.5*horas_clase)    # Horas de materia/horas de clase
                    vector=[0,0,0,0,0,horas_clase,aprovechamiento,dias_cursada,cuatrimestres]          
                    vector[i]=1
                    vector[j]=1
                    solucion.append(vector)                                 #Cargo la nueva solucion hallada      
    
    if dias_cursada==3:                                           # Calculo para 3 dias por semana
        for i in range(0,3):            # Prueba de lu a mi
            for j in range(i+1,4):      # de ma a ju
                for k in range(j+1,5):  # de mi a vi
                    if ((dias_disponibles[i]+dias_disponibles[j]+dias_disponibles[k])*1.5*4)>= duracion_catedra:                
                        for n in range(4,0,-1):         #Voy bajando la cantidad de horas catedra hasta dar con el minimo
                            if ((dias_disponibles[i]+dias_disponibles[j]+dias_disponibles[k])*1.5*n)>= duracion_catedra:
                                n-=1
                            else:
                                break                       
                        horas_clase=n+1                 # Cantidad minima de horas de clase para 3 dias por semana                
                        aprovechamiento=duracion_catedra/((dias_disponibles[i]+dias_disponibles[j]+dias_disponibles[k])*1.5*horas_clase)    # Horas de materia/horas de clase
                        vector=[0,0,0,0,0,horas_clase,aprovechamiento,dias_cursada,cuatrimestres]          
                        vector[i]=1
                        vector[j]=1
                        vector[k]=1
                        solucion.append(vector)                                 #Cargo la nueva solucion hallada             
                
    if dias_cursada==4:                                           # Calculo para 4 dias por semana
        for i in range(0,2):                # Prueba de lu a ma
            for j in range(i+1,3):          # de ma a mi
                for k in range(j+1,4):      # de mi a ju
                    for l in range(k+1,5):  # de ju a vi
                        if ((dias_disponibles[i]+dias_disponibles[j]+dias_disponibles[k]+dias_disponibles[l])*1.5*4)>= duracion_catedra:                
                            for n in range(4,0,-1):         #Voy bajando la cantidad de horas catedra hasta dar con el minimo
                                if ((dias_disponibles[i]+dias_disponibles[j]+dias_disponibles[k]+dias_disponibles[l])*1.5*n)>= duracion_catedra:
                                    n-=1
                                else:
                                    break                       
                            horas_clase=n+1                 # Cantidad minima de horas de clase para 3 dias por semana                
                            aprovechamiento=duracion_catedra/((dias_disponibles[i]+dias_disponibles[j]+dias_disponibles[k]+dias_disponibles[l])*1.5*horas_clase)    # Horas de materia/horas de clase
                            vector=[0,0,0,0,0,horas_clase,aprovechamiento,dias_cursada,cuatrimestres]          
                            vector[i]=1
                            vector[j]=1
                            vector[k]=1
                            vector[l]=1
                            solucion.append(vector)                                 #Cargo la nueva solucion hallada      
                            
                            
    if  dias_cursada==5:        # Hay una sola posibilidad de lu a vi todos los dias
        if (sum(dias_disponibles) *1.5*4)>= duracion_catedra:  
            for n in range(4,0,-1):         #Voy bajando la cantidad de horas catedra hasta dar con el minimo
                if (sum(dias_disponibles) *1.5*n)>= duracion_catedra:
                    n-=1
                else:
                    break                       
            horas_clase=n+1     
            aprovechamiento=duracion_catedra/ (sum(dias_disponibles) *1.5*horas_clase)
            vector=[1,1,1,1,1,horas_clase,aprovechamiento,dias_cursada,cuatrimestres]                
            solucion.append(vector) 




                                        #Inicializacion 
determinacion_dias=False
dias_disponibles=[0,0,0,0,0]
cuatrimestres =1
dias_cursada =1
dias=["Lu","Ma","Mi","Ju","Vi"]
horas_clase =0
aprovechamiento=0
solucion=[[0,0,0,0,0,horas_clase,aprovechamiento,dias_cursada,cuatrimestres]]  


duracion_reloj=int(input("Ingrese la cantidad de horas reloj de la materia      "))
duracion_catedra= duracion_reloj * 1.5
while determinacion_dias==False:     # Si todavia no se cual es la cantidad minima de dias en que se puede dar la materia
    inicio=input("Ingrese la fecha de inicio del cuatrimestre       ")
    fin=input("Ingrese la fecha de fin del cuatrimestre     ")    
    
    
    dias_disponibles =[dias_clase(inicio,fin)[i] + dias_disponibles[i] for i in range(0,5) ] # Calculo cuantos dias de calse que
                                                                                             # hayteniendo en cuenta la cantidad de
                                                                                             # cuatrimestres
                                                             
    horas_disponibles= max(dias_disponibles)*1.5 *4 # Horas catedra del dia de la                                                      
                                                    # semana que tiena mas dias laborables
    dias_calculo=[0,0,0,0,0]
    # for i in range(0,5):                                        # Auxiliar
    #     dias_calculo[i]= dias_disponibles[i]
    dias_calculo=[dias_disponibles[i] for i in range(0,5) ]
    dias_calculo.pop(dias_calculo.index(max(dias_calculo)))     # De la lista de dias saco el dia que estoy tomando en cuenta
    
   
    while dias_cursada<=5:                          # Si con un dia no alcanza voy sumando de mayor a menor los dias de la semana 
        if horas_disponibles >= duracion_catedra:  # que quedan a ver si puedo cubrir las hora de clase
            determinacion_dias=True  
            break
        else:
            dias_cursada +=1                                                                                    
            if len(dias_calculo)>=1:    #Para no querer sacar el max de una lista vacia
                horas_disponibles = horas_disponibles + max(dias_calculo)*1.5 *4 # Le sumo las horas del dia del la semana con mas dias #
                dias_calculo.pop(dias_calculo.index(max(dias_calculo)))    # entre los dias que restan y lo saco de la lista de dias    
    else:                                                   # Si no me alcanza con todos los dias de la semana sumo otro cuatrimestre
        print(f"La materia no se puede dar en {cuatrimestres} cuatrimestres, ingrese las fechas para el proximo cuatrimiestre")
        cuatrimestres +=1
        dias_cursada=1

print(dias_cursada,cuatrimestres)   # Para probar calculo

# Con los minimos ya definidos calculo las posibles combinaciones
                                #Cargo la nueva solucion hallada
                
                   #presentacion resultados
for h in range(dias_cursada,6):
    calcular(h, dias_disponibles, duracion_catedra)
extender_busqueda=input("Ingrese Si si desea extender la busqueda un cuatrimestre mas   ")
if extender_busqueda=="Si":
    cuatrimestres+=1
    inicio=input("Ingrese inicio del proximo cuatrimestre")
    fin=input("Ingrese el fin del proximo cuatrimeestre")
    dias_disponibles=[dias_disponibles[i]+dias_clase(inicio,fin)[i]for i in range(0,5)]
    for h in range(1,6):
        calcular(h, dias_disponibles, duracion_catedra)
print (solucion)




# Borrar la solucion [0000000]  




