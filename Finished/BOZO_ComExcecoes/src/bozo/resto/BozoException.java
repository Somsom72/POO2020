package bozo.resto;

@SuppressWarnings("serial")
public class BozoException extends RuntimeException {

	public BozoException()
	{
		super("Posicao ja ocupada no placar, tente novamente.");
	}

}
