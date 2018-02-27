# Deploying

This project is built using GitBook, and is deployed using GitHub pages. To get started, you will need to install the gitbook-cli package using the Node Package Manager:

`$> npm install -g gitbook-cli`

This will install the command so that it is globally accessible. 

## Automatic deployment

The `build.sh` script can be run to automate deployment to the gh-pages branch on GitHub. It will do the steps listed in Manual deployment below. 

`$> ./build.sh`

## Manual deployment

To build the site:

`$> gitbook build . dist/`

This will build the site and place the static assets in the `dist` folder. You should ensure these changes are then committed to the repository.

`$> git add dist && git commit -m "Commiting dist changes for deployment"`

 Git has a 'subtree push' feature that then lets us push just the `dist` folder to the `gh-pages` branch:

`$> git subtree push --prefix dist origin gh-pages`



