# Using Git


To start using git, we are going to first need to get a repository. Please run:
```bash
git clone <repo_url>
```
with the url being: https://github.com/chaseguy15/Bootcamp.git in this case. This is how you download a remote repository from Github.

When we want to update our local branch to make the upstream branch, we use:
```bash
git pull
```

## Branching

To check your local branches, use branch. To move to another branch use checkout.

```bash
git checkout
git branch
```

To create and move to a new branch, run:

```bash
git checkout -b <branch_name>
```
Finally, to complete a branch and move those change over, we will use merge. This should only be done when big tasks are completed and will require code reviews.
```bash
git merge
```

## Commit and Pushing

Now let's say we have changed some code and we want to save that locally in case we want to go back. We can run add, commit to make a permanent save. This should be done at the end of at least every day you are working on code. It is recommended you do this every time you complete a small task.
```bash
git add .
git commit -m "<commit message>"
```

Finally, to push your last local commit to the origin, we will use:

```bash
git push
```

If you have not yet set the upstream branch, you will need to run:
```bash
git push --set-upstream origin <upstream_branch>
```
