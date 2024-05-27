Fedora Infrastructure runs a handful of bots on Matrix to help Fedora Project Contributors. This repository is kind of a meta-repo for users to file issues with the bots, and to contain the development environment for hacking on the plugins that we develop.

Fedora Infrastructure runs a Maubot instance, that deploys the following bots:

* **zodbot**
  a bot with commands for the Fedora Community, it can provide information about Fedora Users and Groups, as well as package ownership information.

  It currently is running the following maubot plugins:
  * [maubot-fedora](https://github.com/fedora-infra/maubot-fedora)
  * [maubot-adminclient](https://github.com/fedora-infra/maubot-adminclient)
* **meetbot**
  a bot to that records logs and minutes for meetings held on matrix. Note that the meetings functionality used to be part of zodbot in the IRC days, but is now split out into a seperate bot.

  This bot is installed with the following maubot plugins:
  * [maubot-meetings](https://github.com/GregSutcliffe/maubot-meetings)
  * [maubot-adminclient](https://github.com/fedora-infra/maubot-adminclient)

* **nonbot**
  nonbot is primarily the bot we use for notifications, things such as pagure notifications that get sent automatically to channels

  This bot is installed with the following maubot plugins:
  * [maubot-pagure-notifications](https://github.com/fedora-infra/maubot-pagure-notifications)
  * [maubot-adminclient](https://github.com/fedora-infra/maubot-adminclient)


# Matrix bots development environment

This repo also contains a full development environment for testing and developing on the matrix bots.

It is built around [tiny-stage](https://github.com/fedora-infra/tiny-stage) which gives the environment
access to Fedora Messaging, Fedora Accounts, and a bunch of other stuff.

## Initial setup

1. First, ensure the base machines of tiny-stage are running. If you are also testing fedora-messages from the bots, you may want to also run the datagrepper tinystage machine.

2. Start the vagrant machine (matrixbots) 
    ```
    vagrant up
    ```

## Using the environment

### Logging in to matrix

The environment runs its own matrix server at http://matrixbots.tinystage.test/

Log into this server (with your matrix client of choice) with the following details, and the aaronhale user should already be in a room called `testroom` with the bots.

* **username:** `aaronhale`
* **password:** `password`
* **homeserver:** `http://matrixbots.tinystage.test`

### maubot admin interface

The maubot admin interface is available at: 

http://matrixbots.tinystage.test:29316/_matrix/maubot/

* **username:** `admin`
* **password:** `mypassword`

### meetbot logs and mote

An instance of mote is also running in the development environment at:

http://matrixbots.tinystage.test:9696/

and the raw logs (meetbot-raw.fedoraproject.org equivalent) are accessible at

http://matrixbots.tinystage.test:8009/

The mote consumer and worker are also running, and should consume any message sent to the tinystage fedora messaging bus, and upodate mote accordingly.

If you need to troubleshoot this use the following command on the vagrant machine to get the logs for all the mote services:

```
sudo journalctl -u mote-worker -u mote-consumer -u mote
```

### hacking on the plugins

During provisioning, we clone copies of the plugins (and mote) from git before installing them to maubot. These are located on the VM in the `/home/vagrant/` directory.

These clones are also mounted (and synced to the VM) and available on the host machine in the following directories:

* _maubot-fedora
* _maubot-meetings
* _mote

If you make changes to the plugins and want to update them on the maubot instance, wun commands like this on the VM:

```
cd /home/vagrant/maubot-fedora/
mbc build -u
```

this will build and upload the plugin to maubot, and restart the plugin.
