<?php
session_start();
try {
    // On se connecte à MySQL
    $bdd = new PDO('mysql:host=localhost;dbname=general;charset=utf8', 'root', 'Zapmaths_86!');
} catch (Exception $e) {
    // En cas d'erreur, on affiche un message et on arrête tout
    die('Erreur : ' . $e->getMessage());
} ?>


<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <link rel="stylesheet" href="style.css" />
    <title>Zapmaths.fr</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;400&display=swap" rel="stylesheet">
</head>

<body>
    <br><br>
    <div class="card card-auth">
        <form id="auth-form" action="index.php" method="post">
            <input type="text" id="identifiant" name="identifiant" placeholder="Identifiant">
            <input type="password" id="mdp" name="mdp" placeholder="Mot de passe">
            <input type="submit" value="Connexion" id="button-connexion">
        </form>
    </div>
    <br><br>
    <p class="p-white" align="center">Identifiant : prenom.nom</p>
    <p class="p-white" align="center">Mot de passe : date de naissance en 6 chiffres.<br><i>Exemple pour le 03 avril 2005 : 030405</i></p>
    <br><br>
</body>

</html>