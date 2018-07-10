## AFD com pilha em Python
### Como executar:
Dentro do diretório dos arquivos, digite:
```python3 main.py [arquivo] [palavra]```
ou:
```python3.5 main.py [arquivo] [palavra]```

Sendo *[arquivo]* um arquivo txt com a definição do autômato e suas regras de
transição, e *[palavra]* uma palavra que se deseja processar.

### Arquivo .txt:
O arquivo txt com a definição do autômato finito determinístico deve seguir a
seguinte sintaxe (padrão):

Deve ter os 6 parâmetros entre parênteses e separados por
vírgula, contendo:
1. O conjunto de símbolos (alfabeto) entre chaves;
2. O conjunto de estados atingíveis, entre chaves;
3. O caractere referente ao conjunto de regras de transição; 
4. O estado inicial;
5. O conjunto de estados finais, entre chaves;
6. O conjunto de simbolos da pilha.

Nas linhas abaixo devem estar as definições das regras de transição, seguindo:
1. Cada regra contém 5 itens, estado inicial, símbolo a ser lido da
palavra, simbolo a ser lido da pilha, estado alvo e simbolo a ser escrito na
pilha. Eles devem estar separados por vírgula.
2. As regras devem estar dispostas em linhas diferentes, uma logo após a outra.
