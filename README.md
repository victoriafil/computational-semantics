# Computational Semantics (LT2213)

Labs and other materials for LT2213 Computational semantics


# Group works guidlines

## Table of content
1. [Requirements](#requirements)
2. [Start a group-lab](#start-a-group-lab)
3. [Working on the assignments](#working-on-the-assignments)
4. [Submitting the work](#submitting-the-work)


## Requirements

In order to submit an assignment you need a private github repository with student discount:

1. If you don't have `git`, install it on your system (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
1. Sign up for GitHub (https://github.com/).
1. Go to https://education.github.com/ and sign up for the Student Developer Pack to get unlimited private repositories. You are a "student" and you want an "individual account". Once you have completed these first steps, you are then ready to create your private GitHub repository for this class.
1. Setup your terminal acceess with ssh-key from your local computer to your github account. (https://github.com/settings/keys)

## Start a group-lab

Everyone in the group is expected to work on the assignment individually.
The group work gives you more chance to solve issues and learn about other possible solutions.
The goal of this guideline is to maximises your remote performance.

There are two general roles in the group that could be any member of the group:
- Repository manager `userm`: owning the repository and sharing the admin role with others.
- Final submision admin `userf`: sharing screen when preparing the final submission.


#### Repository manager

- Choose one person as repository manager: `userm`
- `userm` creates a private github repository. (Initialise with README, and ignore Python) 
- The repository name should be `lt2213-lab-x-group-y` (`x` for the lab number and `y` for group number).
- Add all group members and all course instructors (`adamlek`, `mmehdig`, `sdobnik`) as collaborators with Admin role in the repository settings.
(https://github.com/userm/lt2213-lab-x-group-y/settings/access)
- `userm` adds the lab matterial as a module in your repository.
In the terminal:
```
git clone git@github.com:userm/lt2213-lab-x-group-y
cd lt2213-lab-x-group-y
git submodule add https://github.com/sdobnik/computational-semantics
git commit -am "initialise the submodule"
git push
```

#### For all members

Working remotely is challenging. Each member of the group must be able to practice and learn when working on the lab assignments.
The following guidline is a suggestion for maximising the accessibility of everyone in the team.

All members should follow these steps:

- Clone from the group repository. In the terminal:
```
git clone git@github.com:userm/lt2213-lab-x-group-y
cd lt2213-lab-x-group-y
```
- Create a copy of the problem-set of the lab in the root under your username. On your terminal:
```
cp -R computational-semantics/problem-set-#/ <username>
```
- Share your work with others by add and commit in the repository:
```
git add <username>
git commit -m "message about what you are committing here."
git pull 
git push
```
- Update your repository with pull command:
```
git pull 
```

## Working on the assignments

- Try to solve problems individually.
- As a group we recommend getting online at the same time but focus on your individual work.
- If you don't understand a question, or you if you encounter an error share you question and experience with other members. 
- Let others also try to solve the question on their own.
- There might be more than one answer for each question.
- After everyone found and run an answer under each question, you need a final submission.
- When working on the final version, one user `userf` can administer the session by sharing the screen.

#### Administrating the final group submission

The admin user for the final submission, `userf`, is going to share screen with others while working on the final version.

Here is a guidline for `userf`.
- Share your screen with other team members.
- The final version must be constructed based on the contribution of everyone.
- Create a final copy from your own work:
```
cp -R userf final
```
- Let one of the members give you guidance and you follow their commands. 
- Change the role of the lead time by time. When you, `userf`, is leading your own work try to narrate what you are about to do.

## Submitting the work

Each individual member must submit in the Canvas. You can submit your work by sending a link to your group repository.


