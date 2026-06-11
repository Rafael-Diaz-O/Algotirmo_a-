class BaseDeConocimiento: 

 def __init__(self):
    self.hechos = []
    delf.reglas = []

 def  agregar_hecho(self,hecho):
   self.hechos.append(hecho)

 def agregar_regla(self,condicion,conclusion):
   self.reglas.append((condicion,conclusion))  

class SistemaExperto:
  
 def __init__(self,base_conocimiento):
  self.base_conocimiento = base_conocimiento

 def inferir(self):
   nuevos_hechos = True
   while nuevos_hechos:
     nuevos_hechos = False 
     for condicion, conclusion in self.base_conocimiento.reglas:
       if all(hecho in self.base_conocimiento.hechos for hecho in condicion):
         if conclusion not in self.base_conocimiento.hechos: 
           self.base_conocimiento.hechos.append(conclusion)
           nuevos_hechos = True  

#Creando la base de conocimientos 
base = BaseDeConocimiento()

#Agregando hechos 
base.agregar_hecho("Fierbre alta")
base.agregar_hecho("tos")

#Agregando reglas 
base.agregar_regla(["fierbre alta","tos"],"ifección respiratoria")
base.agregar_regla(["infeccion respiraoria","dificultad para respirar"],"neumonía")

#Creando el sistema experto 
sistema = SistemaExperto(base)

#Ejecutando la inferencia 
sistema.inferir()

#Mostrando los hechos actualizados 
print("Hechos inferidos:")
print(base.hechos)

