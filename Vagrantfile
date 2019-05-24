# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/bionic64"
    config.vm.box_check_update = true

    config.vm.network "forwarded_port", guest: 8000, host: 8000 # django dev server
    config.vm.network "forwarded_port", guest: 80, host: 8080 # web server
    config.vm.network "forwarded_port", guest: 8889, host: 8889 # mapproxy
    config.vm.network "forwarded_port", guest: 5432, host: 15432 # postgresql

    config.vm.synced_folder "./", "/usr/local/apps/COMPASS"

end
