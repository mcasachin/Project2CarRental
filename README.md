To map existing code to git repo --
echo "# Project2CarRental" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mcasachin/Project2CarRental.git
git push -u origin main

To clone a existing repo --
https://www.youtube.com/watch?v=Uz_mTOQL9Tw
git clone https://github.com/mcasachin/PythonSImpl  - Clone file to loacl

To check inc ode to github repo 
after chaning all the files 
git status		To view current status of added/modified files
git commit -m "first commit"
git add. 		To add all modified files to loacl repo (git add filename for specific files)
git resotre  filename.txt 		To undo changes of a file 
git resotre -- staged filename.txt 	To undo add file to local repo
git commit -m 'firstgit - Commit file to local repo'	To coomit file to loacl repo
git push 				To push file to cloud


Create a Branch and checkin to github
git branch firstbranch 		- create first branch
git checkout firstbranch 	- checkout branch
git branch 			- list of branch 
git commit -m "first commit"
git add. 			- To add all branch modified files to loacl repo (git add filename for specific files)
git push 			- To push branch file to cloud
git checkout master		- checkout Master
git merge			- Merge with Master
git push 			- To push master to cloud

git diff			- To comapre working directory and staging directory
git diff --staged		- To comapre staging file with last commited files

Genral commands --
git remote -v  		To know the origin of project - HTTP URL of project
vim filename		To edit a filename
git log			To view logs
git clear		To clear view
git log	--patch -1	To view specific logs.
git config --global user.email "mcasachin@gmail.com" - config usermail
git config --global user.name "Sachin"- config username
git revert commitid  	To undo all commit id and check in
git revert -n commitid 	To undo specific commit id
git reset commit id  	To go to specific commitid
git -difftool




  
