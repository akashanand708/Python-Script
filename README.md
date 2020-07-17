# Lint your js/ts/rb files using Python script 

Python script to run your linter for your only changed javascript, typescript and ruby files.

## Note: Anyone can modify this file to use it for own purpose.

## Problem statement:
##### Traditional way of linting our changed files
We add some script tag in **package.json** like
```sh
"lint:server": "eslint 'app/server/**/*.js' 'app/server/**/*.ts' 'app/server/**/*.tsx'"
```
and we run 
```sh
yarn lint:server
```
from root of our project where **package.json** lies.

Suppose, we are working in a code base connected to **github**, when we **modify** many files and add **new files** to our code base, let's say **10 or 20 files**.
we want to run our linter 
```sh
(yarn eslint or BE linter command )
```
only for **changed files**, not for **all file**.
It will not be optimised way to use 
```sh
yarn lint:server
```
every time though we have only small number of changed files.



### Steps to use
1. Make sure we have python installed.
2. Go to the root of the project.
3. Add all the untracked files into git, which you want to commit.
4. nvm use **<**node version**>** **(if you are using nvm to switch to your node versions for your project or skip this)**
4. python3 BE_FE_Linter.py **or** python BE_FE_Linter.py


License
----

MIT


**Free script, Hell Yeah!**
