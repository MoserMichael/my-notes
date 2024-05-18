---

git/github

        # fixing divergent feature branches 

            # rename branch to temporary name
            git branch -m thisfeature-tmp 

        
            git checkout develop
            git branch -m thisfeature

            # merge --squash  - get changes in one commit! solve all merge conflicts in one step!
            git merge --squash thisfeature-temp

        # github: put link to youtube video into github README
            https://www.linkedin.com/pulse/how-add-embedded-video-github-readme-file-cengiz-toru/
           
            # for me it goes as follows:::

            [<img src="https://i.ytimg.com/vi/3vnq1ltptZA/maxresdefault.jpg" width="50%">](https://www.youtube.com/watch?v=3vnq1ltptZA&t=2s "youtube video: dockerdashphp - managing your local docker engine: 55")

        # github search cheat sheet 
            https://cheatography.com/cpriest/cheat-sheets/github-search-syntax/

        # github search: limit search of term "miau" in files with file extension:*.py
        path:*.py miau

        # github serach: limit to root level of repository (can use that to limit to subdirectories)
        path:/

        # 'deleted by us' during merge or cherry-pick
            # file x was added in the commit being cherry-picked
            # file x was deleted in the branch that you cherry-pick into.
                git add x  # if you want to keep the file
                git rm  x  # if you want to delete the file.

        # 'deleted by us' during rebase - now 'us' and 'them' is reversed !!!!
            # file x was added in the branch that is being rebased
            # file x was removed in the branch that is brought in
            

        # shallow clone of linux kernel (--depth 1 - get commit history of the last commit) (much faster to clone)
        git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git linux-git --depth 1

        # sort files by extension (rev - reverts each line of the output, so that the extension (in reverse) comes first)
        git ls-files | rev | sort | rev

        # Get all commits by user (that can be useful during performance reviews...)
        # select all commits done by user

        git log --author=<user name that appears in commit messages>

        # get the commit message of all commits by user.
        git log --author=<user name that appears in commit messages> --format=%s 

        # in case that the first string is the name of the issue - get all the issues that the user did.
        git log --author=<user name that appears in commit messages> --format=%s | awk '{print $1}' | sort | uniq


        # github.com ::: open a pull request on some other repository https://github.com/AwesomeUser/AwesomeProject

        - on original repo page: create a fork (press the 'fork' button)
        - after forking: you have that repository under your own github user  https://github.com/YourOwnUser/AwesomeProject

        - clone that forked repository.
        - create a new branch of the main branch.
            git branch -m my_new_pr
        - add your changes and commit
        - set the UPSTREAM of the branch: 
            git remote add upstream https://github.com/AwesomeUser/AwesomeProject
        - push the new branch:
             git push -u origin my_new_pr
        - push command writes a long text to the console, that text includes a link to open the new pull request.   
 