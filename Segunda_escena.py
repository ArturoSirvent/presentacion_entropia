from manimlib.imports import *
import numpy as np 





class Radios_relativos(Scene):
    #vamos a poner dos esferas y explicar 
    def construct(self):


        imagen1=ImageMobject("radio_efectivo1.png")
        imagen2=ImageMobject("radio_efectivo2.png")
        imagen1.scale(2.2)
        imagen2.scale(2.2)
        imagen1.to_edge(RIGHT,buff=1)
        imagen2.to_edge(LEFT,buff=1)
        self.play(FadeIn(imagen2))
        self.wait(3)
        self.play(FadeIn(imagen1))
        self.wait(3)
        end_scene(self)

        N=10
        radius=1
        #dentro de una caja vamos a poner varios puntos aleatoriamente
        dots=[]
        textos=[]
        caja=RoundedRectangle(height=FRAME_HEIGHT*0.8,width=FRAME_WIDTH*0.8)
        for i in range(N):
            random.seed()
            x_aux=FRAME_WIDTH*0.5*0.7-2*random.uniform(0,1)*FRAME_WIDTH*0.5*0.7
            y_aux=FRAME_HEIGHT*0.5*0.7-2*random.uniform(0,1)*FRAME_HEIGHT*0.5*0.7
            texto_aux=DecimalNumber(DEFAULT_DOT_RADIUS)
            texto_aux.scale(0.5)
            dot_aux=Dot([x_aux,y_aux,0])
            texto_aux.next_to(dot_aux,UP,buff=SMALL_BUFF)
            dots.append(dot_aux)
            textos.append(texto_aux)
        puntos=VGroup(*dots)
        labels=VGroup(*textos)
        self.add(caja,puntos,labels)
        self.wait(3)
        for i in range(N):
            labels[i].add_updater(lambda m: m.next_to(puntos[i],UP,buff=SMALL_BUFF))
            labels[i].add_updater(lambda l: l.set_value(radius))
        self.add(puntos,labels)
        for i in range(N):
            
            dot_aux=Dot(puntos[i].get_center(),radius=radius)
            dot_aux.set_color(GREY)
            self.play(ReplacementTransform(puntos[i],dot_aux),run_time=0.6)
            #podemos acceder a la configuracion mediante ese comando
            self.add(labels)
        self.wait(2)
        end_scene(self)
        self.wait(2)

        estado2_imagen=ImageMobject("ordenado.png")
        estado2_imagen2=ImageMobject("ordenado2.png")
        estado2_imagen3=ImageMobject("ordenado3.png")
        estado2_imagen.scale(2)
        estado2_imagen2.scale(2)
        estado2_imagen3.scale(2)
        estado2_imagen2.next_to(estado2_imagen,LEFT)
        estado2_imagen3.next_to(estado2_imagen,RIGHT)
        self.play(FadeIn(estado2_imagen),FadeIn(estado2_imagen2),FadeIn(estado2_imagen3))
        self.wait(5)
        end_scene(self)
        """
        self.wait()
        self.add(caja)
        ORIGEN=FRAME_WIDTH/2.0+FRAME_HEIGHT/2.0
        for i in range(6):
            for j in range(2):
                posicion_aux=ORIGEN
                punto_aux=Dot(posicion_aux)
                self.add(punto_aux)
        """



#class Mydots(Dot):
#    valor=DEFAULT_DOT_RADIUS
#    CONFIG={"radius":valor}
#    def change_rad(self,new_valor):
#        valor=new_valor
#        CONFIG={"radius":valor}


def end_scene(self):
    #esto nos coge todo lo de la escena y nos lo elimina con un fade out

    self.play(*[FadeOut(i) for i in self.get_mobjects()])
