<div align="center">
<h1> Desafio de Scraping em Python - SAUTER </h1>
</div>

<il>
<li> Objetivo: Raspagem de Reviews do Aplicativo Alexa na Google Play Store usando a Lib Google-Play-Scraper</li>
<li> Motivo: O Scraping de dados tem diversas finalidades, entre ela analisar a aceitação ou o nível de incômodo dos usuários com uma nova versão do app ou featura implementada.</li>
<li> Ferramentas: Para a raspagem usei a lib Google-Play-Scraper onde filtrei para trazer apenas os reviews em português dentro do território brasileiro. Para a manipulação dos dados e das tabelas, usei Pandas e Numpy. Para banco de dados usei a solução da Google, o BigQuery. E para análise dos dados usei o Google DataStudio. Construí uma página HTML interativa com o dashboard e os insigths, você poderá vê-la na apresentação. PAra examinar o código, poderá abrir o arquivo dashboard.html.</li>
</il>

<h3> Instruções de uso: </h2>

<p> Alguns passos simples devem ser seguidos antes de rodar o pipeline de dados. </p>
<ol>
  <li>  Abra o terminal e execute: </li>
  
  ```
  $ git clone https://github.com/saractavares/scrap_sauter_desafio.git
  ```
  
  <li>  Navegue até a pasta criada: </li>
  
```
  $ cd scrap_sauter_desafio
```
   <li>  Abra a pasta com seu editor ou se for VS Code, apenas digite " code . " no terminal </li>
   <li>  Com o editor aberto, insira na raiz do projeto a credencial do banco, o arquivo json copmpartilhado no Google Drive  </li>
   <li>  Pronto, execute o script shell! Ele instalará as libs necessárias e já iniciará a execução do programa! </li>  

  ```
  $ sh run.sh
  ```
  
<p> Ao terminar o processo, o módulo clear.py fará a limpeza dos arquivos locais que foram usados para atualizar o BigQuery. Ao temrinar você verá a seguinte mensagem no terminal: </p>

<div align="center">
<img src="https://github.com/saractavares/scraping-python-google-play-scraper/blob/main/readme/Screenshot_20211214_172644.png?raw=true" href="" alt="msg de conclusão no terminal">
</div>

<h3> Análise e Insights</h3> 

<p> Ao analisar os dados recolhidos dos reviews do app Alexa, pude notar alguns padrões de comportamento das pessoas que deram seus comentários. Entre eles, a versão de maior sucesso, com mais reviews positivos, e a de mnor sucesso, pelo motivo contrário. Também, os motivos mais comuns de reclamação e se estes tem relação com a pessoa ou com o app. Ficarei feliz de apresentar as análises numa reunião.
Abaixo, poderá ver o report gerado automáticamente pela lib Pandas-Profiling. Entretanto, construí meu próprio dashboard em um html com o Google Data Studio.</p>

<div style="display: inline_block" >
     <img align="center" alt="sara-HTML" src="https://github.com/saractavares/scraping-python-google-play-scraper/blob/main/readme/aval_positivas.png?raw=true">
</div>

<h3> Considerações Finais </h3>

<p> Gostei muito de trabalhar neste desafio, usando minha stack para algo que tenho muito gosto, que é a área de dados e tudo o que ela envolve e representa. No futuro, pretendo implementar melhorias de acordo com as necessidades ao projeto de scrap e talvez automatizar ainda mais.</p>


### Bibliotecas Usadas:

- google-play-scraper  -> para fazer o scraping
- pandas-profiling     -> para gerar os reports em html
- pandas-gbq           -> para manipular o banco de dados Google BigQuery
- pandas               -> para manipular os csv que irão para o banco
- google-auth          -> para autenticação da api do banco


  ### O fluxo de toda a execução é:

```
1º scrap.py -> faz -> scraping por meio da lib google-play-scraper 
   depois   -> invoca -> tratamento.py
2º tratamento.py -> faz -> limpeza dos dados coletados e organização por score 
        depois   -> invoca -> file_factory.py
3º file_factory.py -> faz -> 3 arquivos html de report usando a lib pandas-profiling 
          depois   -> invoca -> drop.py
4º drop.py -> faz -> checagem se existe já tabelas no banco de dados, se sim, as apaga 
  depois   -> invoca -> insert_tables.py
5º insert_tables.py -> faz -> inserção dos arquivos csv nas tabelas correspondentes por meio de pandas_gbq
           depois   -> invoca -> clear.py
6º clear.py -> faz -> limpeza dos arquivos csv já consumidos da raiz local

--- Fim do Processo --- 
  
  * módulo extra *
  reports_clear.py -> limpa os reports gerados da raiz do projeto. Acionado manualmente quando necessário.
```
<div align=center> 
  <a href="https://instagram.com/dadososfatos/" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
  <a href = "mailto: sara27082011@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://www.linkedin.com/in/saractavares" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
  <a href="https://saractavares.github.io/" target="_blank"><img src="https://img.shields.io/badge/-Portifolio-%d31717?style=for-the-badge&logo=portifolio&logoColor=<d31717>" target="_blank"></a>
</div>
