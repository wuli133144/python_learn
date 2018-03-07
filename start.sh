#!/bin/bash
#
#
#wuyuije


if [[  $UID -ne 0 ]]; then
	#statements
	echo "must be root"
	sleep 1
	exit 1
fi


if [[ ! -e /usr/bin/python ]]; then

	#statements
	yum install python python-devel

fi

python $1

if [[ $? -ne 0 ]]; then

	echo "run $@ is failed!"
	sleep 1
	exit 1
	#statements
fi