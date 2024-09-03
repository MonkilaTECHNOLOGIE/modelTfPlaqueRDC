# Détection de Plaques d'Immatriculation pour la RDC

Ce projet utilise YOLOv5 et TensorFlow.js pour détecter les plaques d'immatriculation spécifiques de la République Démocratique du Congo (RDC) en temps réel à l'aide d'une caméra. L'application web permet de capturer des images de plaques d'immatriculation, de les reconnaître et de les vérifier avec une base de données Firebase.

## Table des Matières

- [Installation](#installation)
- [Structure du Projet](#structure-du-projet)
- [Entraînement du Modèle](#entrainement-du-modèle)
- [Conversion du Modèle](#conversion-du-modèle)
- [Déploiement de l'Application Web](#deploiement-de-lapplication-web)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Installation

1. Clonez le référentiel YOLOv5 dans le répertoire du projet :

    ```bash
    git clone https://github.com/ultralytics/yolov5.git
    ```

2. Accédez au répertoire `yolov5` et installez les dépendances :

    ```bash
    cd yolov5
    pip install -r requirements.txt
    ```

3. Installez les dépendances supplémentaires nécessaires pour ONNX et TensorFlow.js :

    ```bash
    pip install onnx onnx-tf tensorflowjs
    ```

## Structure du Projet

La structure du projet est organisée comme suit :

