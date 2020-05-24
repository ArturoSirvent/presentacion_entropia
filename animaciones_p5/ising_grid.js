//VARIABLES PARA CAMBIAR###################################################################################
let N_filas=60;
let N_columnas=60;
let p_c=0.5;
let p_r=0.3;
let p_c_die=0.002;
let p_r_die=0.027;
let frames_per_sec=60;
let dt=0.05;





//CODIGO################################################################################################
let slider_p_c, slider_p_r;
let grid_c=[];
let grid_r=[];
let num_c=0;
let num_r=0;
let num_total=N_filas*N_columnas*2;

let t=0;
//lo que vamos a hacer es hacer unloop y cuando se pase por un sitio que ya tiene una celula, le damos la prob de morir


//aqui pongo el valor numerico, pero sin width y height, pero no me deja ponerlo
width_1=600;
height_1=600;


let ancho_c=width_1/N_columnas;
let alto_c=height_1/N_filas;


function setup() {
  createCanvas(1200, 600);
  background(255);
  stroke(0);
  for(let i=0;i<width_1;i+=ancho_c){
    line(i,0,i,height_1);
  }
  for(let i=0;i<height_1;i+=alto_c){
  line(0,i,width_1,i);
  }
  //slider_p_c=createSlider(0,1,0.1,0.01);
  //slider_p_r=createSlider(0,1,0.1,0.01);
  //array de los cuadrados
  for(let i=0;i<N_filas;i++){
    grid_c[i]=[];
    for(let j=0;j<N_columnas;j++){
//      if(0.5<=random(0,1)){
//        grid_c[i][j]=1;
//        num_c+=1;
//      }else{
      grid_c[i][j]=0;
//      }
    }
  }
  
  
  //array de los rombos, van a ser todos los vertices menos la última linea de la derecha y     //la de abajo del todo
  //va a tener el doble de alto el array
  for(let i=0;i<N_filas*2;i++){
    grid_r[i]=[];
    for(let j=0;j<N_columnas;j++){
      if(i>1 && i<N_filas*2-2 && j>0 && j<N_columnas-1){
        if(0.5<=random(0,1)){
          grid_r[i][j]=1;
          num_r+=1;
        }else{
          grid_r[i][j]=0;
        }
      }else{grid_r[i][j]=0;}
    }
  }
  
}

function draw() {
  //p_c=slider_p_c.value();
  //p_r=slider_p_r.value();
  //vamos a dibujar la grid cada vez
  stroke(3);
  for(let i=0;i<width_1;i+=ancho_c){
    line(i,0,i,height_1);
  }
  for(let i=0;i<height_1;i+=alto_c){
  line(0,i,width_1,i);
  }
  noStroke();
  
  
  //las actualizaciones se van a llevar a cabo para los cuadrados interiores para no tener 
  //en cuenta effectos de borde, es por simplicidad en el código
  
  //lo hacemos primero para los cuadrados
  for(let i=1;i<N_filas-1;i++){
    for(let j=1;j<N_columnas-1;j++){
      
      //miramos si esta celda esta vacia, si lo esta, procedemos
      if(! grid_c[i][j]){
        //generamos un numero aleatorio y con una probabilidad p pondremos ahi un cuadrado
        let p_c_aux=random(0,1);

        if(p_c_aux<=p_c){
           //si esta por debajo de la prob indicada miramos si es factible ponerlo
           //en realidad la forma correcta sería tener un array que nos indique si es posible            //colocar una cuadrado o no, asi nos ahorramos esto, pero no creo que sea mucho              //más rápido.
           if(c_is_possible(i,j)){
             grid_c[i][j]=1;
             num_c+=1;
             draw_square(i,j);
           } 
        }
     }else{
        //le damos la oprtunidad de morir
       if(random(0,1)<p_c_die){
         grid_c[i][j]=0;
         num_c-=1;
         remove_square(i,j);
       }
    
      }
      
    }
  }
  //ahora lo hacemos para los rombos
  for(let i=2;i<N_filas*2-1;i++){
    for(let j=1;j<N_columnas-1;j++){
      
      
      if(! grid_r[i][j]){
      
        //generamos un numero aleatorio y con una probabilidad p pondremos ahi un cuadrado

        let p_r_aux=random(0,1);

        if(p_r_aux<=p_r){
           //si esta por debajo de la prob indicada miramos si es factible ponerlo
           //en realidad la forma correcta sería tener un array que nos indique si es posible            //colocar una cuadrado o no, asi nos ahorramos esto, pero no creo que sea mucho              //más rápido.
           if(r_is_possible(i,j)){
             draw_rombo(i,j);

             grid_r[i][j]=1;
             num_r+=1;
           } 
        }
        
      }else{
        //le damos la oprtunidad de morir
       if(random(0,1)<p_r_die){
         grid_r[i][j]=0;
         num_r-=1;
         remove_rombo(i,j);
       }

      }
    }
  }
  
  
  frameRate(frames_per_sec);
  
  
  //aqui vamos a dibujar la grafica de la derecha
  //primero los ejes
  push();
  translate(width_1+width_1*0.1,height_1-height*0.1)
  stroke(4);
  line(0,0,0,-height_1*0.83);
  line(0,0,width_1*0.83,0);
  //ahora dibujamos un punto para cada setuacion de r y c
  strokeWeight(1.7);
  stroke(color(0,200,100));
  point(t,-height_1*0.83*num_r/num_total);
  stroke(color(200,0,100));
  point(t,-height_1*0.83*num_c/num_total);
  t+=dt;
  pop();

  
}



function c_is_possible(y,x){
  //lo que hacemos es mirar los rombos cercanos para ver si hay alguno
  let indice_filas_r=y*2+1;
  let indice_columnas_r=x;
  for(let i=-1;i<=1;i++){
    if(i==0){
      
      if(grid_r[indice_filas_r][indice_columnas_r]==1){
        return false;
      } //is not possible
      if(grid_r[indice_filas_r][indice_columnas_r+1]==1){
        return false;
      } //is not possible
    
    }else{
      if(grid_r[indice_filas_r+i][indice_columnas_r]==1){
        return false;
      } //is not possible
    }      
  }
  return true;
}

function r_is_possible(y,x){
  //para poner un rambo solo necesitamos mirar dos valores, pero depende de si es vertical o
  //horizontal, resulta que todas las lineas horizontales son pares y todas las verticales     //son impares

  
  if(y%2==0){
    //miramos grid_c en los valores arriba y abajo, siendo el de arriba el inicial
    let indice_filas_c=floor(y/2)-1;
    let indice_columnas_c=x;
    if(grid_c[indice_filas_c][indice_columnas_c]==1){
      return false;
    } //esta ocupado, no se                                                                         //puede poner rombo
    if(grid_c[indice_filas_c+1][indice_columnas_c]==1){
      return false;
    }
  }else{
    let indice_filas_c=floor(y/2);
    let indice_columnas_c=x-1; //nos colocamos a la derecha, esto hay que tener cuidado pues
                               //en el limite no valdría, pero los vamos a considerar
    if(grid_c[indice_filas_c][indice_columnas_c]==1){
      return false;
    } //esta ocupado, no se                                                                         //puede poner rombo
    if(grid_c[indice_filas_c][indice_columnas_c+1]==1){
      return false;
    }

  }
  
  return true;

}



function draw_square(y,x){
  let coord_alto=y*alto_c;
  let coord_ancho=x*ancho_c;
  fill(200,0,100);
  rect(coord_ancho,coord_alto,ancho_c,alto_c,13);

}

function remove_square(y,x){
  let coord_alto=y*alto_c;
  let coord_ancho=x*ancho_c;
  fill(255);
  rect(coord_ancho,coord_alto,ancho_c,alto_c,13);

}





function draw_rombo(y,x){
  //aqui tambien es diferente si es horizontal o vertical
  
  if(y%2==1){
    let coord_alto=floor(y/2)*alto_c;
    let coord_ancho=(x)*ancho_c;
    push();
    translate(coord_ancho,coord_alto);
    rotate(PI/4);
    fill(0,200,100);
    rect(0,0,ancho_c/sqrt(2),alto_c/sqrt(2),3);
    pop();

  }else{
  
    let coord_alto=(floor(y/2))*alto_c;
    let coord_ancho=x*ancho_c;
    push();
    translate(coord_ancho,coord_alto);
    rotate(-PI/4);
    fill(0,200,100);
    rect(0,0,ancho_c/sqrt(2),alto_c/sqrt(2),3);
    pop();
  
  
  }
}


function remove_rombo(y,x){
  //aqui tambien es diferente si es horizontal o vertical
  
  if(y%2==1){
    let coord_alto=floor(y/2)*alto_c;
    let coord_ancho=(x)*ancho_c;
    push();
    translate(coord_ancho,coord_alto);
    rotate(PI/4);
    fill(255);
    rect(0,0,ancho_c/sqrt(2),alto_c/sqrt(2),3);
    pop();

  }else{
  
    let coord_alto=(floor(y/2))*alto_c;
    let coord_ancho=x*ancho_c;
    push();
    translate(coord_ancho,coord_alto);
    rotate(-PI/4);
    fill(255);
    rect(0,0,ancho_c/sqrt(2),alto_c/sqrt(2),3);
    pop();
  
  
  }
}


