#!/bin/bash
# Shell script for ask-cli post-new hook for Python
# Script Usage: post_new_hook.sh <SKILL_NAME> <DO_DEBUG>
 
# SKILL_NAME is the preformatted name passed from the CLI, after removing special characters.
# DO_DEBUG is boolean value for debug logging
 
# Run this script one level outside of the skill root folder
 
# The script does the following:
#  - Create a '.venv' directory under <SKILL_NAME> folder
#  - Find if python3 is installed.
#    - If yes, try creating virtual environment using built-in venv
#      - If that fails, install virtualenv and create virtualenv
#    - If no, install virtualenv and create virtualenv
#  - If virtual environment is created, use container pip to install dependencies from ${SOURCE_DIR}/requirements.txt
#  - Provide message on activation script location and additional dependencies
 
create_env () {
    # Check for Python3 installation
    if command -v python3 &> /dev/null; then
        PYTHON=python3
        # Use Python3's venv script to create virtualenv.
        if $PYTHON -m venv "$ENV_LOC"; then
            echo "Using Python3's venv script"
            return 0
        else
            # No venv script present (< Py 3.3). Install using virtualenv
            return create_using_virtualenv $PYTHON
        fi
    else
        # Python2 environment. Install using virtualenv
        PYTHON=python
        return create_using_virtualenv $PYTHON
    fi
    return 1
}
 
create_using_virtualenv () {
    # Check for virtualenv installation or install
    if $1 -m pip install virtualenv; then
        echo "Using virtualenv library"
        # Try creating env
        if $1 -m virtualenv "$ENV_LOC"; then
            return 0
        else
            echo "There was a problem creating virtualenv"
            return 1
        fi
    else
        echo "There was a problem installing virtualenv"
        return 1
    fi
}
 
install_dependencies() {
    # Install dependencies at lambda/py/requirements.txt
    return $("$ENV_LOC"/bin/python -m pip -q install -r "$SKILL_DIR"/"$1"/requirements.txt)
}
 
SKILL_NAME=$1
DO_DEBUG=${2:-false}
SKILL_DIR=$SKILL_NAME
SKILL_ENV_NAME="skill_env"
ENV_LOC="$SKILL_DIR/.venv/$SKILL_ENV_NAME"
 
if ! $DO_DEBUG ; then
    exec > /dev/null 2>&1
fi
 
echo "###########################"
echo "###### post-new hook ######"
echo "###########################"
echo "Creating virtualenv for $SKILL_NAME"
mkdir "$SKILL_NAME/.venv"
if create_env; then
    echo "Created $SKILL_ENV_NAME virtualenv at $ENV_LOC"
    echo "###########################"
    echo "Installing dependencies based on sourceDir"
    grep "sourceDir" "$SKILL_NAME/skill.json" | cut -d: -f2 | sed 's/"//g' | sed 's/,//g' | while read -r SOURCE_DIR; do
        if install_dependencies $SOURCE_DIR; then
            echo "Codebase ($SOURCE_DIR) built successfully."
        else
            echo "There was a problem installing dependencies for ($SOURCE_DIR)."
            exit 1
        fi
    done
    echo "###########################"
    echo "Activate the environment before installing any other dependencies by running 'source $ENV_LOC/bin/activate'"
    exit 0
else
    exit 1
fi
