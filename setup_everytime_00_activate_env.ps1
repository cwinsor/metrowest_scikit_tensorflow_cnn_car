# activate the virtual environment
# if the pymote_env does not exist - give user a good message
if (Test-Path '.\pymote_env\Scripts\activate' -PathType Leaf) {
    .\pymote_env\Scripts\activate
    } else {
    "did not find pymote_env\Scripts\activate - do you need to run setup_onetime?"
    }




