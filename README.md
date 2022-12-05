# LOG6309E-Intelligent-DevOps
Final Project for the Intelligent DevOps of Large-Scale Software System course

Steps: 
1- lttng create sessionName --output='path'

2- lttng enable-channel --userspace userChannelName

3- lttng enable-channel --kernel kernelChannelName

4- lttng enable-event -c kernelChannelName -k -a

5- lttng enable-event -c userChannelName --python -a

6- lttng add-context --userspace -t vtid -t vpid

7- lttng add-context --kernel -t tid -t pid

8- lttng start

Do Something

9- lttng stop

10- lttng destroy


##How to solve lttng errors
###Error: Events: Kernel tracer not available
When you install lttng there is one specific package that gets installed: lttng-modules-dkms
This package installs a bunch of kernel module to be able to get lttng kernel events. When running apt upgrade, it will upgrade this package and reinstall the kernel modules but because it recompiles these modules, sometimes it runs into some issues, and does not install those modules properly.
That is why sometimes when you try running lttng -k you get this error even though it worked before
so what you need to do is to try reinstalling those modules and try to fix that error

```
sudo apt update && sudo apt upgrade
sudo apt install lttng-modules-dkms --reinstall
```

or if you still have problem you should remove two files
```
cd / .
cd /etc/apt/sources.list.d
sudo rm lttng-ubuntu-ppa-focal.list
sudo rm lttng-ubuntu-ppa-focal.list.save 
sudo apt autoremove lttng-tools lttng-modules-dkms
sudo apt update && sudo apt upgrade
 sudo apt install lttng-modules-dkms
```
