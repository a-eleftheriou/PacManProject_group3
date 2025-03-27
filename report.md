# Group 3 Report

## Antonios
I forked the repo, added all group members as contributers, and generally managed the logistics of the group. I contributed to the repo by creating the game_board branch, which included 'implementing' game_board.py and writing tests for it (which I later found out were unneeded, but at that point I had already written them, so they stayed). I also created this report file for the repo and approved Joshua's pull request.

## Harleen
I contributed to this repo by managing two merge requests, which consisted of reviewing the code line-by-line and sending forward approval comments. I also tested the game out for any bugs and identified 2 key issues that interfered with gameplay: (1) the score fails to increment after consuming dots/ghosts, (2) the ghosts don't go back to their original positions when the game restarts (if a ghost somehow stopped you at your starting position, you can't really restart the game). I then chose the first bug I found and developed a test to show the bug: it generates a pellet at the same position where the player starts so that it tests if the score is 10, which in this case it is 0 as the score never updates.

## Bhavini
I contributed to the repo by 'implementing' the ghost.py file as well as writing tests for the file. Similarly to Antonios, I did not realize that the tests were unnecessary, but left them in as I had already written them. I ensured to test the initial ghost setup as well as the movement patterns of the ghosts. I also created 2 PR's to merge my code -- for some reason, the initial commit did not copy over the test file, so I committed to my branch again (manually) and created a second PR for the test file.
