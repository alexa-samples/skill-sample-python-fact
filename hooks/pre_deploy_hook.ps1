# Powershell script for ask-cli pre-deploy hook for Python
# Script Usage: pre_deploy_hook.ps1 <SKILL_NAME> <DO_DEBUG> <TARGET>
 
# SKILL_NAME is the preformatted name passed from the CLI, after removing special characters.
# DO_DEBUG is boolean value for debug logging
# TARGET is the deploy TARGET provided to the CLI. (eg: all, skill, lambda etc.)
 
# Run this script under the skill root folder
 
# The script does the following:
#  - Create a temporary 'lambda_upload' directories under each SOURCE_DIR folder
#  - Copy the contents of '<SKILL_NAME>/SOURCE_DIR' folder into '<SKILL_NAME>/SOURCE_DIR/lambda_upload'
#  - Copy the contents of site packages in $VIRTUALENV created in <SKILL_NAME>/.venv/ folder
#  - Update the location of this 'lambda_upload' folder to skill.json for zip and upload
 
param( 
    [string] $SKILL_NAME,
    [bool] $DO_DEBUG = $False,
    [string] $TARGET = "all"
)

if ($DO_DEBUG) {
    Write-Output "###########################"
    Write-Output "##### pre-deploy hook #####"
    Write-Output "###########################"
}
 
if ($TARGET -eq "all" -Or $TARGET -eq "lambda") {
    $ALL_SOURCE_DIRS = Get-Content -Path "skill.json" | select-string  -Pattern "sourceDir" -CaseSensitive
    Foreach ($SOURCE_DIR in $ALL_SOURCE_DIRS) {
        # Step 1: Decide source path and upload path
        $FILTER_SOURCE_DIR = $SOURCE_DIR -replace "`"", "" -replace "\s", "" -replace ",","" -replace "sourceDir:", ""
        if ($FILTER_SOURCE_DIR.endsWith("/lambda_upload")) {
            $UPLOAD_DIR_PATH = $FILTER_SOURCE_DIR
            $CODE_PATH = $FILTER_SOURCE_DIR.replace("/lambda_upload", "")
        } else {
            $UPLOAD_DIR_PATH = $FILTER_SOURCE_DIR + "/lambda_upload"
            $CODE_PATH = $FILTER_SOURCE_DIR
        }
        # Step 2: Create empty lambda_upload folder
        Remove-Item -Recurse -Force $UPLOAD_DIR_PATH -ErrorAction Ignore
        New-Item -Force $UPLOAD_DIR_PATH -ItemType "directory" 2>&1 | Out-Null
 
        # Step 3: Copy source code in sourceDir to lambda_upload 
        $EXCLUDE_PATH = Resolve-Path -Path ((pwd).Path + "/" + $UPLOAD_DIR_PATH)
        robocopy $CODE_PATH $UPLOAD_DIR_PATH /s /e /ndl /XD $EXCLUDE_PATH 2>&1 | Out-Null
 
        # Step 4: Find virtual environment site packages, copy contents to lambda_upload
        $SITE = $(.venv\skill_env\Scripts\python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
        Copy-Item "$SITE\*" -Destination $UPLOAD_DIR_PATH -Recurse 
 
        # Step 5: Update the "manifest.apis.custom.endpoint.sourceDir" value in skill.json if necessary
        if (!$FILTER_SOURCE_DIR.endsWith("/lambda_upload")) {
            $RAW_SOURCE_DIR_LINE = "`"sourceDir`": `"$FILTER_SOURCE_DIR`""
            $NEW_SOURCE_DIR_LINE = "`"sourceDir`": `"$UPLOAD_DIR_PATH`""
            (Get-Content "skill.json").replace($RAW_SOURCE_DIR_LINE, $NEW_SOURCE_DIR_LINE) | Set-Content "skill.json"
        }
    }
    
    if ($DO_DEBUG) {
        Write-Output "###########################"
    } 
 
    exit 0
}
