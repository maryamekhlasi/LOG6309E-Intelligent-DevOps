# LOG6309E-Intelligent-DevOps
Final Project for the Intelligent DevOps of Large-Scale Software System course

Steps: 
lttng create sessionName --output='path'
lttng enable-channel --userspace userChannelName
lttng enable-channel --kernel kernelChannelName
lttng enable-event -c kernelChannelName -k -a
lttng enable-event -c userChannelName --python -a
lttng add-context --userspace -t vtid -t vpid
lttng add-context --kernel -t tid -t pid
lttng start
Do Something
lttng stop
lttng destroy
