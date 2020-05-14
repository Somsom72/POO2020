package bozo.main;
/* Jogo "Bozo" para POO, autor: Luca Maciel Alexander, nUSP: 11219175 */

import java.io.IOException;

import bozo.resto.EntradaTeclado;
import bozo.resto.Placar;
import bozo.resto.RolaDados;
import bozo.resto.BozoException;

public class Bozo {

	public static void main(String[] args) throws IOException
	{
		/* Instancia classes necessarias */
		Placar plc = new Placar();
		RolaDados rladds = new RolaDados(5);
		
		/* Declara variaveis auxiliares e inicia loop do jogo */
		String entradaCrua = null;
		
		for (int i = 0; i < 10; i++)
		{
			/* Imprime placar */
			System.out.printf("%s\n", plc.toString());
			
			/* Lanca dados */
			System.out.printf("****** Rodada %d\nPressione ENTER para lançar os dados.\n", i+1);
			rladds.rolar();
			EntradaTeclado.leString();
			rladds.rolar();
			System.out.printf("%s\n", rladds.toString());

			/* Troca dados */
			for(int j = 0; j < 2; j++)
			{
				System.out.println("Digite os números dos dados que quiser TROCAR, separados por espaços.");
				while(true) {
					try {
					entradaCrua = EntradaTeclado.leString();
					}
					catch(IOException e) {System.out.println("erro, tente novamente"); continue;}
					break;
				}
				if(entradaCrua.equals("")) {break;}
				
				/* Se chega aqui, o usuario de fato quer trocar alguns dados */
				rladds.rolar(entradaCrua);
				System.out.printf("%s\n", rladds.toString());
			}
			
			/* Finaliza a rodada, atualizando o placar com a escolha do usuario */
			System.out.printf("%s\n", plc.toString());
			System.out.printf("Escolha a posição que quer ocupar com essa jogada ===> ");
			while(true)
			{
				try {
				plc.add(EntradaTeclado.leInt(), rladds.rolar(""));
				}
				catch(IOException e) {System.out.println("erro, tente novamente"); continue;}
				catch(BozoException e) {System.out.println(e.getMessage()); continue;}
				break;
			}
			System.out.printf("\n");
		}
		
		/* Imprime o placar final e encerra o programa */
		System.out.printf("%s\n", plc.toString());
		System.out.printf("*************************************************\n***\n***  Seu escore final foi: %d\n***\n*************************************************\n", plc.getScore());
		return;
	}
}
