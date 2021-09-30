from decorador import guardar_logs
from interfaz import object


class Animal(object):
         Mascota = 'Perro'
    
         def __init__(self, nombre = 'Shannell', edad = 2):
          self.nombre = nombre
          self.edad = edad
          
         @guardar_logs 
         def datos(self):
            print('mascota:', Animal.Mascota) 
            print ('nombre:', self.nombre)
            print ('Edad:', self.edad)
            
         @guardar_logs 
         
         def Tipo_mascota(self):
            print('perro', self)
                
            return self.Mascota
        
         @classmethod
         def Color(self):
           print('mono', self)
           
         @classmethod
         def Genero(self):
           print('femenino', self)
                  
        
         @staticmethod
         def Raza(raza):
                print ('es de raza', raza)
                
                if __name__ == "__Animal__":    
                # Llame al método de instancia, primero instancie la clase
                        info=Animal()
                        info.datos()
                        print(Animal.Tipo_mascota())
                
         
         
Animal.Raza('Pincher')  





 
        
         
            


 