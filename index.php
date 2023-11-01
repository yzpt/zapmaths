<?php
session_start();
try {
    // On se connecte à MySQL
    $bdd = new PDO('mysql:host=localhost;dbname=general;charset=utf8', 'username', 'password');
} catch (Exception $e) {
    // En cas d'erreur, on affiche un message et on arrête tout
    die('Erreur : ' . $e->getMessage());
}

if (!isset(($_POST['identifiant'])) or !isset(($_POST['mdp']))) {
    // pas d'info en POST, on redirige vers la page d'identification auth.php
    $_SESSION['log'] = FALSE;
    header("Location: auth.php");
    exit();
} else {
    // infos en POST, on récupère les infos utilisateur et on redirige vers le portail home.php si le mdp est bon

    // On récupère contenu de l'identifiant de table_eleve
    $temp = htmlspecialchars($_POST['identifiant']);
    $reponse_sql = $bdd->query("SELECT * FROM table_eleves WHERE IDENTIFIANT = '$temp' ");
    $donnees = $reponse_sql->fetch();

    if (htmlspecialchars($_POST['mdp']) == $donnees['mdp']) {
        //si mdp ok, on charge les données user de bdd vers les données SESSION
        $_SESSION['identifiant']     = $donnees['IDENTIFIANT'];
        $_SESSION['nom']             = $donnees['NOM'];
        $_SESSION['prenom']          = $donnees['PRENOM'];
        $_SESSION['classe']          = $donnees['CLASSE'];
        $_SESSION['log']             = TRUE;
        $_SESSION['date']            = date("Y-m-d H:i:s");

        // inscription à la table registre_login
        if ($donnees['IDENTIFIANT'] != "Yohann.zapart") {
            $req2 = $bdd->prepare('INSERT INTO registre_login(id, NOM, PRENOM, IDENTIFIANT, DATE) VALUES(:id, :NOM, :PRENOM, :IDENTIFIANT, :DATE)');
            $req2->execute(array(
                'id'          => 0,
                'NOM'         => $_SESSION['nom'],
                'PRENOM'      => $_SESSION['prenom'],
                'IDENTIFIANT' => htmlspecialchars($_SESSION['identifiant']),
                'DATE'        => $_SESSION['date']
            ));
        }

        setcookie('identifiant', $_SESSION['identifiant'], time() + 365 * 24 * 3600, null, null, false, true);
        $_SESSION['num_question_a_corriger'] = rand(1, 99);


        header("Location: home.php");
        exit();
    } else {
        // mdp pas bon
        header("Location: auth.php");
        $_SESSION['mdp_faux'] = TRUE;
        exit();
    }
}
