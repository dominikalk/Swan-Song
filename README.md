# Group Text Based Game

This text based game is going to be made within a group for a cardiff university project. This file will mark out convensions we will use and how to set up the repo

## Git global setup

```
Git global setup
git config --global user.name "<Your Name>"
git config --global user.email "<Your Email>"
```

## Cloning the project

```
git clone https://gitlab.cs.cf.ac.uk/c21024669/group-text-based-game.git
cd group-text-based-game
```

This will only work if you have access to the repo

## Let's try to create your first branch and push to the repo

What does checkout mean?
Checkout means moving from one branch to another
```
git checkout <branch name>
```
would switch branch to the name specified
Make sure all changes are staging (commited) if switching branch

To create a new branch use the -b tag
```
git checkout -b <branch name>
```
would switch to a new branch of the name specified

### Branch naming convention

We will preface the branch name with either **feature/** or **fix/** and then write the description of the branch as an non capitalised non spaced string
E.g. *feature/mapcolours* or *fix/playerspeed*

### Tracking files and Staging changes

To track files run 
```
git add <file name>
```
to track a specific file
or
```
git add .
```
to track all edited files

To stage changes run
```
git commit -m '<commit message - MAKE IT GOOD :) >'
```

### Pushing and pulling

To push to the remote repo
```
git push origin <repo name (the branch you were working on)>
```

To pull from the remote repo
```
git pull origin main
```
to pull from main so you get everyones changes

