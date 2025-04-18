# Part 2 Report

## Antonios
I created this report file and reviewed, approved, and merged pull requests created by teammates. Merging the .env fix was a real pain due to the web interface saying that it had to be merged via the command line, so I set up and familiarized myself with the GitHub CLI to manually merge the PR. I also caught and fixed some leftover player references after merging the namechange PR, removed the .env file from the repo after merging the change to .gitignore, and rewrote the commit history to try and remove mentions of the secret key.

## Bhavini
I worked on the "Secure Sensitive Information" part of the project. I used .gitignore to exclude the .env file from future commits and removed it from Git tracking using git rm --cached. To prevent access to sensitive data in past commits, I ran git filter-branch to clean the repository history and remove all traces of .env. The cleaned branch was then safely pushed and submitted as a pull request for review.

## Joshua
I worked on updating the player to Pac-Man wherever necessary. This included all file contents and names. I used a command involving sed and grep to check for all file contents to update "player" to "Pacman." Some files weren't completely updated, which Antonios caught and then updated accordingly. A PR was made for review. 

## Saanvi
I worked with Harleen to create the YAML file for the CI pipeline. We worked together on figuring out the format of the file, and then I added half of the implementation, from the part of installing system dependencies down to running the pytests. Then I created a PR that was made for review. 

## Harleen
I worked with Saanvi to create a ci_yaml_file_creation branch, on which we created the .github/workflows directories and implemented the ci.yml file for the CI pipeline. Specifically, I added the branch set up in the beginning and the start of jobs, including running on ubuntu, checking out the code, and setting up Python v3.10. When merging these changes, I noticed that our code was not formatted as according to Black specifications, so I pip-installed black on the python venv and ran 'black .' so that we can adhere to what Black required. Finally, I pushed those changes, resolved a few merge conflicts, and merged the ci_yaml_file_creation branch which then passed all the tests in the pipeline.
