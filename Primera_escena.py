from manimlib.imports import *
import numpy as np 
#podemos hacer una instancia de la clase camara y modificarla o añadir artibutos y metodos
#y usarla como si fuera la clase real que teniamos 
#o podemos codificar directamente la configuracion de la camara en la configuracion de la escena
#los archivos de configuracion se van acumulando o sobreescribiendo, pero no se sustituyen

#JUNTAMOS TODO CON ffmpeg -f concat -safe 0 -i files.txt -c copy presentacion.mp4


#applymethod va a ser muy util para poder hacer diferentes trasnformaciones en mobjects (basicamente es aplicar un metodo de mobject, pero animar la transicion)

class micamara(Camera):
    CONFIG={"background_color":BLACK}

class Primer_frame(Scene):
    def construct(self):

        titulo1=TextMobject("La entropía como creadora","de orden")
        titulo1.scale(1.5)
        formula1=TexMobject(r"S=k \log{\Omega}",height=1.07)
        titulo1[0].move_to(3*UP)
        titulo1[1].next_to(titulo1[0],DOWN*1.5)
        formula1.move_to(1.7*DOWN)
        self.add(titulo1)
        self.add(formula1)
        self.wait(3)


class Primera_escena(Scene):

    #CONFIG={"camera_config": {"background_color":WHITE}}
    CONFIG={"camera_class": micamara}
    def construct(self):
        DecimalNumber
        titulo1=TextMobject("La entropía como creadora","de orden")
        titulo1.scale(1.5)
        formula1=TexMobject(r"S=k \log{\Omega}",height=1.07)
        
        titulo1[0].move_to(3*UP)
        titulo1[1].next_to(titulo1[0],DOWN*1.5)
        formula1.move_to(1.7*DOWN)
        #creo que es posible aplicar a un vgroup una transformacion tal que se ejecute en cada uno de ellos
        self.add(titulo1)
        self.add(formula1)
        self.wait(3)
        #titulo=VGroup(titulo1,titulo2)
        conceptos=TextMobject("Conceptos")
        conceptos.move_to(3*UP)
        #el play se llama una vez tras de otra si queremos hacer varias cosas a la vez las tenemos que meter dentro del mismo play
        self.play(Transform(titulo1,conceptos),FadeOutAndShiftDown(formula1))
        #self.play(FadeOutAndShiftDown(formula1))
        linea=Line(start=2*LEFT,end=2*RIGHT)
        linea.next_to(conceptos,DOWN)
        self.play(FadeInFromDown(linea))
        self.wait(3)

        #ahora ponemos lo que vamos a revisar
        sub_apats=TextMobject("- Concepto de entropía.","- Energía libre.","- Interacción Entrópica.")

        
        posicion_aux= 4*LEFT+2*UP  
        sub_apats[0].move_to(posicion_aux)           
        for i in range(2): 
            sub_apats[i+1].next_to(sub_apats[i].get_corner(DOWN+LEFT),DOWN*4, aligned_edge=LEFT)

        uno_mas=TextMobject("- Conclusiones")
        #aligned edge hace que lo que se aplica se aplice respecto de una esquina
        #cada mobject tiene una caja que lo contiene y podemos obtener sus coordenadas
        uno_mas.next_to(sub_apats[2].get_corner(DOWN+LEFT),DOWN*4,aligned_edge=LEFT)
        for i in range(3):
            self.play(FadeInFromLarge(sub_apats[i]))
            self.wait(0.6)
        self.play(FadeInFromLarge(uno_mas))
        self.wait(4)
        #en mobjects se gardan todos los objetos de la escena
        self.play(*[FadeOut(i) for i in self.get_mobjects()])
        self.wait(2)
        

class Segunda_escena(Scene):

    def construct(self):
        titulo=TextMobject("Referencias")    
        titulo.to_edge(UP)    
        linea=Line(start=2*LEFT,end=2*RIGHT)
        linea.next_to(titulo,DOWN)
        articulo=ImageMobject("articulo_main1.png")
        articulo.scale(1.5)
        titulo1=TextMobject("La entropía como creadora de orden.")
        #titulo1.scale(0.6)
        autor1=TextMobject(r"José A. Cuesta")
        #autor1.scale(0.6)

        articulo.to_edge(LEFT,buff=2)
        titulo1.next_to(articulo,DOWN)
        autor1.next_to(titulo1,DOWN)
        recurso1=VGroup(titulo1,autor1)
        recurso1.scale(0.6)
        cuantumfrac=ImageMobject("thumbnail1.png")
        cuantumfrac.scale(1.3)
        titulo2=TextMobject("El cristal que se alimenta de entropía.")
        #titulo2.scale(0.6)
        autor2=TextMobject("Quantum Fracture")
        #autor2.scale(0.6)
        cuantumfrac.to_edge(RIGHT,buff=2)
        titulo2.next_to(cuantumfrac,DOWN)
        autor2.next_to(titulo2,DOWN)
        recurso2=VGroup(titulo2,autor2)
        recurso2.scale(0.6)

        self.wait(1)
        self.play(FadeIn(titulo),FadeInFromDown(linea))
        self.wait(1.5)
        self.play(FadeInFrom(articulo,direction=RIGHT),Write(recurso1))#,Write(autor1))
        self.wait(3)
        self.play(FadeInFrom(cuantumfrac,direction=LEFT),Write(recurso2))#,Write(autor2))
        self.wait(3)
        end_scene(self)
        self.wait(1)

    
class Tercera_escena(Scene):
    #queremos explicar el concepto de entropía como número de estados microscópicos compatibles
    #con nuestro sistema macroscopico. Para hacer esto vamos a mostrar mediante espines,flechas, 
    #que nuestro sistema sin restricciones va a evolucionar hacie el estado que le proporciona un mayor 
    #numero de estados libres (mas libertad). Si tenemos restricciones entonces tenemos que tener en cuenta que 
    #primero viene el complir con los requisitos de las restricciones y luego la entropia, es decir,
    #si tenemos un restriccion como que la suma final de flechas up sea 200 o mas, pues habra muchas posibilidades (201,202), pero
    #estamos restringidos y si hay 800 flechas el valor seguramente sea mayor y no pase nada, pero si hay 203 flechas, la restricción
    #nos lleva a un estado muy "artificial" que cumplira con la maximizacion de la entropia pero bajo esas restricciones
    def construct(self):
        grid=[]
        num_vects=0
        #point.move_to([2,2,0])
        #lo que vamos a hacer es crear un vector de vectores 4 x 3
        for i in range(-3,4):
            for j in range(-2,3):
                aux=Vector(UP,stroke_width=7)
                aux.scale(0.5)
                aux.set_color(RED)
                aux.move_to([i,j,0])
                grid.append(aux)
                num_vects+=1

        rectangle = Rectangle(height=5, width=7)
        #creamos el vmobject
        colect=VGroup(*grid,rectangle)
        self.play(Write(colect, run_time=6))
        valor_B=100
        campo_B=TexMobject("B="+str(valor_B))
        campo_B.move_to([-4.5,3.5,0])
        self.play(Write(campo_B))
        #digamos que tenemos un sistema y segun nuestras restricciones quiza un campo magnetico, se encuentra en un estado como este
        #si empezamos a relajar el campo magnetico
        self.wait(2)
        valor_B=0
        campo_B_2=TexMobject("B="+str(valor_B))
        campo_B_2.move_to([-4.5,3.5,0])
        self.play(Transform(campo_B,campo_B_2))

        for i in range(num_vects):
            if(random.random()<0.6):
                
                self.play(ApplyMethod(colect[i].rotate,PI,run_time=0.5))
                colect[i].set_color(BLUE)
        self.wait(2)
        self.play(ApplyMethod(colect.scale,0.2))
        self.play(ApplyMethod(colect.shift,[-5,2.5,0],run_time=0.7))
        self.wait(2)
        for i in range(5):
            if(i!=0):
                self.play(ApplyMethod(colect.shift,DOWN*1.7,run_time=0.2))
            for j in range(0,7,1):
                colect_aux=colect.copy()
                colect_aux.move_to(colect.get_center()+RIGHT*2*j)
                self.play(Transform(colect.copy(),colect_aux,run_time=0.2))
        self.wait(3)
        end_scene(self)
        self.wait()
        #colect_aux=colect.copy()
        #colect_aux.move_to([-4.5,3.5,0])
        #colect=colect_aux.copy()
        #colect_aux.move_to([-4.5,3.5,0]+2*DOWN)
#
        #self.play(Transform(colect,colect_aux))

class Frame_todo_alig(Scene):

    def construct(self):
        grid=[]
        num_vects=0
        #point.move_to([2,2,0])
        #lo que vamos a hacer es crear un vector de vectores 4 x 3
        for i in range(-3,4):
            for j in range(-2,3):
                aux=Vector(UP,stroke_width=7)
                aux.scale(0.5)
                aux.set_color(RED)
                aux.move_to([i,j,0])
                grid.append(aux)
                num_vects+=1

        rectangle = Rectangle(height=5, width=7)
        #creamos el vmobject
        colect=VGroup(*grid,rectangle)
        self.play(FadeIn(colect, run_time=0.4))
        self.wait(3)
        end_scene(self)
        self.wait()
    

class Frame_medio_alig(Scene):

    def construct(self):
        grid=[]
        num_vects=0
        #point.move_to([2,2,0])
        #lo que vamos a hacer es crear un vector de vectores 4 x 3
        for i in range(-3,4):
            for j in range(-2,3):
                if(random.random()<0.6):
                    aux=Vector(DOWN,stroke_width=7)
                    aux.set_color(BLUE)
                else:
                    aux=Vector(UP,stroke_width=7)
                    aux.set_color(RED)   
                aux.scale(0.5)
                aux.move_to([i,j,0])
                grid.append(aux)
                num_vects+=1

        rectangle = Rectangle(height=5, width=7)
        #creamos el vmobject
        colect=VGroup(*grid,rectangle)
        self.play(FadeIn(colect, run_time=0.4))
        self.wait(3)
        end_scene(self)
        self.wait()


class Imags_qf(Scene):
    def construct(self):
        im1=ImageMobject("qf1.png")
        im1.scale(3.5)
        im2=ImageMobject("qf2.png")
        im2.scale(3.5)
        im3=ImageMobject("qf3.png")
        im3.scale(3.5)

        self.play(FadeIn(im1))
        self.wait(3)
        self.play(FadeOut(im1))
        self.play(FadeIn(im2))
        self.wait(3)
        self.play(FadeOut(im2))
        self.play(FadeIn(im3))
        self.wait(3)
        self.play(FadeOut(im3))
    

def end_scene(self):
    #esto nos coge todo lo de la escena y nos lo elimina con un fade out

    self.play(*[FadeOut(i) for i in self.get_mobjects()])
