
public class Dado {
	
	private int nLados;
	private int ladoAtual;
	
	/* Cria um cubo */
	public Dado()
	{
		nLados = 6;
		ladoAtual = 1;
	}
	
	/* Cria um poliedro de n lados */
	public Dado(int n)
	{
		nLados = n;
		ladoAtual = 1;
	}
	
	/* Atualiza o campo 'ladoAtual' */
	public int rolar(int k)
	{
		Random r = new Random(k);
		ladoAtual = r.getIntRand(nLados) + 1;
		return ladoAtual;
	}
	
	/* Retorna o campo 'ladoAtual' */
	public int getLado()
	{
		return ladoAtual;
	}
	
	/* Retorna 'imagem' do dado (nao utilizado no programa principal) */
	public String toString()
	{
		if(ladoAtual == 1)
		{
			return("+-----+\n|     |\n|  *  |\n|     |\n+-----+");
		}
		if(ladoAtual == 2)
		{
			return("+-----+\n|*    |\n|     |\n|    *|\n+-----+");
		}
		if(ladoAtual == 3)
		{
			return("+-----+\n|*    |\n|  *  |\n|    *|\n+-----+");
		}
		if(ladoAtual == 4)
		{
			return("+-----+\n|*   *|\n|     |\n|*   *|\n+-----+");
		}
		if(ladoAtual == 5)
		{
			return("+-----+\n|*   *|\n|  *  |\n|*   *|\n+-----+");
		}
		if(ladoAtual == 6)
		{
			return("+-----+\n|* * *|\n|     |\n|* * *|\n+-----+");
		}
		return("");
	}
	
}