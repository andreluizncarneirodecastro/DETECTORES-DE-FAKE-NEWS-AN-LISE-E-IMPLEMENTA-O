<!doctype html>
<html>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />

    <head>
        <meta charset="utf-8">
        <title>Detector de Fake News - Sobre</title>
        <link rel="stylesheet" type="text/css" href="static/css/app.css">
        <link rel="stylesheet" href="static/css/materialize.min.css">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link href="static/css/emoji.css" rel="stylesheet">
    </head>
    <body>
        <nav>
            <div class="nav-wrapper">
                <div class="container center-align">
                    <a href="/"><span class="text" style="font-weight: bold; font-size: 18px; margin-right: 175px;">Página inicial</span></a>

                    <a href="/sobre.php"><span class="text" style="font-weight: bold; font-size: 18px; margin-left: 35px;">Sobre o algoritmo</span></a>
                </div>
            </div>
        </nav>
        <main>
            <div class="container">
                <div class="center-align">
                    <h3 id="teste">Algoritmo</h3>
                    <hr>
                </div>
                <div class="row center-align">
                    <h5 class='col s12 m10 l6 offset-l3 offset-m1'><b>Como funciona?</b></h5>
                    <p class='col s12 m10 l6 offset-l3 offset-m1'> O algorítmo funciona calculando a porcentagem de todas as notícias onde temos a ocorrência das palavras <b>(O)</b>, a porcentagem de consistência <b>(C)</b> onde começa com <b>0%</b> e vai aumentando em <b>7,5%</b> a cada palavra encontrada da qual não pertence a sentença inserida pelo usuário. Para porcentagem de cada notícia <b>(PN)</b>, temos <b>PN = O × ((100 – C) / 100)</b>.</p>

                    <p class='col s12 m10 l6 offset-l3 offset-m1'> Calcula-se, então, o total de notícias, onde possuímos o número de notícias <b>(N)</b>, soma de porcentagem de todas as notícias <b>(PNS)</b>, a porcentagem média final de todas as notícias <b>(PF)</b>. A equação final fica, então, <b>PF = PNS/N</b>.</p>

                    <p class='col s12 m10 l6 offset-l3 offset-m1'> Além do algoritmo de ocorrências que é utilizado com as informações levantadas pelo crawler, foi utilizado para obter uma maior eficiência, o algoritmo de similaridade <b>(Levenshtein)</b>, a utilização de um <b>stop-words</b> que remove artigos que são desnecessários para o entendimento do algoritmo e um <b>dicionário de sinônimos</b>.</p>
                    
                    <p class='col s12 m10 l6 offset-l3 offset-m1'> <b>Trabalho de conclusão de curso</b> <br>
                     <b>Aluno: </b>André Luiz Neilsen Carneiro De Castro <b>RA:</b> 92854
                    </p>

                
                </p>
                </div>

                <div class="row center-align">
                    <div class="input-field col s12 m10 l6 offset-l3 offset-m1">
                        <a href="DETECTORES DE FAKE NEWS ANÁLISE E IMPLEMENTAÇÃO.pdf" download><button class="btn waves-effect waves-light" type="submit">Download PDF</button></a>
                    </div>
                </div>

                <div class="row center-align">
                    <a href="https://github.com/andreluizncarneirodecastro/DETECTORES-DE-FAKE-NEWS-ANALISE-E-IMPLEMENTACAO" target="_blank"><img src="github.png" alt="Github" style="width: 80px;"></a>
                </div>
            </div>
        </main>
        <footer class="page-footer">
            <div class="container">
                Fundação Hemínio Ometto
                <span class="text right">2021</span>
            </div>
        </footer>
        <script src="static/js/jquery-3.1.0.min.js"></script>
        <script src="static/js/materialize.min.js"></script>
        <script src="static/js/app.js"></script>
    </body>
</html>