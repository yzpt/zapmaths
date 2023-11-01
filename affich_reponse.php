<?php
session_start();
if (!isset(($_SESSION['identifiant']))) {
    // pas d'info user en POST, on redirige vers la page d'identification auth.php
    $_SESSION['log'] = FALSE;
    header("Location: auth.php");
    exit();
}

error_reporting(E_ALL);
ini_set("display_errors", 1);
try {
    // On se connecte à MySQL
    $bdd = new PDO('mysql:host=localhost;dbname=general;charset=utf8', 'username', 'password');
    $bdd->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (Exception $e) {
    // En cas d'erreur, on affiche un message et on arrête tout
    die('Erreur : ' . $e->getMessage());
}


$num_ligne = $_SESSION['num_question_a_corriger'];
$qcm   = $_GET['qcm'];
// $requete = $bdd->query("SELECT * FROM $qcm WHERE  id = $num_ligne ");
$requete = $bdd->prepare('SELECT * FROM ' . $qcm . ' WHERE id=:num_ligne');
$requete->execute(array(
    'num_ligne'  => $num_ligne
));

while ($donnees = $requete->fetch()) {
    //pour simplifier, on met dans REPNUM la valeur REPCHOIX
    // if (isset($donnees['REPCHOIX'])) {
    //     $donnees['REPNUM'] = $donnees['REPCHOIX'];
    // }
    // if (isset($donnees['REPTXT'])) {
    //     $donnees['REPNUM'] = htmlspecialchars($donnees['REPTXT']);
    // }

    // if ($_POST['reponse_eleve'] == $donnees['REPNUM']) {
    //     //UPDATE incrémentation niveaux
    //     $req_incr = $bdd->prepare('UPDATE registre_niveaux SET NIVEAU=NIVEAU+1 WHERE IDENTIFIANT=:id AND QCM=:qcm');
    //     $req_incr->execute(array(
    //         'id' => $_SESSION['identifiant'],
    //         'qcm' => $qcm
    //     ));
    // }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <title>Zapmaths</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://kit.fontawesome.com/ba5ef4e547.js" crossorigin="anonymous"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;400&display=swap" rel="stylesheet">
    <script async="true" src="https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=AM_CHTML"> </script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="script.js"></script>
</head>

<body>
    <nav>
        <a href="home.php" style="color: inherit;"><i class="fa-solid fa-house nav--icones"></i></a>
        <!--
        <i class="fa-solid fa-chart-line nav--icones"></i>
        <i class="fa-solid fa-envelope nav--icones"></i>
        -->
        <p class="nav--p"><?php echo ($_SESSION['prenom'] . ' ' . $_SESSION['nom']); ?></p>
    </nav>


    <!-- =================== barre de progression =================== -->
    <?php
    $select_niveau = $bdd->prepare('SELECT * FROM registre_niveaux WHERE IDENTIFIANT=:id AND QCM=:qcm');
    $select_niveau->execute(array(
        'id' => $_SESSION['identifiant'],
        'qcm' => $_GET['qcm']
    ));

    if ($donnees_niveau_temp = $select_niveau->fetch()) {
        $niveau = intval($donnees_niveau_temp['NIVEAU']);
        $objectif = intval($donnees_niveau_temp['OBJECTIF']);
    } else {
        $niveau = 0;
    }
    ?>
    <table width=100%>
        <tr width=100%>
            <td align="center" width=100%>
                <?php
                for ($i = 0; $i < $objectif; $i++) {
                    echo ("<span class='");
                    if ($niveau > $i) {
                        echo ("case_verte");
                    } else {
                        echo ("case_grise");
                    }
                    echo ("'></span>");
                }
                ?>
            </td>
        </tr>
    </table>


    <!-- ============================== énoncé question ========================== -->
    <div class="card card-question">
        <?php
        $num_ligne = $_SESSION['num_question_a_corriger'];
        // $requete = $bdd->query("SELECT * FROM $qcm WHERE  id = $num_ligne ");
        $requete = $bdd->prepare('SELECT * FROM ' . $qcm . ' WHERE id=:num_ligne');
        $requete->execute(array(
            'num_ligne' => $num_ligne
        ));
        while ($donnees = $requete->fetch()) {
            if (isset($donnees['REPCHOIX'])) {
                $donnees['REPNUM'] = $donnees['REPCHOIX'];
            }
            if (isset($donnees['REPTXT'])) {
                $donnees['REPNUM'] = htmlspecialchars($donnees['REPTXT']);
            }

            if ($_POST['reponse_eleve'] == $donnees['REPNUM']) {
                //UPDATE incrémentation niveaux
                $req_incr = $bdd->prepare('UPDATE registre_niveaux SET NIVEAU=NIVEAU+1 WHERE IDENTIFIANT=:id AND QCM=:qcm');
                $req_incr->execute(array(
                    'id' => $_SESSION['identifiant'],
                    'qcm' => $qcm
                ));
            }
            echo ("<div class='boite-question'>");
            echo $donnees['ENONCE'];

            // image
            if (($donnees['IMGB64']) != "") { ?>
                <p align="center">
                    <img src="data:image/png;base64, <?php echo ($donnees['IMGB64']); ?>" alt="imgb64" style="max-width:100%" />
                </p>
            <?php }
            ?>




            <div class="espace_icone" style="text-align:center">
                <?php
                if (htmlspecialchars($_POST['reponse_eleve']) == $donnees['REPNUM']) {
                    echo ('<img src="img/icone_bonne_reponse.png" style="width:80px" align="center">');
                    echo ('<p class="texte_BR">Bonne réponse : ' . $donnees['REPNUM'] . '</p>');
                } else if ((htmlspecialchars($_POST['reponse_eleve'])) == "") {
                    echo ("<p class='texte_BR'>Réponse : " . $donnees['REPNUM'] . "</p>");
                } else {
                    echo ('<img src="img/icone_mauvaise_reponse.png" style="width:80px" align="center"><br><br>');
                    echo ('<p class="texte_MR">Mauvaise réponse (' . $_POST['reponse_eleve'] . ')</p>');
                    echo ('<p class="texte_BR">Bonne réponse : ' . $donnees['REPNUM'] . '</p>');
                } ?>
            </div>

            <!-- ======================= feedback ======================== -->
            <div align="left">
                <?php echo $donnees['FEEDBACK']; ?>
            </div>
        <?php
            // enregsitrement reponse élève
            // if ($_SESSION['log'] == TRUE) {
            if (TRUE) {
                $req2 = $bdd->prepare('INSERT INTO registre_reponses(id, IDENTIFIANT, NOM, PRENOM, CLASSE, QCM, NUM_LIGNE, REP_ELEVE, REP_VALIDE, DATE) VALUES(:id, :IDENTIFIANT, :NOM, :PRENOM, :CLASSE, :QCM, :NUM_LIGNE, :REP_ELEVE, :REP_VALIDE, :DATE)');
                $req2->execute(array(
                    'id' => 0,
                    'IDENTIFIANT' => $_SESSION['identifiant'],
                    'NOM' => $_SESSION['nom'],
                    'PRENOM' => $_SESSION['prenom'],
                    'CLASSE' => $_SESSION['classe'],
                    'QCM' => $_GET['qcm'],
                    'NUM_LIGNE' => $num_ligne,
                    'REP_ELEVE' => $_POST['reponse_eleve'],
                    'REP_VALIDE' => $donnees['REPNUM'],
                    'DATE' => date("Y-m-d H:i:s")
                ));
            }
        }
        echo ("</div>");
        $requete->closeCursor(); // Termine le traitement de la requête
        ?>
    </div>


    <div align="center" style="width: 100%;">
        <form method="post" action="affich_question.php?qcm=<?php echo $qcm; ?>">
            <button id="bouton-suivant">Question suivante &rarr;</button>
        </form>
    </div>

</body>

</html>