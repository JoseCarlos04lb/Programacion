package orientado.persona;
import java.time.LocalDate;
import java.util.Scanner;
import orientado.persona.Genero;
import orientado.persona.persona;
public class main {

	public static void main(String[] args) {
 
		Genero generoIntroducido =null;
		do {
			try {
				System.out.println("Introduzca el genero :");
				String generoComoString = new Scanner(System.in).nextLine();
				generoIntroducido =Genero.valueOf(generoComoString.toUpperCase());
				
			}catch(Exception exception) {
				System.out.println("El valor introducido no es correcto ");
			}
		}while(generoIntroducido==null);
		
		persona antonio = new persona("Antonio", "sanchez", Genero.HOMBRE);
		persona juan = new persona("Juan","Sanchez",Genero.HOMBRE);
		persona manu = new persona("manu","Sanchez",Genero.HOMBRE);

		
		persona [] grupo = new persona [3];
		grupo[0]=antonio;
		grupo[1]=juan;
		grupo[2]=manu;
	}

}
