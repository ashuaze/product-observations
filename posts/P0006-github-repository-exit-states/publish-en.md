### 1/6

1/6

A maintainer who wants to “leave” a GitHub repository may need one of three different outcomes: stop changes, hand over responsibility, or remove the project.

Archive, transfer, and delete look adjacent in Settings. They solve different jobs.

### 2/6

2/6

Archive makes a repository read-only while preserving it as a reference. People can still search it, fork it, and star it; an owner can unarchive it later.

That fits “maintenance has stopped,” not “this content should disappear.”

https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories

### 3/6

3/6

Transfer keeps the project alive under a new owner. Issues, pull requests, wiki, stars, and watchers move with it, and old repository links redirect.

But GitHub Pages URLs do not redirect, and permissions or plan features can change.

https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository

### 4/6

4/6

Deletion’s blast radius depends on relationships. Deleting a public repository leaves its forks; deleting a private one deletes its forks. Team permissions are permanently removed.

So “delete” is not one uniform operation.

https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository

### 5/6

5/6

GitHub says some deleted repositories can be restored within 90 days. A non-empty fork network can block self-service restoration, and restored repositories do not regain team permissions.

A recovery window is not a promise of full rollback.

https://docs.github.com/en/repositories/creating-and-managing-repositories/restoring-a-deleted-repository

### 6/6

6/6

Decision rule: archive when reference matters; transfer when stewardship continues; delete when ongoing availability is the problem.

For builders, separate pause, handoff, removal, and recovery. “Are you sure?” cannot decide which job the user meant.
