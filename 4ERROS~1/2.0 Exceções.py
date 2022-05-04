xceções
Cada vez que o seu código tenta fazer algo de errado/tolo/irresponsável/maluco/imprevisível, o Python faz duas coisas:

para o seu programa;
cria um tipo especial de dados, chamado uma exceção.
Ambas estas atividades são designadas por levantar uma exceção. Podemos dizer que o Python levanta sempre uma exceção (ou que foi levantada uma exceção) quando não tem ideia do que fazer com o seu código.

O que acontece a seguir?

a exceção levantada espera que alguém ou alguma coisa a note e se encarregue dela;
se nada acontecer para tratar da exceção levantada, o programa será terminado à força, e verá uma mensagem de erro enviada para a consola pelo Python;
caso contrário, se a exceção for cuidada e tratada adequadamente, o programa suspenso pode ser retomado e a sua execução pode continuar.
O Python fornece ferramentas eficazes que lhe permitem observar exceções, identificá-las e tratá-las eficientemente. Isto é possível devido ao facto de todas as potenciais exceções terem os seus nomes inequívocos, pelo que se pode categorizá-los e reagir adequadamente.




O_conceito_de_exceções.JPG


Já conhece alguns nomes de exceção. Dê uma vista de olhos à seguinte mensagem de diagnóstico:

ValueError: math domain error
output

A palavra destacada acima é apenas o nome da exceção. Vamos familiarizar-nos com algumas outras exceções.