#!/bin/bash
# Shell script for ask-cli pre-deploy hook for Python
# Script Usage: pre_deploy_hook.sh <SKILL_NAME> <DO_DEBUG> <TARGET>
 
# SKILL_NAME is the preformatted name passed from the CLI, after removing special characters.
# DO_DEBUG is boolean value for debug logging
# TARGET is the deploy TARGET provided to the CLI. (eg: all, skill, lambda etc.)
 
# Run this script under skill root folder
 
# The script does the following:
#  - Create a temporary 'lambda_upload' directories under each SOURCE_DIR folder
#  - Copy the contents of '<SKILL_NAME>/SOURCE_DIR' folder into '<SKILL_NAME>/SOURCE_DIR/lambda_upload'
#  - Copy the contents of site packages in $VIRTUALENV created in <SKILL_NAME>/.venv/ folder
#  - Update the location of this 'lambda_upload' folder to skill.json for zip and upload
 
SKILL_NAME=$1
DO_DEBUG=${2:-false}
TARGET=${3:-"all"}
SKILL_ENV_NAME="skill_env"
 
if ! $DO_DEBUG ; then
    exec > /dev/null 2>&1
fi
 
echo "###########################"
echo "##### pre-deploy hook #####"
echo "###########################"
 
if [[ $TARGET == "all" || $TARGET == "lambda" ]]; then
    grep "sourceDir" ./skill.json | cut -d: -f2 | sed 's/"//g' | sed 's/,//g' | while read -r SOURCE_DIR; do
        # Step 1: Decide source path and upload path
        if [[ $SOURCE_DIR == */lambda_upload ]]; then
            ADJUSTED_SOURCE_DIR=${SOURCE_DIR%"/lambda_upload"}
            UPLOAD_DIR=$SOURCE_DIR
        else
            ADJUSTED_SOURCE_DIR=$SOURCE_DIR
            UPLOAD_DIR="$SOURCE_DIR/lambda_upload"
        fi
 
        # Step 2: Create empty lambda_upload folder
        echo "Checking for lambda_upload folder existence in sourceDir $ADJUSTED_SOURCE_DIR"
        rm -rf $UPLOAD_DIR
        mkdir $UPLOAD_DIR
 
        # Step 3: Copy source code in sourceDir to lambda_upload 
        echo "Copying source code in $SKILL_NAME/$ADJUSTED_SOURCE_DIR folder to $SKILL_NAME/$UPLOAD_DIR"
        rsync -avzq --exclude '*lambda_upload' $ADJUSTED_SOURCE_DIR/* $UPLOAD_DIR
 
        # Step 4: Find virtual environment site packages, copy contents to lambda_upload
        echo "Copying dependencies installed in $SKILL_NAME/.venv/$SKILL_ENV_NAME to $SKILL_NAME/$UPLOAD_DIR"
        SITE=$(.venv/$SKILL_ENV_NAME/bin/python -c 'from distutils.sysconfig import get_python_lib; print(get_python_lib())')
        cp -r $SITE/* $UPLOAD_DIR
 
        # Step 4: Update the "manifest.apis.custom.endpoint.sourceDir" value in skill.json if necessary
        if ! [[ $SOURCE_DIR == */lambda_upload ]]; then
            echo "Updating sourceDir to point to lambda_upload folder in skill.json"
            RAW_SOURCE_DIR_LINE="\"sourceDir\": \"$SOURCE_DIR\""
            NEW_SOURCE_DIR_LINE="\"sourceDir\": \"$UPLOAD_DIR\""
            sed -in "s#$RAW_SOURCE_DIR_LINE#$NEW_SOURCE_DIR_LINE#g" ./skill.json
        fi
    done
    echo "###########################"
fi
 
exit 0
