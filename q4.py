"""
#4- Você está analisando um código que gera a sequência de Fibonacci, muito
utilizada em matemática e computação para representar padrões numéricos.
Este código calcula a sequência de Fibonacci: A sequência de Fibonacci é
uma série de números onde cada número é a soma dos dois números
anteriores, começando com 0 e 1. F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) para
n &gt; 1. 

Responda às perguntas a seguir sobre esse código:

a, b = 0, 1
print(&quot;Sequência de Fibonacci:&quot;)
# A função range gera uma sequência de números inteiros.
for _ in range(10):
print(a, end=&quot; &quot;)
a, b = b, a + b


a) O que o código acima faz?
Resposta: Exibe os 10 primeiros números da sequência de Fibonacci.

b) O que significam as variáveis a e b no início do código?
Resposta: São os valores iniciais da sequência (o número atual e o próximo).

c) Como você modificaria o código para gerar os primeiros 20 números da
sequência de Fibonacci?
Resposta: Mudaria o range(10) para range(20).

d) Como você modificaria o código para começar a sequência de Fibonacci
com outros dois números, por exemplo, 2 e 3?
Resposta: Mudaria a primeira linha para a, b = 2, 3.

e) Qual é a função do loop for neste código?
Resposta: Repetir o cálculo e a impressão dos números 10 vezes.


"""