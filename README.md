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
