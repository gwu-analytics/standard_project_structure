# Standard Project Readme
This is a standard project structure for Water Analytics projects.

## Project Layout
This project structure breaks up the project into a set of directories:

```
Project/
|   The .gitignore is in the root directory
|   LICENSE if applicable
|   setup.py
|   readme.md
|   Add a requirements.txt!
│
├───config/
|       * Content in this directory is gitignored
|       Store .ini files in this directory.
│
├───data/
|   |  Data, including input/output files and caching.
│   ├───cache
|   |      * Contents is gitignored
│   │      Store cached data at runtime.      
│   ├───program
|   |      Store program (hardcoded) data.  
│   ├───raw
|   |      * Contents is gitignored
│   │      Store input (raw) data as needed.       
│   └───refined
|           * Contents is gitignored
│           Store output (refined) data as needed.
├───docs/
|       Documentation beyond readmes:
|            methodology, whitepapers, etc.
│
├───logs/
|       * Content in this directory is gitignored
|       Output logging results to this directory.
│
├───notebooks/
|       Jupyter notebooks should be stored here.
│
├───scripts/
|       Store helper scripts and devtools here.
│
├───src/
|   |   The source code. Include main and modules.
│   |
│   └───your_project/
|       ├───__init.py__
|       └───main.py   
|
├───temp/
|       * Content in this directory is gitignored
|       Store files that SHOULD NOT be included in the repository!
|       I.e. Test outputs, secrets/credentials, etc.
│
├───tests/
    └───__init.py__
        └───test1.py
```
When starting a project, clone this repository and you will have the directory structure and tools you need to conform with the standard project structure!

### Directories
#### Root (project) directory
In the root directory, the following files should be stored:
- .gitignore
    - Root gitignore
    - Ignores .ini, .secret, and .log files
    - Ignores the \_\_pycache\_\_ and venv directories
- venv
    - It is best practice to create a venv for the project
    - this directory is not present in the repository
        - should be added during project setup
    - Use the standard `venv` directory name during setup to ignore automatically
- readme.md
- LICENSE if applicable
- setup.py
    - See the "Writing the setup.py script" section
- requirements.txt
    - Use `pipreqs . --force` command in the terminal to generate requirements.txt
#### config
The config directory is for storing .ini files used in the main program.
The contents of this file is ignored by git, since .ini files should be created during setup or runtime of the program.
  
Note that .ini files are ignored no matter where they are stored in the root directory as well!
#### data
The data directory is for storing input, output, program, and cached data. There are four subdirectories in this directory.
##### cache
Cached data is typically used for in-memory processing, batch jobs, saved states, etc.  
This directory's concents are gitignored.
##### program
The data/program directory is for hardcoded data used by the program at runtime.  

**!!! The data in this directory is retained in the repository !!!**
##### raw
The data/raw directory is intended for storing ingested raw data at runtime from databases or other external sources.  
This directory's content is gitignored.
##### refined
The data/refined directory is for storing output data from processes. 
Any output files should be stored here.  

**!!! This directory's content is included in the repository !!!**
#### docs
This is a location to store any reference documentation, user guides, etc.
#### logs
Store logging files in this location. 
Note that the contents of this file are gitignored.
#### notebooks
Any Jupyter Notebooks should be stored here.
#### scripts
Any development scripts should be stored here. 
By default, the clean.py and build.py scripts will be stored here for prepping the project files for deployment.
#### src
The source code of the program. To make your project into a module, you will need to dp the following:
-  Make a subdirectory; your_project\
    - Add the \_\_init.py\_\_ boilerplate
    - main.py
    - submodules
#### temp
Store any temporary files that should not be included in the repository.
Anything that includes PII or credentials should be kept here.
For anything that contains security items, use the .secret extension on your plain text files. These will be ignored by git.
#### tests
Store your test scripts here.
Add \_\_init.py\_\_ to this directory to make it a module.

## Setting up the repository
- Navigate your projects directory (wherever you store your local repositories).
- Using the command line, run the following command:  
`git clone https://github.com/gwu-analytics/standard_project_template.git`
- Copy the repository to a new directory:  
`cp -r standard_project_template new_project_name` 
- Change to the new project directory:  
`cd new_project_name`
- Remove existing git history:  
`rm -Recurse -Force .git`
- Intialize a new git repo:  
`git init`
- Using the GitHub CLI, create a remote repository:  
`gh repo create gwu-analytics/new_project_name --public --source=., --remote=origin`
- Add files and make an initial commit:  
`git add .`
`git commit -m "Initial commit message"`
- Push to remote:  
`git push origin master`
- Run the clean.py script from the scripts/ directory to remove all of the .gitkeep placeholder files from the project.
    - This will ensure that any unused files are cleaned from the remote.
- Create your virtual environment and start coding!
