# Migrating Gerrit to GitHub

1. Use `gerrit2github.py` to download Gerrit changesets and create branches on
   GitHub. See the file for information on things that need to be changed in that file.

2. Edit `config.py` to add information about collaborators, GitHub API tokens, etc.

3. Run `make_prs.py` to create Pull Requests from the GitHub branches.

## ChaNGa-specific Instructions

You will need owner/write permissions of [N-BodyShop/ChaNGa](https://github.com/N-BodyShop/changa) GitHub repository for the following.

1. Clone the GitHub repository: `git clone git@github.com:N-BodyShop/changa.git`.

2. Add Gerrit as a remote: `git add remote gerrit charmgit:cosmo/changa`.

3. Copy all Python scripts into the repo folder.

4. From inside the repo, run `python gerrit2github.py cosmo/changa`.
   Check if review branches are created on GitHub.

5. Edit `config.py`. `GITHUB_REPO` has already been set, but you need to specify the rest.
   Bogus user `changa-import` will be assigned to the pull requests for Gerrit usernames without a mapping to Github.
   Currently personal access tokens for Tim Haines, Robel, Tom Quinn, and Harshitha are required.

6. Run `python make_prs.py`. Check if pull requests are created on GitHub.
