#!/bin/bash

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`

pm2 start $SCRIPTPATH/bot.py --name "HamzaUtils" --interpreter python3

pm2 save
