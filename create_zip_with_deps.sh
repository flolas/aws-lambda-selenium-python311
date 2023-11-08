#!/bin/bash

PACKAGE_PATH='./build/package/'

# Crear directorio
mkdir -p $PACKAGE_PATH

# Copiar todo el contenido del repositorio al directorio del paquete
cp -r ./src/* $PACKAGE_PATH

# Instalar las dependencias del archivo requirements.txt en el directorio del paquete
pip3 install -r requirements.txt \
--platform manylinux2014_x86_64 --only-binary=:all: --upgrade \
--target $PACKAGE_PATH

# Cambiar al directorio del paquete
cd $PACKAGE_PATH

# Comprimir todo en el directorio actual en un archivo llamado lambda_with_deps.zip en el directorio padre
zip -r ../lambda_with_deps.zip . python/lib/python3.11/site-packages/. -x "test/*" "build/*" "env/*" "infraestructure/*" "*__pycache__*"

# Regresar al directorio original
cd -

# Eliminar el directorio del paquete
rm -r $PACKAGE_PATH