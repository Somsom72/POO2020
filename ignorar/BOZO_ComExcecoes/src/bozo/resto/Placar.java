package bozo.resto;

public class Placar {

	private int[] pos;

	/* inicializa as posicoes da tabela com (-1) para indicar 'nao preenchida' */
	public Placar()
	{
		pos = new int[10];
		for(int i = 0; i < 10; i++)
		{
			pos[i] = -1;
		}
	}
	
	/* registra pontuacao em uma posicao dado um conjunto de dados */
	public void add(int posicao, int[] dados)
	{
			if(posicao < 1 || posicao > 10 || pos[posicao-1] != -1)
			{
				throw new BozoException();
			}
			
			int soma = 0;
			/* atualizando pontuacao no caso 1 a 6 ("normais") */
			if(posicao < 7)
			{
				for(int i = 0; i < dados.length; i++)
				{
					if(dados[i] == posicao)
					{
						soma += posicao;
					}
				}
				pos[posicao-1] = soma;
				return;
			}
			/* atualizando pontuacao nos casos "especiais" */
			else
			{
				int[] quantosDeCadaValor = new int[6];
				for(int i = 0; i < dados.length; i++)
				{
					quantosDeCadaValor[dados[i] - 1]++;
				}
				if(posicao == 7) // full (15 pontos)
				{
					for(int i = 0; i < 6; i++) {
						if(quantosDeCadaValor[i] >= 3)
						{
							soma += 15;
							break;
						}
					}
				}
				if(posicao == 8) // sequencia (20 pontos)
				{
					if(quantosDeCadaValor[1] != 0 && quantosDeCadaValor[2] != 0 && quantosDeCadaValor[3] != 0 && quantosDeCadaValor[4] != 0 && (quantosDeCadaValor[0]!=0 || quantosDeCadaValor[5]!=0))
					{
						soma += 20;
					}
				}
				if(posicao == 9) // quadra (30 pontos)
				{
					for(int i = 0; i < 6; i++) {
						if(quantosDeCadaValor[i] >= 4)
						{
							soma += 30;
							break;
						}
					}
				}
				if(posicao == 10) // quina (40 pontos)
				{
					for(int i = 0; i < 6; i++) {
						if(quantosDeCadaValor[i] >= 5)
						{
							soma += 40;
							break;
						}
					}
				}
				pos[posicao-1] = soma;
				return;
			}
	}
	
	/* retorna a soma das pontuacoes das posicoes ja ocupadas */
	public int getScore()
	{
		int soma = 0;
		for(int i = 0; i < 10; i++)
		{
			if(pos[i] != -1)
			{
				soma += pos[i];
			}
		}
		return soma;
	}
	
	/* retorna 'imagem' do placar atual */
	public String toString()
	{
		String retorno = "";
		String margem1 = "   |   ";
		String margem2 = "--------------------------\n";
		String margem3 = "       +----------+       \n";
		String aux = null;
		
		/* loop para montar as linhas do placar */
		for(int i = 0; i < 3; i++)
		{
			/* loop para montar as colunas do placar */
			for(int j = 0; j < 3; j++)
			{
				if(j == 0)
				{
					if(pos[i] == -1)
					{
						aux = String.format("(%d)", (i+1));
					}
					else
					{
						aux = String.format("%d", pos[i]);
					}
					retorno += String.format("%-4s%s", aux, margem1);
				}
				if(j == 1)
				{
					if(pos[i+6] == -1)
					{
						aux = String.format("(%d)", (i+1)+6);
					}
					else
					{
						aux = String.format("%d", pos[i+6]);
					}
					retorno += String.format("%-4s%s", aux, margem1);
				}
				if(j == 2)
				{
					if(pos[i+3] == -1)
					{
						aux = String.format("(%d)", (i+1)+3);
					}
					else
					{
						aux = String.format("%d", pos[i+3]);
					}
					retorno += String.format("%-4s   \n%s", aux, margem2);
				}
			}
		}
		/* imprimindo a ultima linha "anomala" do placar */
		if(pos[9] == -1)
		{
			aux = String.format("(%d)", 10);
		}
		else
		{
			aux = String.format("%d", pos[9]);
		}
		retorno += String.format("    %s%-4s%s    \n%s", margem1, aux, margem1, margem3);
		
		return retorno;
	}
	
}
