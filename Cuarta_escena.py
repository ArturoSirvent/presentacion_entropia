from manimlib.imports import *
import numpy as np 

class Esferas_duras(Scene):
    #ahora vamos a explicar el caso de esferas duras, qeu por encima de 50% de ocupacion muestan cristalización
    #despues vamos a introducir el tema de espacio disponible
    def construct(self):
        titulo=TextMobject("Cristalización en esferas duras")
        sub1=TextMobject("- No muestran interacción entre ellas.")
        sub2=TextMobject("- La propia característica de no solaparse hace que se ordenen.")
        imagen1=ImageMobject("desorden1.png")
        capt1=TextMobject(r"Por debajo del 50 \% de ocupación")
        capt1.scale(0.7)
        imagen2=ImageMobject("orden1.png")
        capt2=TextMobject(r"Pasado el 50 \% de ocupación")
        capt2.scale(0.6)
        titulo.to_corner(UL)
        sub1.next_to(titulo,DOWN*2.5,aligned_edge=LEFT)
        sub2.next_to(sub1,DOWN*2.5,aligned_edge=LEFT)
        imagen1.move_to(DOWN+3*LEFT)
        imagen2.move_to(DOWN+3*RIGHT)
        capt1.next_to(imagen1,DOWN)
        capt2.next_to(imagen2,DOWN)
        self.play(Write(VGroup(titulo,sub1,sub2)))
        imagen1.to_edge(LEFT,buff=2)
        capt1.next_to(imagen1,DOWN)
        imagen2.to_edge(RIGHT,buff=2)
        capt2.next_to(imagen2,DOWN)
        self.wait(4)
        self.play(FadeIn(imagen1),Write(capt1))
        self.wait(4)
        self.play(FadeIn(imagen2),Write(capt2))
        self.wait(4)



#puedes decir, bueno pero esque si hay muchas esferas o su radio es muy grande, pues no les queda otra que ordenarse para caber, claro.
#Bueno pues esque es eso lo qeu pasa cuando la temperatura es baja que se debe buscar la ordenacion para no solaparse, sino el estado no existiria, o 
#o quiza empezarian a solapar y habría una presion extraña de algun lado, pero gracias a que se ordenan el sistema puede existir en equilibrio!!!



class Espacio_libre(Scene):
    def construct(self):
        titulo=TextMobject("El espacio libre no es ")
        titulo.scale(0.7)
        titulo.to_corner(UL,buff=1)
        ec1=TexMobject(r"(V-N* \nu_{esfera})")
        ec1.next_to(titulo,RIGHT*1.5)
        imagen1=ImageMobject("esf_lib_1.png")
        imagen1.next_to(ec1,RIGHT)
        titulo2=TextMobject("Hay una zona entorno a cada esfera, donde no hay otro centro")
        titulo2.scale(0.8)
        titulo2.move_to(UP)
        imagen2=ImageMobject("esf_lib_2.png")
        imagen2.next_to(titulo2,DOWN)
        titulo3=TextMobject("En esos puntos exteriores sí se puede añadir otra esfera.")
        titulo3.move_to(DOWN*2)
        titulo3.scale(0.8)
        #"cabe" justo en el limite!!!!
        titulo4=TextMobject("Este es el volumen accesible")
        ec2=TexMobject(r"(V-N*\nu_{esfera}^*)")
        titulo4.to_corner(DL,buff=1)
        ec2.next_to(titulo4,RIGHT)
        self.play(Write(VGroup(titulo,ec1)))
        self.play(FadeIn(imagen1))
        self.wait(4)
        self.play(Write(titulo2))
        self.play(FadeIn(imagen2))
        self.wait(4)
        self.play(Write(titulo3))
        self.wait(4)
        self.play(Write(VGroup(titulo4,ec2)))
        self.wait(2)
        end_scene(self)



#ultima escena ya, ostia

def end_scene(self):
    #esto nos coge todo lo de la escena y nos lo elimina con un fade out

    self.play(*[FadeOut(i) for i in self.get_mobjects()])

class Ultima_escena(Scene):
    #aqui vamos a poner la equivalencia entre mas espacio disponible y mayor numero de estados
    def construct(self):

        titulo=TextMobject("Si la densidad es alta, las esferas se juntarán")
        titulo.scale(0.85)
        titulo2=TextMobject("Si se juntan, el area \"prohibida\" es menor que las dos separadas")
        titulo2.scale(0.7)
        imagen2=ImageMobject("area1.png")
        imagen22=ImageMobject("area2.png")
        imagen2.scale(0.85)
        imagen22.scale(0.85)
        titulo3=TextMobject("A mayor ordenación")
        titulo3.scale(0.7)
        titulo4=TextMobject("Mayor area accesible")
        titulo4.scale(0.7)
        titulo5=TextMobject("Más estados posibles") #MAS LUGARES DONDE COLOCARTE
        titulo5.scale(0.7)
        titulo6=TextMobject("Mayor entropía")
        titulo6.scale(0.7)
        titulo7=TextMobject("¡Cuando la densidad es alta!") 
        titulo7.scale(0.8)
        flecha1=Vector(DOWN*0.5)

        flecha2=Vector(DOWN*0.8)
        flecha3=Vector(DOWN*0.5)
        flecha4=Vector(DOWN*0.5)
        flecha5=Vector(DOWN*0.5)
        titulo.to_edge(UP)
        flecha1.next_to(titulo,DOWN*0.5)
        titulo2.next_to(flecha1,DOWN*0.5)
        imagen2.move_to(titulo2.get_center()+DOWN*1.3+RIGHT*3.4)
        imagen22.move_to(titulo2.get_center()+DOWN*1.3+LEFT*2.9)
        flecha2.next_to(titulo2,DOWN*2.1)
        titulo3.next_to(flecha2,DOWN*2.5)
        flecha3.next_to(titulo3,DOWN*0.5)
        titulo4.next_to(flecha3,DOWN*0.6)
        flecha4.next_to(titulo4,DOWN*0.5)
        titulo5.next_to(flecha4,DOWN*0.6)
        flecha5.next_to(titulo5,DOWN*0.5)
        titulo6.next_to(flecha5,DOWN*0.6)
        titulo7.rotate(PI/6)
        titulo7.move_to(LEFT*4+DOWN*2.2)
        titulo7.set_color(RED)
        self.play(Write(titulo))
        self.wait(2)
        self.play(Write(VGroup(flecha1,titulo2)))
        self.wait(2)
        self.play(FadeIn(imagen2),FadeIn(imagen22))
        self.wait(2)
        self.play(Write(VGroup(flecha2,titulo3)))
        self.wait(2)
        self.play(Write(VGroup(flecha3,titulo4)))
        self.wait(2)
        self.play(Write(VGroup(flecha4,titulo5)))
        self.wait(2)
        self.play(Write(VGroup(flecha5,titulo6)))
        self.wait(2)
        self.play(FadeInFromLarge(titulo7))
        self.wait(2)

        end_scene(self)

    

    #mencionar que el caso de esferas duras es cierto en algunos coloides, pero para otros muchos casos, 

#lo ultimo sera el tema de la segregacion entrópica