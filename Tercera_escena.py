from manimlib.imports import *
import numpy as np 


class Tercera_escena(Scene):

    #Vamos a dibujar un sistema en un baño termico y a decir que que la temperatura es constante
    #despues vamos a explicar que ahora la que se conserva es la energía promedio y que eso supone una restriccion sobre
    #la entropia maxima a la que el sistema puede llegar, al igual que con el ejemplo de las flechas, el campo era relevante

    #primero vamos a dibujar dos cajas para decir sistema s y ambiente y decimos que estan en quilibrio y dibujamos <E< como sontante tbn

    #despues vamos a dibujar una barra que sea la entropía y vamos a poner un tope dadas las restricciones, así explicar que aunque aumente eso no explica que suceda
    #despues vamos a poner que Q=TS y sin restricciones (T=cte) se hace maximo pero, pero si conservamos <E>  Q-E lo que se hace máximo y que eso es -F
    #Finalmente explicar que dadas nuestras restricciones sera la minimizacion de F lo que nos guia. Y explicar los casos de Delta F=Delta E y -T Delta S
    def construct(self):
        sistema=RoundedRectangle(height=FRAME_HEIGHT*0.3,width=FRAME_WIDTH*0.3)
        sistema_text=TextMobject("Sistema")
        entorno=RoundedRectangle(height=FRAME_HEIGHT*0.8,width=FRAME_WIDTH*0.8)
        entorno_text=TextMobject("Entorno")
        sistema.move_to(1.7*DOWN+2.2*LEFT)
        entorno_text.move_to(entorno.get_center()+UP+RIGHT)
        sistema_text.move_to(sistema.get_center())

        temp=TexMobject("T=cte")
        eng_media=TexMobject("<E>=cte")
        temp.to_edge(DOWN,buff=SMALL_BUFF)
        eng_media.next_to(temp,RIGHT*3.5)
        escena=VGroup(sistema,entorno,entorno_text,sistema_text)
        self.play(Write(escena))
        self.wait(2)
        self.play(Write(temp))
        self.wait()
        self.play(Write(eng_media))
        self.wait()
        end_scene(self)
        


class restric_entropia(Scene):

    def construct(self):

        #de todas las configuraciones sin restriccion el top es el maximo de entropia, pero tenemos restricciones, y aunque aumente, aumenta bajo limites
        barra=Rectangle(height=5.5,width=1.3,fill_color=WHITE,fill_opacity=0.7)
        barra.to_edge(DOWN,buff=SMALL_BUFF)

        titulo_entropia1=TextMobject("La entropía puede no tomar su máximo","valor debido a las restricciones.")
        titulo_entropia1[1].next_to(titulo_entropia1[0],DOWN,aligned_edge=LEFT)
        titulo_entropia1.move_to(3*LEFT+3.2*UP)
        titulo_entropia1.scale(0.75)
        base_barra=Line(star=LEFT*1.5,end=1.5*RIGHT,stroke_width=20)
        base_barra.move_to(barra.get_bottom())
        perma_columna=barra.copy()
        perma_columna.set_opacity(0.3)
        linea_maxim=Line(start=LEFT,end=RIGHT,set_color=RED,stroke_width=2)
        text_max=TextMobject("Máximo posible")
        text_max.scale(0.6)
        text_max.next_to(barra.get_top(),LEFT*1.8+UP*0.6)
        text_max_seg_rest=TextMobject("Máximo según nuestras restricciones")
        text_max_seg_rest.scale(0.7)
        
        self.play(Write(titulo_entropia1))
        self.play(FadeInFromDown(VGroup(barra,base_barra)))
        self.wait()
        self.add(perma_columna)
        self.play(FadeIn(text_max))
        self.play(ApplyMethod(barra.shift,DOWN*2))
        linea_maxim.move_to(barra.get_top())
        text_max_seg_rest.next_to(linea_maxim,LEFT*1.8)
        self.wait()
        self.play(FadeIn(VGroup(text_max_seg_rest,linea_maxim)))
        self.wait(0.5)
        self.play(ApplyMethod(barra.shift,DOWN*2)) 
        self.wait(0.6)
        self.play(ApplyMethod(barra.shift,UP*1.3)) 
        self.wait(0.6)
        self.play(ApplyMethod(barra.shift,DOWN*2))
        self.wait(2)
        self.play((ApplyMethod(barra.shift,UP*(4-1.3))))
        self.wait()
        end_scene(self)


class Energia_libre(Scene):
    def construct(self):
        #en nuestro caso lo que se hace maximo será S-<E>/T que no deja de ser un nuevo máximo como hemos definido
        #como podemos ver la entropia como S=Q/T, cosa que sabemos de la termodinamica
        #el sistema, en equilibrio, distribuye la máxima cantidad de energía posible en grados de libertad que 
        #no producen trabajo (en calor), el calor se hace maximo
        #podemos escribir que (Q-<E>)/T se hace máximo cuando la energia media se conserva 
        #en termodinamica esto tiene una interpretacion, es -F, donde F es la energía libre, es decir la energía del sistema
        #"dispuesta" para convertirse en trabajo, lo que llamariamos la energia util y usable. Hemos convertido el principio de 
        #maxima entropía en el principio de minima energia libre (esto no es otra cosa que el hecho de que la energía se homogeiniza y el universo muere)

        ec1=TexMobject("S",r"- \frac{<E>}{T}")
        ec2=TexMobject("Q","=","S","T")
        ec3=TexMobject(r"\frac{Q}{T}","=","S")
        ec4=TexMobject(r"\frac{Q-<E>}{T}")
        #t es constante por eso consideramos solo el numerador
        ec5=TexMobject("Q-<E>","=","TS-<E>","=","-F")
        ec5.shift(LEFT*1.1+UP)
        ec6=TexMobject("S","Q","F")
        titulo1=TextMobject("Energía (libre) de Helmholtz")
        flecha1=Vector(UP)
        flecha1.next_to(ec6[0],RIGHT)
        flecha2=Vector(UP)
        flecha3=Vector(DOWN)
        titulo1.scale(0.8)
        titulo1.move_to(UP*2.3+RIGHT)
        ec1.scale(2)
        ec2.scale(1.6)
        ec3.scale(1.6)
        self.play(Write(ec1[0]))
        self.wait(2)
        self.play(Write(ec1[1:]))
        self.wait(2)
        self.play(ApplyMethod(ec1.shift,UP*2))
        self.play(ApplyMethod(ec1.scale,0.7))
        self.wait(1.5)
        self.play(Write(ec2))
        self.wait(2)
        self.play(Transform(ec2,ec3))
        self.wait(2)
        ec1_aux=TexMobject(r"\frac{Q}{T}")
        ec1_aux.move_to(ec1[0].get_center())
        ec1_aux.scale(2*0.7)
        self.play(Transform(ec3[0].copy(),ec1_aux),Transform(ec1[0],ec1_aux))
        self.wait(2)
        end_scene(self)
        self.play(Write(ec5[0]))
        self.wait(2)
        self.play(Write(ec5[1:]))
        self.wait(2)
        self.play(Write(titulo1),FadeIn(Arrow(titulo1.get_center(),ec5[-1].get_center(),stroke_width=3.5)))
        ec6.shift(DOWN)
        ec6[0].shift(LEFT*2)
        ec6[2].shift(RIGHT*2)
        flecha1.next_to(ec6[0],RIGHT)
        flecha1.set_color(GREEN)
        flecha3.next_to(ec6[2],RIGHT)
        flecha3.set_color(RED)
        flecha2.next_to(ec6[1],RIGHT)
        flecha2.set_color(GREEN)
        
        self.wait(2.5)
        self.play(GrowFromCenter(ec6))
        self.play(ApplyMethod(ec6[0].scale,2),GrowFromCenter(flecha1))
        self.wait(2)
        #self.play(GrowFromCenter(ec6[1]))
        self.play(ApplyMethod(ec6[1].scale,2),GrowFromCenter(flecha2))
        self.wait(2)
        #self.play(GrowFromCenter(ec6[2]))
        self.play(ApplyMethod(ec6[2].scale,0.6),GrowFromCenter(flecha3))
        self.wait(4)

        end_scene(self)
        #hemos tansformado el principio de maxima S en el de minima F, lo cual los hace completamente equivalentes para nuestro caso de T=cte
        frase1=TextMobject("Principio de máxima entropía.")
        frase2=TextMobject("Principio de mínima energía libre.")
        frase1.scale(1.6)
        frase2.scale(1.6)
        frase1.shift(UP*2)
        frase2.shift(UP*2)
        consecuencia1=TextMobject("- Estado muy homogeneo energeticamente hablando")
        consecuencia2=TextMobject("- Pocas diferencias de temperatura (sin flujo de calor no se puede obtener trabajo)")
        consecuencia3=TextMobject("- Muerte térmica del Universo")
        consecuencia1.move_to(DOWN*2+LEFT*3)
        consecuencia2.move_to(DOWN*2)
        consecuencia3.move_to(DOWN*2+RIGHT*3)
        
        consecuencia1.scale(0.75)
        consecuencia2.scale(0.7)
        consecuencia3.scale(0.75)
        consecuencia1.next_to(frase1,DOWN*2,aligned_edge=LEFT)
        consecuencia2.next_to(consecuencia1,DOWN*2,aligned_edge=LEFT)
        consecuencia3.next_to(consecuencia2,DOWN*2,aligned_edge=LEFT)

        #consecuencia2[1].next_to(consecuencia2[0],DOWN*0.75)
        self.play(FadeInFromDown(frase1))
        self.wait(4)
        self.play(Transform(frase1,frase2))
        self.wait(2)
        self.play(Write(consecuencia1))
        self.wait(2)
        self.play(Write(consecuencia2))
        self.wait(3.5)
        self.play(Write(consecuencia3))
        self.wait(2)
        end_scene(self)

class Ordenado_Desordenado(Scene):
    #supongamos que tenemos dos fases, ordenada y desordenada, sea lo que sea que signifique eso, las transiciones de fase es algo muy estudiado
    #y cuenta con varia deficiones, pero por ahora vamos a suponer que tenemos esas dos fases (obviamente en la ordenada suponemos una estructura geometrica etc)
    #dos fases, con sus cantidades S y <E>
    #calculamos la energia libre en el paso de la a la otra
    #sabemos que siempre se diaminuye , luego DELTA DE F debe ser negativo, eso lo podemos conseguir de varias formas
    def construct(self):
        #vamos a definir dos estados ordenado y desordenado, entre ellos obviamente hay un cambio de fase, pues las propiedades de 
        #cada uno de ellos son diferentes
        titulo1=TextMobject("Definimos dos estados posibles de nuestro sistema.")
        titulo1.to_edge(UP)
        linea1=Line(start=LEFT*6,end=RIGHT*6)
        linea1.next_to(titulo1,DOWN)
        estado1_label=TextMobject("Desordenado")
        #este lo podemos pensar como la fse cristalina
        estado1_imagen=ImageMobject("desordenada.png")
        estado1_imagen.to_edge(LEFT,buff=2)
        estado1_label.next_to(estado1_imagen,UP)
        estado2_label=TextMobject("Ordenado")
        #este como la fase fluida
        estado2_imagen=ImageMobject("ordenado.png")
        estado2_imagen2=ImageMobject("ordenado2.png")
        estado2_imagen3=ImageMobject("ordenado3.png")
        estado2_imagen.to_edge(RIGHT,buff=2.2)
        estado2_imagen2.next_to(estado2_imagen,LEFT)
        estado2_imagen3.next_to(estado2_imagen,DOWN)
        estado2_label.next_to(estado2_imagen,UP+LEFT)
        self.play(Write(titulo1),FadeInFromDown(linea1))
        self.wait(2)
        self.play(Write(estado1_label),FadeIn(estado1_imagen))
        self.wait(2)
        self.play(Write(estado2_label),FadeIn(estado2_imagen),FadeIn(estado2_imagen2),FadeIn(estado2_imagen3))
        self.wait(2)
        #ponemos que cada uno tiene sus cantidades, de energia media y de entropia
        titulo2=TextMobject("Y casda estado cuenta con sus cantidades termodinámicas")
        titulo3=TextMobject("En nuestro caso nos van a interesar la energía media y la entropía")
        cantidades_1=TexMobject(r"<E_{d}>",r"S_{d}")
        cantidades_1[1].next_to(cantidades_1[0],DOWN)
        cantidades_2=TexMobject(r"<E_{O}>",r"S_{O}")
        cantidades_2[1].next_to(cantidades_2[0],DOWN)
        cantidades_1.next_to(estado1_imagen,DOWN*1.5)
        cantidades_2.next_to(estado2_imagen3,LEFT*1.2)
        self.play(Write(VGroup(cantidades_1, cantidades_2)))
        self.wait(3)
        end_scene(self)

class Diferencias(Scene):
    def construct(self):
        #voy a definir las diferencias y lo que implica que se positivo o negativo

        definimos=TextMobject("Definimos:")
        definimos2=TextMobject("Y usando la ecuación conocida:")
        definimos2.to_edge(LEFT)
        definimos.to_corner(UL)
        #este E es el <E> que es FIJO EN CADA ESTADO,pero nada impide que en el no equilibrio esto cambie de estado a estado
        deltaE=TexMobject(r"\Delta E",r" = E_{O}-E_{d}")
        deltaS=TexMobject(r"\Delta S ",r"= S_{O}-S_{d}")
        deltaF=TexMobject(r"\Delta F ",r"= F_{O}-F_{d}")
        ecuacion1=TexMobject("F=E-TS")
        ecuacion2=TexMobject(r"\Delta F","=",r"\Delta E","-T",r"\Delta S")

        deltaS.move_to(UP*1.5)
        deltaE.next_to(deltaS,3*LEFT)
        deltaF.next_to(deltaS,3*RIGHT)
        ecuacion1.move_to(DOWN*1.5)
        ecuacion2.move_to(DOWN*1.5)

        self.play(Write(definimos))
        self.wait(4)
        self.play(Write(VGroup(deltaE,deltaS,deltaF)))
        self.wait(2)
        self.play(Write(VGroup(definimos2,ecuacion1)))
        self.wait(2)
        self.play(Transform(ecuacion1,ecuacion2),Transform(deltaE[0].copy(),ecuacion2[1]),Transform(deltaS[0].copy(),ecuacion2[2]),Transform(deltaF[0].copy(),ecuacion2[0]))
        self.wait(5)
        #self.play(FadeOut(VGroup(definimos,definimos2,deltaE,deltaS,deltaF,ecuacion1)))
        end_scene(self)
        
       # enunciado1=TextMobject("Ahora podemos ver si la transición es favorable viendo si se minimiza la energia libre Delta F<0")
        #self.play(Write(enunciado1))
class Posibilidades(Scene):
    #ESTO ES EN REALIDAD JUSTIFICAR COMO SE PUEDE PASAR A UNA FASE ORDENADA, ES DECIR CRISTALIZAR ETC, AUN SI ESO REDUCE LA ENTROPIA
    #EN ESTE RAZONAMIENTO ESTAMOS JUSTIFICANDO QUE GANE LA MINIMA ENERGIA FRENTE A LA MAXIMA ENTROPIA A LA HORA DE CRISTALIZAR ETC
    #SIN EMBARGO LUEGO EXPLICAREMOS QUE HAY PROCESOS EN QUE ES LA PROPIA ENTROPIA LA QUE AUMENTA TODO ESTO Y ORDENA EL ESTADO
    def construct(self):
        ecuacion2=TexMobject(r"\Delta F","=",r"\Delta E","-T",r"\Delta S")
        deltaS=TexMobject(r"\Delta S ",r"= S_{O}-S_{d}")
        ecuacion2.scale(1.5)
        ecuacion2.to_edge(UP,buff=2)
        deltaS.next_to(ecuacion2,LEFT*2.5)

        enunciado=TextMobject("Podemos ver si la transición es favorable")
        enunciadoo=TextMobject("viendo si se minimiza la energia libre.")
        enunciado.to_edge(UP,buff=SMALL_BUFF)
        enunciadoo.next_to(enunciado,DOWN)
        enunciado1=TextMobject("Si la variación es negativa,","entonces es favorable la fase ordenada.")
        enunciado1.scale(0.6)
        
        enunciado1[1].next_to(enunciado1[0],DOWN)
        formula1=TexMobject(r"\Delta F","<","0")
        imagen1=ImageMobject("up.png")
        enunciado2=TextMobject("Si la variación es positiva,","entonces es favorable la fase desordenada.")
        enunciado2[1].next_to(enunciado2[0],DOWN)
        enunciado2.scale(0.6)
        formula2=TexMobject(r"\Delta F",">","0")
        imagen2=ImageMobject("down.png")
        enunciado1.to_edge(LEFT,buff=1)

        imagen1.next_to(enunciado1,DOWN*2)
        formula1.next_to(imagen1,RIGHT)
        enunciado2.to_edge(RIGHT,buff=1)
        imagen2.next_to(enunciado2,DOWN*2)
        formula2.next_to(imagen2,RIGHT)
        mas=TexMobject("(+)")
        menos1=TexMobject("(-)")
        menos2=TexMobject("(-)")
        menos3=TexMobject("(-)")
        self.play(Write(VGroup(ecuacion2,enunciado,enunciadoo,deltaS)))
        self.wait(4)
        self.play(Write(VGroup(enunciado1,formula1)),FadeIn(imagen1))
        self.wait(4)
        self.play(Write(VGroup(enunciado2,formula2)),FadeIn(imagen2))
        self.wait(4)
        #self.play(ApplyMethod(ecuacion2[0].scale,1.5))
        #self.wait()
        #self.play(ApplyMethod(ecuacion2[2].scale,1.5))
        #self.wait()
        #es lógico pensar que en la fase final/fase ordenada la energía media es menor, por su posicionamiento mas ordenado,
        #esto contribuye con valor negativo
        #AUN ESTAMOS SUPONIENDO QUE LA FASE ORDENADA SUPONE MENOS ENTROPIA
        menos1.next_to(ecuacion2[2],DOWN)
        self.play(Write(menos1))
        menos2.next_to(ecuacion2[4],DOWN)
        self.play(Write(menos2))
        self.wait(2)
        self.play(ApplyMethod(ecuacion2[2].scale,0.5))
        self.play(ApplyMethod(ecuacion2[4].scale,1.5))
        self.wait(2)
        mas.next_to(ecuacion2[0],DOWN)
        self.play(Write(mas))
        #esto hace que no sea posible el cambio de fase
        #sin embargo si la temperatura es suficiente baja entonces
        self.wait(2)
        self.play(ApplyMethod(ecuacion2[2].scale,1.5))
        self.play(ApplyMethod(ecuacion2[4].scale,0.5))
        self.wait(2)
        self.play(ApplyMethod(ecuacion2[3].scale,0.5))
        self.wait(2)
        ecuacion3=TexMobject(r"|\Delta E| > T | \Delta S|")
        
        ecuacion3.scale(0.8)
        ecuacion3.next_to(ecuacion2,RIGHT*2)
        self.play(Write(ecuacion3))
        self.wait(2)
        menos3.next_to(ecuacion2[0],DOWN)
        self.play(Transform(mas,menos3))
        self.wait(2)
        end_scene(self)

#ESTO ULTIMO SUCEDE DE FORMA NORMAL EN LAS TRANSICIONES DE FASE, PERO QUE PASA SI TENEMOS ESFERAS DURAS QUE NO TIENEN INTERACCION ENTRE ELLAS
class Ord_entropia(Scene):
    def construct(self):
        titulo=TextMobject("¿Pero que pasaría si no hay energía de interacción?")
        titulo.to_corner(UL,buff=1.5)
        #como por ejemplo esferas duras, naranjas etc
        ec1=TexMobject(r"\Delta E = 0")
        a=TexMobject(r"\Delta F = - T \Delta S")
        ec1.next_to(titulo,DOWN*2)
        titulo2=TextMobject("La única alternativa para la cristalización es:")
        titulo2.to_edge(LEFT)
        ec2=TexMobject(r"\Delta S > 0")
        ec2.move_to(DOWN*2)
        ec4=TexMobject(r" S_{0} > S_{d}")
        ec4.move_to(DOWN*2)
        
        a.scale(0.9)
        a.move_to(DOWN)

        self.play(Write(titulo))
        self.wait(2)
        self.play(Write(ec1))
        self.wait(2)
        self.play(Write(titulo2))
        self.wait(0.9)
        self.play(Write(a))
        self.wait(2)
        self.play(Write(ec2))
        self.wait(2)
        self.play(Transform(ec2,ec4))
        self.wait(2)
        end_scene(self)
#. A menos que... ¡la entropía del cristal sea mayor que la del fluido! Pero, ¿cómo podría una fase ordenada tener más entropía que una desordenada?



def end_scene(self):
    #esto nos coge todo lo de la escena y nos lo elimina con un fade out

    self.play(*[FadeOut(i) for i in self.get_mobjects()])





