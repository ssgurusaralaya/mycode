# Modified by S.S Gnana Guru on 28 Jun 22 at 18:16

Training of Python programing & Ansible

## Getting Started

These instructions will get you a copy of the project up and running on your local machine
for development and testing purposes. See deployment for notes on how to deploy the project
on a live system.

### Prerequisites

What things are needed to install the software and how to install them. For now, maybe copy in
"how to install python and python3 using apt."

## Built With

* [Python](https://www.python.org/) - The coding language used

## Updating Git 

Staging

# When you’ve modified a file and have marked it to go in your next commit, it is considered to be a staged file.
# Check the status of your Git repository, including files added that are not staged, and files that are staged:

git status

# To stage modified files, use the add command, which you can run multiple times before a commit. If you make subsequent changes that you want to include in the next commit, you must run add again.
# You can specify the specific file with add:

git add my_script.py

# With . you can add all files in the current directory, including files that begin with a .:

git add .

# If you would like to add all files in a current directory as well as files in subdirectories, you can use the -all or -A flag:

git add -A

# You can remove a file from staging while retaining changes within your working directory with reset:

git reset my_script.py

			Commit

# Once you have staged your updates, you are ready to commit them, which will record changes you have made to the repository.
# To commit staged files, you’ll run the commit command with your meaningful commit message so that you can track commits:

git commit -m "Commit message"

# You can condense staging all tracked files by committing them in one step:

git commit -am "Commit message"

# If you need to modify your commit message, you can do so with the --amend flag:

git commit --amend -m "New commit message"

## Authors

* **Guru** - *Initial work* - [YourWebsite](https://example.com/)
