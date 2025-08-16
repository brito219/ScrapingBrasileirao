o que é html-> hypertext markup language, esqueleto das paginas
tags de html-

#### Tags (Etiquetas)
HTML usa "tags" para marcar diferentes tipos de conteúdo:
```html
<table>     <!-- Início de uma tabela -->
<tr>        <!-- Linha da tabela (table row) -->
<td>        <!-- Célula da tabela (table data) -->
<div>       <!-- Divisão/seção -->
<span>      <!-- Texto inline -->
```
as tags podem ter atributos
class e id sao etiquetas que ajudam a identificar alguns elemtos, no bsoup é bom pra encontrar oq eu quero, ajuda a identificar legal

exemplo: 
<table class="classificacao" id="tabela-serie-b"> 
<div class="container">
<span id="nome-time">
```

exemplo do site da ufmg:

```html
<table class="leaguemanager">
    <thead>  <!-- Cabeçalho da tabela -->
        <tr>
            <th>N</th>      <!-- Posição -->
            <th>TIMES</th>  <!-- Nome do time -->
            <th>PG</th>     <!-- Pontos -->
            <th>J</th>      <!-- Jogos -->
            <!-- ... outras colunas -->
        </tr>
    </thead>
    <tbody>  <!-- Corpo da tabela -->
        <tr>
            <td>1</td>
            <td>GOIÁS</td>
            <td>41</td>
            <td>21</td>
            <!-- ... outros dados -->
        </tr>
        <tr>
            <td>2</td>
            <td>CORITIBA</td>
            <td>39</td>
            <td>21</td>
            <!-- ... outros dados -->
        </tr>
    </tbody>
</table>
```