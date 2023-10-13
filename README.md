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


# Maubot development environment

## Initial setup

The environment is built around Vagrant:

    $ vagrant up

Now create a virtualenv to install maubot on your host machine:

    $ python3 -m venv venv
    $ source ./venv/bin/activate
    $ pip install maubot

## Login to the maubot instance

After the vagrant box has been deployed, log in to the maubot instance (from your host machine)
using the command:

    mbc login -s http://maubot.tinystage.test:29316/ -u admin -p mypassword -a maubot-tinystage-test

## Add a new client to maubot

A client in maubot is a 1:1 link to a user on matrix.
this returns a link that you have to open in a browser, log in though ipsilon to the
account that will be used on matrix / fedora.im, and it should then be added to maubot

    mbc auth --sso -c -h fedora.im -s maubot-tinystage-test

If you want to use matrix.org and login using a password, run:

    mbc auth -c -h matrix.org -s maubot-tinystage-test


## Setup an instance

Finally go to the webui and login with admin:mypassword and set up an instance
for the plugin to the matrix user:

    http://maubot.tinystage.test:29316/_matrix/maubot/

To use the instance with Tinystage, configure the `maubot-fedora` plugin with:

    fasjson_url: https://fasjson.tinystage.test/fasjson
    pagureio_url: https://pagure.io
    paguredistgit_url: https://src.tinystage.test
