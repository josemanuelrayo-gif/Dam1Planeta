package Principal;

import java.util.Random;

public class Productor implements Runnable{
    Cola colaCompartida;
    public Productor(Cola cola){
            this.colaCompartida=cola;
    }
    public void run() {
       while (true){
               int num=alea(0,10);
   
               while (colaCompartida.encolar(num)==false){
                       esperarTiempoAzar(3000);
               } /*Fin del while*/

               System.out.println("Productor encoló el numero:"+num);
       } /*Fin del while externo*/
    } /*Fin de run()*/
    public static void esperarTiempoAzar(int max){
        Random generador=new Random();
        /* Se calculan unos milisegundos al azar*/
        int msgs=(1+generador.nextInt(max))*1000;
        try {
                        Thread.currentThread().sleep(msgs);
        } catch (InterruptedException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
        }
    }
        public static int alea(int li,int ls){
        	return (int)(Math.random()*(ls-li+1))+li;
        	
        }

} /*Fin de la clase*/