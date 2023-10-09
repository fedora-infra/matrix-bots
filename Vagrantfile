# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.manage_guest = true

  config.vm.define "maubot" do |maubot|
    maubot.vm.box_url = "https://download.fedoraproject.org/pub/fedora/linux/releases/38/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-38-1.6.x86_64.vagrant-libvirt.box"
    maubot.vm.box = "f38-cloud-libvirt"
    maubot.vm.hostname = "maubot.tinystage.test"

    maubot.vm.synced_folder ".", "/home/vagrant/maubot", type: "sshfs"

    maubot.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 2
      libvirt.memory = 2048
    end

    maubot.vm.provision "ansible" do |ansible|
      ansible.playbook = "devel/ansible/maubot.yml"
      ansible.config_file = "devel/ansible/ansible.cfg"
      ansible.verbose = true
    end
  end

end
