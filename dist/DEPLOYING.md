# Deploying

This project is built using GitBook, and is deployed using GitHub pages. To get started, you will need to install the gitbook-cli package using the Node Package Manager:

`$> npm install -g gitbook-cli`

This will install the command so that it is globally accessible. To build the site:

`$> gitbook build . dist/`

This will build the site and place the static assets in the `dist` folder. You should ensure these changes are then committed to the repository.

 Git has a 'subtree push' feature that then lets us push just the `dist` folder to the `gh-pages` branch:

 `$> git subtree push --prefix dist origin gh-pages`



The site needs to be built prior to deploying. Run the command:

