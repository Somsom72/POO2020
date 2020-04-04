import java.util.Calendar;

public class Random {

	private static long p = 2147483648L;
	private static long m = 843314861;
	private static long a = 453816693;
	private long x = 1023;

	// definindo construtor semente manual
	public Random(int k) {
		Calendar c = Calendar.getInstance();
		x = c.getTimeInMillis()*(long)k;
	}
	
	// definindo construtor semente automatica
	public Random() {}
	
	// retorna numero aleatorio entre 0 e 1
	public double getRand() {
		x = (a + m*x)%p;
		double d = x;
		return Math.abs(d/p);
	}

	// retorna aleatorio de zero ate maximo
	public int getIntRand(int max) {
		double d = getRand() * max;
		return (int)d;
	}
	
	// permite mudar o valor de 'x': a semente
	public void setSemente(int semente) {
		x = semente;
	}
	
}
