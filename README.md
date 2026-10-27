# INTEMPO

### The Daily Music Guessing Game
#### Group Project for CSCI 4830, Intro to Software Engineering
#### Group Members: Chris, Audra, Alex, Jorge, and Jonathan

---

## REPO CONTRIBUTION INSTRUCTIONS:
1. Open your AWS server via SSH:
    **~> ssh <username>@<server-address>**
2. Create a new directory wherever you want
    **~> mkdir <dir-name>**
3. Clone this repository
    **~> git clone https://github.com/brewInstallMetroid/InTempo**
4. Make a branch to commit your changes to
    **~> git branch <branch-name>**
    - note: would be nice to follow these prefixes, but not a big deal if we don't:
        1. DEVOPS: Changes to repo/git/dev environment (ex. README changes, .gitignore changes)
        2. IMPL: Application changes, new code or new functionality
        3. BUGF: Bugfix, repairing broken business logic or fixing up code
    - example branch: "IMPL: Initialized user interface, scaffolded new BL class."
5. Once changes are done, make sure everything is committed and pushed
    **~> git commit -m "<your-message>"**
    **~> git push <OPTIONAL-your-branch>**
    - *if pushing brings up authentication issues*, leave changes committed and run:
    **~> git remote add origin git@github.com:brewInstallMetroid/InTempo.git**
    - this should work every time and let you push without a new ssh key or any of that malarky
6. Then go to GitHub in your browser: https://github.com/brewInstallMetroid/InTempo
7. Click the "Pull Requests" tab at the top of the webpage
8. Click "Create Pull Request"
9. Now find and select your branch and use whatever title you want, once again, would be nice to follow the DEVOPS, IMPL, BUGF notation but it's not the end of the world
10. After pull request is created, press the gear next to the "Reviewers" section of the rightmost column
11. Choose any collaborator to code review your changes
12. Once code review is done, press the "Squash and merge" button or use a merge commit.  Not a big deal either way

---

### All done!
#### Let Chris know if you have issues!

---

### TECH STACK (subject to whatever changes):
- Django/Python framework with a thin JavaScript front end
- Using the built-in Django sqlite database as our db
