####################################################
# This file contains the user configuration.       #
# You will need to change the values in this file. #
####################################################

#
# GitHub API information
#

# The GitHub repository to add the Pull Request to:
GITHUB_REPO = 'N-BodyShop/changa'

# Pull requests will be created by this GitHub user if the real user is not
# in the map below
github_default_username = 'changa-import'

# Maps Github user names to their Github access tokens. The tokens can be
# generated in Settings -> Developer Settings -> Personal access tokens,
# Generate new token. Only the public_repo scope is necessary.
github_tokenmap = {
  'changa-import':  '681cacbd8342cd77a379391e55bbf9be24cca03a',
}

# Maps Gerrit user names to Github user names:
github_usermap = {
  'Gerrit user':  'GitHub user',
}
