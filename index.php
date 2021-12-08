<!doctype html>
<html>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />

    <head>
        <meta charset="utf-8">
        <title>Detector de Fake News</title>
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
                    <h3 id="teste">Analisador e Detector de Fake News</h3>
                    <hr>
                </div>
                <div class="row center-align">
                    <h5 class='col s12 m10 l6 offset-l3 offset-m1'><b>Como funciona?</b></h5>
                    <p class='col s12 m10 l6 offset-l3 offset-m1'> Esta aplicação é capaz de analisar um trecho de uma notícia e tem como saída uma porcentagem probabilística desta notícia se tratando de fake news ou não.</p>
                    <p class='col s12 m10 l6 offset-l3 offset-m1'> O trabalho é focado na atual necessidade da sociedade em diferenciar a vasta quantidade de notícias e informações que inundam o meio digital, de tal forma que este trabalho irá auxiliar as pessoas a diferenciar as notícias recebidas.</p>
                    <p class='col s12 m10 l6 offset-l3 offset-m1'> <b>Insira um título</b> referente a uma notícia que deseja ser pesquisada, para que seja indicado a porcentagem de chance dessa notícia ser falsa ou não.</p>
                    <p class='col s12 m10 l6 offset-l3 offset-m1'> <b>Exemplos:</b> "Agnaldo Timóteo morreu"; "Tiago Leifert deixa globo"; "IBM lança chip quântico"</p>
                </div>
                <form action="/">
                    <div class="row center-align">
                        <div class="col s12 m10 l6 offset-l3 offset-m1">
                            <input placeholder="Insira o trecho da sua notícia" class="materialize-textarea"  name="search"/>
                        </div>

                        <div class="input-field col s12 m10 l6 offset-l3 offset-m1">
                            <button class="btn waves-effect waves-light" type="submit">Detectar
                                <i class="material-icons right">send</i>
                            </button>
                        </div>
                    </div>
                </form>

                <?php
                    if (isset($_GET['search'])) {
                        $search = trim($_GET['search']);

                        if (strlen($search)) {
                            $cmd = 'python C:\xampp\htdocs\python\main.py ' . '"' . $search . '"';
                            $command = escapeshellcmd($cmd);
                            $output = shell_exec($command);

                            echo "<div class='center-align'>Pesquisado: '" . $_GET['search'] . "'</div>";
                            echo "<br>";
                            echo "<div class='center-align'> Porcentagem de ser verdade: <h5><b>" . $output. "</b></h5></div>";
                        } else {
                            echo "<div class='center-align'>Digite o título</div>";
                        }
                    }
                ?>
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