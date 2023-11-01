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
    $bdd = new PDO('mysql:host=localhost;dbname=general;charset=utf8', 'root', 'Zapmaths_86!');
    $bdd->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (Exception $e) {
    // En cas d'erreur, on affiche un message et on arrête tout
    die('Erreur : ' . $e->getMessage());
}


$qcm = $_GET['qcm'];

// comptage nb de lignes/questions du qcm
$res = $bdd->query("select count(*) as nb from $qcm");
$data = $res->fetch();
$nb = $data['nb'];
$_SESSION['num_question_a_corriger'] = rand(1, $nb);


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
        $requete = $bdd->query("SELECT * FROM $qcm WHERE  id = $num_ligne ");
        while ($donnees = $requete->fetch()) {
            echo ("<div class='boite-question'>");
            echo $donnees['ENONCE'];
            echo ("</div>");

            // image
            if (($donnees['IMGB64']) != "") { ?>
                <p align="center">
                    <img src="data:image/png;base64, <?php echo ($donnees['IMGB64']); ?>" alt="imgb64" style="max-width:100%" />
                </p>
            <?php } ?>
    </div>


    <!-- ========================== formulaire ========================  -->
    <div align="center" style="width:100%;">
        <form method="post" action="affich_reponse.php?qcm=<?php echo $qcm; ?>">
            <?php
            if (isset($donnees['PROPCHOIX1'])) {

                for ($i = 1; $i < 8; $i++) {
                    $temp_chaine = 'PROPCHOIX' . $i;
                    if (($donnees[$temp_chaine] != '') & ($donnees[$temp_chaine] != '_')) {
                        $temppp = '<input type="submit" name="reponse_eleve" id="bouton-suivant" style="height:2em;" value="' . $donnees[$temp_chaine] . '"/><br>';
                        echo $temppp;
                    }
                }
            } else { ?>
                <?php
                //on regarde si c'est du repnum ou du reptxt et on place l'input adéquat
                if (isset($donnees['REPNUM'])) {
                    if ((mb_strimwidth($qcm, 0, 8) == "qcm_conv") or (mb_strimwidth($qcm, 0, mb_strwidth($qcm) - 2) == "qcm_arrondir")) { ?>
                        <input type="number" id="input-reponse" step="0.001" style="text-align: center" name="reponse_eleve" placeholder="Réponse" autocomplete="off" />
                    <?php } elseif (mb_strimwidth($qcm, 0, mb_strwidth($qcm) - 2) == "qcm_coeff_multi") { ?>
                        <input type="number" id="input-reponse" step="0.0001" style="text-align: center" name="reponse_eleve" placeholder="Réponse" autocomplete="off" />
                    <?php } else { ?>
                        <input type="number" id="input-reponse" step="0.01" style="text-align: center" name="reponse_eleve" placeholder="Réponse" autocomplete="off" />
                    <?php } ?>
                <?php } else { ?>
                    <input type="text" id="input-reponse" style="text-align: center" name="reponse_eleve" placeholder="Réponse" autocomplete="off" autocapitalize="none" />
                <?php } ?>
                <input type="submit" class="bouton-valider" value="Valider" />
            <?php } ?>
        </form>
    <?php  } ?>
    </div>




</body>

</html>