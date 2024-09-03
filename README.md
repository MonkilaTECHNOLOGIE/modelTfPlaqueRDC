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


## Entraînement du Modèle

1. Préparez vos données et annotations dans le dossier `datasets/`.

2. Créez un fichier de configuration `data.yaml` dans le dossier `yolov5/data/` :

    ```yaml
    train: ../datasets/images/train
    val: ../datasets/images/val
    nc: 1  # Nombre de classes (1 pour les plaques d'immatriculation)
    names: ['license_plate']
    ```

3. Entraînez le modèle YOLOv5 :

    ```bash
    cd yolov5
    python train.py --img 640 --batch 16 --epochs 50 --data data/data.yaml --weights yolov5s.pt
    ```

## Conversion du Modèle

1. Exportez le modèle YOLOv5 entraîné au format ONNX :

    ```bash
    python export.py --weights runs/train/exp/weights/best.pt --include onnx
    ```

2. Convertissez le modèle ONNX en TensorFlow, puis en TensorFlow.js :

    ```bash
    onnx-tf convert -i best_model/best.onnx -o best_model/best_tf
    tensorflowjs_converter --input_format=tf_saved_model best_model/best_tf best_model/web_model
    ```

## Déploiement de l'Application Web

1. Placez les fichiers du modèle TensorFlow.js (`model.json` et `.bin`) dans le dossier `web_app/`.

2. Ouvrez le fichier `index.html` dans un navigateur web ou servez-le à l'aide d'un serveur local :

    ```bash
    cd web_app
    python -m http.server 8000
    ```

3. Accédez à `http://localhost:8000` pour voir l'application en action.

## Utilisation

1. Cliquez sur le bouton "Activer la Caméra" pour commencer la détection en temps réel.
2. Le scanner balaiera la zone pour détecter une plaque d'immatriculation.
3. Une fois une plaque détectée, les caractères seront reconnus et vérifiés dans la base de données Firebase.
4. Les résultats seront affichés indiquant si la plaque est valide ou non.

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre des pull requests et signaler les problèmes via GitHub.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.


