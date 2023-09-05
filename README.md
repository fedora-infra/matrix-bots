**This is written as if we are living in the future -- only the staging bots are running, and are in active development**

Fedora Infrastructure runs a handful of bots on Matrix to help Fedora Project Contributors. This repository is kind of a meta-repo for users to file issues with the bots, and to contain the development environment for hacking on the plugins that we develop.

Fedora Infrastructure runs a Maubot instance, that deploys the following bots:

* **zodbot / zodbot-stg**
  a bot with commands for the Fedora Community, it can provide information about Fedora Users and Groups, as well as package ownership information.

  It currently is running the following maubot plugins:
  * [maubot-fedora](https://github.com/fedora-infra/maubot-fedora)
  * [maubot-adminclient](https://github.com/fedora-infra/maubot-adminclient)
* **meetbot / meetbot-stg**
  a bot to that records logs and minutes for meetings held on matrix. Note that the meetings functionality used to be part of zodbot in the IRC days, but is now split out into a seperate bot.

  This bot is installed with the following maubot plugins:
  * [maubot-meetings](https://github.com/GregSutcliffe/maubot-meetings)
  * [maubot-adminclient](https://github.com/fedora-infra/maubot-adminclient)


