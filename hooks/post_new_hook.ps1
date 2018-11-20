# Powershell script for ask-cli post-new hook for Python
# Script Usage: post_new_hook.ps1 <SKILL_NAME> <DO_DEBUG>
 
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

param( 
    [string] $SKILL_NAME,
    [bool] $DO_DEBUG = $False
)

if ($DO_DEBUG) {
    Write-Output "###########################"
    Write-Output "###### post-new hook ######"
    Write-Output "###########################"
}
 
function create_env () {
    # Check for Python3 installation
    python -V | Select-String -Pattern "Python 3." 2>&1 | Out-Null
    if ($?) {
        python -m venv $ENV_LOC 2>&1 | Out-Null
        if ($?) {
            return $true
        }
    }
    return create_using_virtualenv
}
 
function create_using_virtualenv() {
    # Check for virtualenv installation or install
    python -m pip install virtualenv 2>&1 | Out-Null
    if ($?) {
        python -m virtualenv $ENV_LOC 2>&1 | Out-Null
        if ($?) {
            return $true
        } 
    }
    if ($DO_DEBUG) {
        Write-Output "There was a problem installing virtualenv"
    }
    return $false
}
 
function install_dependencies($PARAM_SOURCE_DIR) {
    # Install dependencies at lambda/py/requirements.txt
    $PYTHON_PATH = $ENV_LOC + "\Scripts\python"
    $REQUIREMENTS_PATH = $SKILL_NAME + "\" + $PARAM_SOURCE_DIR + "\requirements.txt"
    $CMD = "$PYTHON_PATH -m pip -q install -r $REQUIREMENTS_PATH"
    return Invoke-Expression $CMD 2>&1 | Out-Null
}
 
 
$SKILL_ENV_NAME = "skill_env"
$ENV_LOC = $SKILL_NAME + "\.venv\" + $SKILL_ENV_NAME
if (create_env) {
    $SKILL_FILE_PATH = $SKILL_NAME + "\skill.json"
    $ALL_SOURCE_DIRS = Get-Content -Path $SKILL_FILE_PATH | select-string  -Pattern "sourceDir" -CaseSensitive
    if ($DO_DEBUG) {
        Write-Output "Created $SKILL_ENV_NAME virtualenv at $ENV_LOC"
        Write-Output "###########################"
        Write-Output "Installing dependencies based on sourceDir"
    }
    Foreach ($SOURCE_DIR in $ALL_SOURCE_DIRS) {
        $FILTER_SOURCE_DIR = $SOURCE_DIR -replace "`"", "" -replace "\s", "" -replace ",","" -replace "sourceDir:", "" 
        if (-Not (install_dependencies $FILTER_SOURCE_DIR)) {
            if ($DO_DEBUG) {
                Write-Output "Codebase ($FILTER_SOURCE_DIR) built successfully."
            }
        } else {
            if ($DO_DEBUG) {
                Write-Output "There was a problem installing dependencies for ($FILTER_SOURCE_DIR)."
            }
            exit 1
        }
    }
    if ($DO_DEBUG) {
        Write-Output "###########################"
        Write-Output "Activate the environment before installing any other dependencies by running 'source $ENV_LOC/bin/activate'"
    }
    exit 0
} else {
    exit 1
}
