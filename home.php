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
    <script src="script.js"></script>
</head>

<body>
    <nav>
        <i class="fa-solid fa-house nav--icones"></i>
        <!--
        <i class="fa-solid fa-chart-line nav--icones"></i>
        <i class="fa-solid fa-envelope nav--icones"></i>
        -->
        <p class="nav--p"><?php echo ($_SESSION['prenom'] . ' ' . $_SESSION['nom'] . ' ' . $_SESSION['classe']); ?></p>
    </nav>


    <?php
    $select_boites = $bdd->prepare('SELECT * FROM table_boites WHERE CLASSE=:classe ORDER BY POSITION');
    $select_boites->execute(array('classe' => $_SESSION['classe']));
    // $select_boites = $bdd->prepare('SELECT * FROM table_boites WHERE IDENTIFIANT=:identifiant ORDER BY POSITION');
    // $select_boites->execute(array('identifiant' => $_SESSION['identifiant']));
    while ($donnees_boites_temp = $select_boites->fetch()) {
        $n_qcm = 1;
    ?>
        <div class="card">
            <h1><?php echo $donnees_boites_temp['TITRE']; ?></h1>
            <p class="card--p"><?php echo $donnees_boites_temp['TEXTE']; ?></p>
            <?php $temp_chaine_qcm = "QCM" . $n_qcm . "_qcm";
            while ($donnees_boites_temp[$temp_chaine_qcm] != "") {
                $temp_chaine_texte = "QCM" . $n_qcm . "_texte";
                $select_niveau = $bdd->prepare('SELECT * FROM registre_niveaux WHERE IDENTIFIANT = :id AND QCM = :qcm');
                $select_niveau->execute(array(
                    'id' => $_SESSION['identifiant'],
                    'qcm' => $donnees_boites_temp[$temp_chaine_qcm]
                ));
                if ($donnees_niveau_temp = $select_niveau->fetch()) {
                    $niveau = intval($donnees_niveau_temp['NIVEAU']);
                    $objectif = intval($donnees_niveau_temp['OBJECTIF']);
                } else {
                    //on insert le niveau 0 dans le registre_niveaux
                    $niveau = 0;
                    $objectif = 10;
                    $insert_niveau = $bdd->prepare('INSERT INTO registre_niveaux(id, IDENTIFIANT, NOM, PRENOM, CLASSE, QCM, NIVEAU, OBJECTIF) VALUES(:id, :IDENTIFIANT, :NOM, :PRENOM, :CLASSE, :QCM, :NIVEAU, :OBJECTIF)');
                    $insert_niveau->execute(array(
                        'id' => 0,
                        'IDENTIFIANT' => $_SESSION['identifiant'],
                        'NOM' => $_SESSION['nom'],
                        'PRENOM' => $_SESSION['prenom'],
                        'CLASSE' => $_SESSION['classe'],
                        'QCM' => $donnees_boites_temp[$temp_chaine_qcm],
                        'NIVEAU' => $niveau,
                        'OBJECTIF' => $objectif
                    ));
                }
                echo ("<a style='text-decoration:none' href='affich_question.php?qcm=" . $donnees_boites_temp[$temp_chaine_qcm] . "'><div class='card--line ");
                if ($niveau >= $objectif) {
                    echo ("bgc--vert'>");
                } elseif ($niveau <= intval($objectif / 2)) {
                    echo ("bgc--rouge'>");
                } else {
                    echo ("bgc--bleu'>");
                }
                echo ("<div><p class='card--p'>" . $donnees_boites_temp[$temp_chaine_texte] . "</p></div><div><p class='card--p card--p--niveau ");
                if ($niveau >= $objectif) {
                    echo ("color--vert'>");
                } elseif ($niveau <= intval($objectif / 2)) {
                    echo ("color--rouge'>");
                } else {
                    echo ("color--bleu'>");
                }
                echo ($niveau . " / " . $objectif . "</p></div></div></a>");
                $n_qcm = $n_qcm + 1;
                $temp_chaine_qcm = "QCM" . $n_qcm . "_qcm";
            }
            ?>
        </div>
    <?php } ?>


</body>

</html>