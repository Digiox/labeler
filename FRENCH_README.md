# LabelCraft

## Introduction

LabelCraft est un logiciel qui permet à l'utilisateur de générer des étiquettes à partir d'un fichier CSV (séparateur point-virgule).

Vous pouvez choisir autant de fichiers CSV que vous le souhaitez, et les étiquettes seront générées les unes après les autres dans un PDF (Vous aurez un champ pour spécifier ou enregistrer ce PDF et un champ pour définir son nom).

Pour chaque fichier, vous avez un champ qui vous permet de spécifier (obligatoirement) un fournisseur.

Ainsi, chaque fichier CSV doit contenir des articles d'un seul fournisseur.

## Champs obligatoires

Votre CSV doit comporter au moins 6 colonnes (Ce seront les colonnes affichées sur l'étiquette) :

- Identifiant Produit
- Produit
- Prix de Vente
- Code-barres
- Référence Fournisseur
- Variation

Assurez-vous que les noms des champs sont écrits exactement comme ci-dessus.

## Aperçu de l'interface

<img src="assets\image.png" alt="Texte alternatif" width="50%">

Dans cette image, vous pouvez voir la composition de l'interface du logiciel :

1. Le premier champ sert à entrer le nom du fichier PDF à sauvegarder.
2. Le deuxième champ est conçu pour spécifier un emplacement sur votre ordinateur où le fichier sera téléchargé.
3. Le troisième champ concerne le fichier CSV source (bouton Parcourir pour ouvrir l'explorateur de fichiers).
4. Le quatrième champ, qui se trouve juste à droite du troisième, sert à spécifier le Fournisseur.
5. Le bouton Supprimer sert à effacer la ligne en cours.
6. Le bouton "Ajouter CSV et Fournisseur" ajoute deux champs supplémentaires pour un fichier source CSV et un fournisseur.
7. Ce sont les journaux du logiciel, où vous pouvez voir si tout s'est bien passé. Si certaines étiquettes n'ont pas pu être générées, vous pourrez le voir ici.
8. Si vous souhaitez vider le contenu des journaux, le bouton Nettoyer/Effacer est présent.
9. Le bouton pour lancer la génération une fois tous les champs remplis.

> **Remarque :** Plus vous avez de lignes dans votre CSV, plus le temps de génération sera long. Ne vous inquiétez pas, c'est normal !

## Besoins spécifiques ?

Cette version du logiciel est entièrement gratuite et non personnalisable (Elle pourrait devenir personnalisable à l'avenir).

Si vous avez besoin d'une version du logiciel spécifique à votre utilisation, veuillez envoyer un message à **bourlon.lyann84@gmail.com** et demander un devis.