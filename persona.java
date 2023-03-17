package orientado.persona;
import orientado.persona.Genero;

import java.time.LocalDate;
import java.util.Objects;
public class persona {

	
	private Genero genero;
	private String nombre;
	private String apellidos;
	private LocalDate fechaNacimiento;
	
	
	public persona(Genero genero, String nombre, String apellidos, LocalDate fechaNacimiento) {
		super();
		this.genero = genero;
		this.nombre = nombre;
		this.apellidos = apellidos;
		this.fechaNacimiento = fechaNacimiento;
	}


	


	public persona(String Antonio, String sanchez, Genero hombre) {
		persona antonio = new persona("Antonio", "sanchez", Genero.HOMBRE);
		persona juan = new persona("Juan","Sanchez",Genero.HOMBRE);
		persona manu = new persona("manu","Sanchez",Genero.HOMBRE);

	}
	
	public int conpareTo(persona o) {
		int resultado =0;
		if(this.genero.equals(Genero.HOMBRE)&& o.genero.equals(Genero.MUJER)) {
			resultado=1;
		}else if (this.genero.equals(Genero.MUJER)&& o.genero.equals(Genero.HOMBRE)) {
			resultado=-1;
		}
		return resultado;
	}


	@Override
	public int hashCode() {
		return Objects.hash(apellidos, fechaNacimiento, genero, nombre);
	}


	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		persona other = (persona) obj;
		return Objects.equals(apellidos, other.apellidos) && Objects.equals(fechaNacimiento, other.fechaNacimiento)
				&& genero == other.genero && Objects.equals(nombre, other.nombre);
	}



	

	
	
	
	
}
