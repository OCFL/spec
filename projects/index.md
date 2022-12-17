# Guidelines for OCFL Projects

## Table of Contents
- [Guidelines for OCFL-based Projects](#guidelines-for-ocfl-based-projects)
  - [When to create new vs. requesting to co-maintain](#when-to-create-new-vs-requesting-to-co-maintain)
  - [What to include in a README file for a project](#what-to-include-in-a-readme-file-for-a-project)
  - [Communicating about your OCFL-based project](#communicating-about-your-ocfl-based-project)
  - [Finding new maintainers for your OCFL-based project](#finding-new-maintainers-for-your-ocfl-based-project)
- [Guidelines for OCFL Contributed Projects in the OCFL GitHub](#guidelines-for-ocfl-contributed-projects-in-the-ocfl-github)
  - [How to include a contributed project in the OCFL GitHub](#how-to-include-a-contributed-project-in-the-ocfl-github)
  - [Co-maintaining contributed projects](#co-maintaining-contributed-projects)
  - [Taking over unsupported contributed projects](#taking-over-unsupported-contributed-projects)

## Guidelines for OCFL-based Projects
### When to create new vs. requesting to co-maintain 
Within open-source communities, too often new projects are started with nearly similar functionality; this leads to confusion and inefficiency. The OCFL community ascribes to the philosophy of collaboration over competition. With that in mind, please consider the following guidelines or ideas before starting a new OCFL-based project:
* Before creating a new OCFL-based project, please do a little research and search for an existing project with the same functionality. You might start by taking a look at our Implementation List on the OCFL wiki.
* Consult other developers of other projects before creating your own. Determine if they need assistance with their project, perhaps instead you can work together to improve an existing project rather than introduce yet another one, as that leads to confusion and frustration for the community.

These guidelines are meant to help foster the OCFL community and ensure that we build upon the work of each other.

### What to include in a README file for a project
All OCFL-based Projects should have a README file. The following sections should be included in the README:
* **Introductory content**
  * _Introduction._ Include a brief paragraph or two that summarizes the purpose and function of this project. 
  * _Maintainers._ Identify maintainers of the project, at minimum their GitHub username should be included.
  * _Table of contents._ This should be included if your README file is long. It will help users with navigating the document.
* **Technical information**
  * _Installation._ Provide instructions on how to install the software.
  * _Dependencies._ Make it clear whether this project requires other software or libraries to work. Provide information about any OCFL extensions the project is dependent on and link to them.
  * _Testing Schema._ Include information about how the project is tested, include any information about testing platforms, objects, etc. the project uses.
* **Support information**
  * _Issue and bug submission._ Let users of the OCFL-contributed project know where they should submit issues and bugs and what they can expect when they do so. [REQUIRED]
  * _Documentation._ Other documentation like example usage, recommended configurations, and usage considerations. [OPTIONAL]

### Communicating about your OCFL-based project
Below are some strategies you can employ to communicate about your project to the OCFL Community:
* Add your project to the [Implementation List on the OCFL wiki](https://github.com/OCFL/spec/wiki/Implementations).
* Send an email to the [OCFL Community](https://groups.google.com/g/ocfl-community) about any updates on your OCFL-based project.
* Post an announcement in the #ocfl Slack channel in the Code4Lib workspace or in any other relevant Slack workspaces about any updates on your OCFL-based project.  

### Finding new maintainers for your OCFL-based project
Below are some strategies you can employ to find new maintainers for your project:
* Edit the project’s README file and indicate you are seeking a new maintainer.
* File an issue in the project's issues section and use the title "Seeking new maintainer for [PROJECT_NAME]". Provide an explanation of your motivation and the current state of the project.
* Post an announcement in the #ocfl Slack channel in the Code4Lib workspace or in other relevant Slack workspaces. 
* Contact people who consistently post issues or pull requests for your project. See if one of them is interested in maintaining or assisting with the project.
* Post an announcement on the [OCFL community list](https://groups.google.com/g/ocfl-community). Point to the issue which should include information about your motivation and the current state.

## Guidelines for OCFL Contributed Projects in the OCFL GitHub
Contributors are able to host OCFL-based projects within the OCFL GitHub. The benefits of hosting your project are:
* **Community-owned.** By hosting your contributed project in the OCFL GitHub you are indicating that the project is community-owned, not owned by a particular person or organization. 
* **Consistency.** Contributed projects hosted on the OCFL GitHub use a framework that creates consistency among the different contributed projects; both how to find them and also how to contribute to them.
* **Maintenance.** The OCFL Editors will try to ensure that contributed projects are maintained. If a project owner is no longer able to maintain it, and cannot identify a new maintainer themselves, they should inform the Editors. The Editors will then work with the community to try and identify a new maintainer or co-maintainers for the project. 

### How to include a contributed project in the OCFL GitHub
Below are the steps you take in order to host your OCFL-contributed project in the OCFL’s GitHub.
1. Send an email to ocfl-editors@googlegroups.com requesting to add a contributed project to the OCFL GitHub. Include in the email a link to the existing repository which should have a README file, a permissive license governing the code (Apache2, MIT, etc), your GitHub username, and information about organizations that are using the project.
2. The OCFL Editors will review your request and will respond back letting you know whether or not the repository can be included in the OCFL GitHub and any next steps.

### Co-maintaining contributed projects
Everyone can submit issues or pull requests to any repository in the OCFL GitHub at any time. Co-maintainers are individuals who usually have the permissions necessary to merge pull requests, commit to the main branch, and thus change a project’s code. If a project is not being maintained, you may be able to become the maintainer.
* Commit access is granted by the OCFL Editors in conjunction with current project maintainers. 
* Applicants should have already read each issue and participated in supporting the project or being involved in architectural and technical discussions. Ideally, applicants are also available in the #ocfl Slack channel in the Code4Lib workspace to answer any questions about the project.
* Project maintainers should have submitted 2 to 3 pull requests without any objections or remarks. Simple patches do not count.

### Taking over unsupported contributed projects
If you have been working in the issues section of an OCFL-contributed project, and you find that your work is not being acknowledged by the owner, the maintainer, or co-maintainers, you may be interested in becoming the project's owner, or being added as a co-maintainer/maintainer; doing so may advance the development of the project. You can also use the below process if you are a co-maintainer and you think it is more appropriate for you to become the project's owner or maintainer.
1. File an issue in the project's issues section stating your interest in becoming the owner, maintainer, or co-maintainer. Give links to your work on the project demonstrating to others you are interested in improving and are actively involved in the project. Point out the motivation behind your request. (For example, you are already using the project and you want it to be well-maintained.)
2. For the issue title, use “Offering to maintain [PROJECT_NAME]” or “Offering to co-maintain [PROJECT_NAME]”. 
3. Include a record of the attempts to make contact in the issue summary, spelling out who, when, and how. This information helps the OCFL Editors determine if they should act immediately or make their own attempts to contact the owners/maintainers/co-maintainers.
4. If the owner replies and sets you up as a co-maintainer or maintainer, the issue is fixed.
5. If the owner agrees to make you the new owner but cannot change the project owner, or the owner agrees to your request but doesn't make any change, tag the OCFL Editors (@OCFL/editors) in the issue and let them know there is agreement but the owner is unable to make the change. 
6. If the owner privately agrees to transfer the ownership, ask for a comment on the issue you created.
7. If the owner doesn't reply after one month, tag the OCFL Editors (@OCFL/editors) letting them know there has been no movement for a month. The OCFL Editors will normally try to contact the owner as an extra safeguard. If the owner still doesn't respond, the OCFL Editors will make a final decision about the request.
8. A project that has been unmaintained for more than 6 months despite the efforts of the current maintainers and/or the Editors to identify a maintainer will be tagged as “Unmaintained”. The README will be updated to indicate this status and indicate that developers should avoid dependencies on the project. Nevertheless, such a project may still be revived through the process above. 
