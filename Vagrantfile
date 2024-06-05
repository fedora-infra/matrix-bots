# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.manage_guest = true

  config.vm.define "matrixbots" do |matrixbots|
    matrixbots.vm.box_url = "https://download.fedoraproject.org/pub/fedora/linux/releases/38/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-38-1.6.x86_64.vagrant-libvirt.box"
    matrixbots.vm.box = "f38-cloud-libvirt"
    matrixbots.vm.hostname = "matrixbots.tinystage.test"

    matrixbots.vm.synced_folder "_mote/", "/home/vagrant/_mote", type: "sshfs", create: true
    # matrixbots.vm.synced_folder "_logs/", "/srv/web/meetbot", type: "sshfs", create: true
    matrixbots.vm.synced_folder "_maubot-meetings/", "/home/vagrant/_maubot-meetings", type: "sshfs", create: true
    matrixbots.vm.synced_folder "_maubot-fedora/", "/home/vagrant/_maubot-fedora", type: "sshfs", create: true
    matrixbots.vm.synced_folder "_maubot-pagure-notifications/", "/home/vagrant/_maubot-pagure-notifications", type: "sshfs", create: true
    matrixbots.vm.synced_folder "_maubot-events/", "/home/vagrant/_maubot-events", type: "sshfs", create: true
    matrixbots.vm.synced_folder ".", "/vagrant", disabled: true

    matrixbots.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 2
      libvirt.memory = 2048
    end

    matrixbots.vm.provision "ansible" do |ansible|
      ansible.playbook = "devel/ansible/matrixbots.yml"
      ansible.config_file = "devel/ansible/ansible.cfg"
      ansible.verbose = true
    end
  end

end
