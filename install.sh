#!/bin/bash

# Colores de texto
rojo='\033[0;31m'
verde='\033[0;32m'
azul='\033[0;34m'
reset_color='\033[0m'  # Restablecer el color a su valor predeterminado


# Comprueba si Python 3 está instalado
if ! command -v python3 &>/dev/null; then
    echo "Python 3 no está instalado. Instálalo antes de continuar."
    exit 1
fi

if ! command -v pip3 &>/dev/null; then
    echo "pip no está instalado. Instálalo antes de continuar."
    exit 1
fi


pip install pipenv


pipenv install
# Continúa con el resto del script aquí

echo "Downloading dataset"

export KAGGLE_USERNAME=sebastiancastroroman
export KAGGLE_KEY=377bff452902ebc73d574fe0c4f734f5

kaggle datasets download -d ashishpatel26/facial-expression-recognitionferchallenge

echo "Unziping dataset"
unzip facial-expression-recognitionferchallenge.zip

rm facial-expression-recognitionferchallenge.zip
rm ./Submission.csv
mkdir datasets
mv ./fer2013/fer2013/fer2013.csv ./datasets/fer2013.csv
rm -rf ./fer2013

echo -e "To activate this project's virtualenv, run ${verde}pipenv shell${reset_color}.
Alternatively, run a command inside the virtualenv with ${verde}pipenv run${reset_color}."

unset KAGGLE_USERNAME
unset KAGGLE_KEY