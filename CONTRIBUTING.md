# Contributing

Contributions to this documentation are welcome.

## Use Cases

We are collecting [Use Cases](https://github.com/ocfl/Use-Cases) from as broad an audience as possible.
These use cases will help inform and direct the specification. The easiest way of contributing to this specification
is to review the use cases. You can signal your support by commenting or simply "Thumbs-Up"ing a particular
use case. 

## Glossary

If you wish to use a term that requires a consistent definition, you should use the Glossary function, which
will automatically detect that term in text and link it to a definition in the Glossary.

Add your term to the `GLOSSARY.md` file as an `h2`:

```
## Foo
This is my definition of the term 'Foo'.
```

When you use the term 'Foo' in your text, it will then be automatically linked to its definition in the Glossary. 

## Linking to Normative Definitions

To help with validation, software should be able to link to specific rules in the definition, providing
users with an easy method of referencing the documentation from their OCFL clients. By default, headers
will be automatically addressed with an Anchor, so clients may construct a URL that includes this anchor.

# Installation (for local editing)

This project is built using Gitbook, and is deployed using GitHub pages. To get started, you will need to install the gitbook-cli package using the Node Package Manager:

`$> npm install -g gitbook-cli`

This will install the command so that it is globally accessible.

Editors and contributors can check out the source for the specification from GitHub and run a local
Gitbook service.

`$> git clone https://github.com/ocfl/spec`

Install the Gitbook plugins:

`$> gitbook install`

Start a local server:

`$> gitbook serve`

The Gitbook should be available at `http://localhost:4000`. Changes to the Gitbook will automatically cause your browser
to reload the page, showing the latest edits.

# Deploying (for Editors only)

Note that deploying will push to the `gh-pages` branch only. You will still have to commit your changes
to the source in the master branch as a separate action.

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



