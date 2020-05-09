package bozo.resto;

public class RolaDados {

	private Dado[] dds;
	
	/* cria um vetor de n dados de 6 lados */
	public RolaDados(int n)
	{
		dds = new Dado[n];
		for(int i = 0; i < n; i++)
		{
			dds[i] = new Dado();
		}
	}
	
	/* rola todos os dados de 'dds' e retorna todos seus valores */
	public int[] rolar()
	{
		int[] valores = new int[dds.length];
		for(int i = 0; i < dds.length; i++)
		{
			valores[i] = dds[i].rolar(i+1);
		}
		return valores;
	}
	
	/* rola alguns dados de 'dds' e retorna todos seus valores */
	public int[] rolar(boolean[] quais)
	{
		int[] valores = new int[dds.length];
		for(int i = 0; i < dds.length; i++)
		{
			if(quais[i] == false)
			{
				valores[i] = dds[i].getLado();
			}
			else
			{
				valores[i] = dds[i].rolar(i+1);
			}
		}
		return valores;
	}
	
	/* rola alguns dados de 'dds' e retorna todos seus valores */
	public int[] rolar(String s)
	{
		/* tratando caso de usuario nao querer trocar nada */
		if(s.equals(""))
		{
			boolean[] quais = new boolean[dds.length];
			for(int i = 0; i < dds.length; i++)
			{
				quais[i] = false;
			}
			return rolar(quais);
		}
		
		String[] numerosNaoParsados = s.split(" "); // preparando para parsar a entrada
		int[] numerosParsados = new int[numerosNaoParsados.length]; // criando o futuro vetor dos "parsados"
		for(int i=0; i < numerosNaoParsados.length; i++) {numerosParsados[i] = Integer.parseInt(numerosNaoParsados[i]);} // parsando
		boolean[] quais = new boolean[dds.length]; // criando um vetor para ser entrada do rolar(boolean[] quais)
		for(int i=0; i < quais.length; i++) {quais[i] = false;} // inicializando-o
		for(int i=0; i < numerosParsados.length; i++) {quais[numerosParsados[i] - 1] = true;} // preenchendo-o com as posicoes a serem trocadas

		return rolar(quais);
	}
	
	/* retorna 'imagem' dos n dados de 6 faces */
	public String toString()
	{
		String retorno = "";
		
		/* concatena linha dos indices dos dados */
		for(int i = 0; i < dds.length; i++){retorno += String.format(" %d         ", i+1);}
		retorno += "\n";
		
		/* concatena a linha de cima dos dados */
		for(int i = 0; i < dds.length; i++){retorno += "+-----+    ";}
		retorno += "\n";
		
		/* concatena a linha 1 do interior dos dados */
		for(int i = 0; i < dds.length; i++){retorno += toStringAux(dds[i].getLado(), 1);}
		retorno += "\n";
		
		/* concatena a linha 2 do interior dos dados */
		for(int i = 0; i < dds.length; i++){retorno += toStringAux(dds[i].getLado(), 2);}
		retorno += "\n";
		
		/* concatena a linha 3 do interior dos dados */
		for(int i = 0; i < dds.length; i++){retorno += toStringAux(dds[i].getLado(), 3);}
		retorno += "\n";
		
		/* concatena a linha de baixo dos dados */
		for(int i = 0; i < dds.length; i++){retorno += "+-----+    ";}
		retorno += "\n";
		
		return retorno;
	}
	
	/* metodo auxiliar para obter as 'imagens' das linhas dos dados individualmente */
	private String toStringAux(int valorDoDado, int qualLinha)
	{
		if(valorDoDado == 1)
		{
			if(qualLinha == 1)
			{
				return "|     |    ";
			}
			if(qualLinha == 2)
			{
				return "|  *  |    ";
			}
			if(qualLinha == 3)
			{
				return "|     |    ";
			}
		}
		
		if(valorDoDado == 2)
		{
			if(qualLinha == 1)
			{
				return "|*    |    ";
			}
			if(qualLinha == 2)
			{
				return "|     |    ";
			}
			if(qualLinha == 3)
			{
				return "|    *|    ";
			}
		}
		
		if(valorDoDado == 3)
		{
			if(qualLinha == 1)
			{
				return "|*    |    ";
			}
			if(qualLinha == 2)
			{
				return "|  *  |    ";
			}
			if(qualLinha == 3)
			{
				return "|    *|    ";
			}
		}
		
		if(valorDoDado == 4)
		{
			if(qualLinha == 1)
			{
				return "|*   *|    ";
			}
			if(qualLinha == 2)
			{
				return "|     |    ";
			}
			if(qualLinha == 3)
			{
				return "|*   *|    ";
			}
		}
		
		if(valorDoDado == 5)
		{
			if(qualLinha == 1)
			{
				return "|*   *|    ";
			}
			if(qualLinha == 2)
			{
				return "|  *  |    ";
			}
			if(qualLinha == 3)
			{
				return "|*   *|    ";
			}
		}
		
		if(valorDoDado == 6)
		{
			if(qualLinha == 1)
			{
				return "|* * *|    ";
			}
			if(qualLinha == 2)
			{
				return "|     |    ";
			}
			if(qualLinha == 3)
			{
				return "|* * *|    ";
			}
		}
		
		return "";
	}
	
}
