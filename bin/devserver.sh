#!/bin/bash

BASE_DIR=`dirname $0`
WORKING_DIR=`pwd`

echo ""
echo "This script starts all the services needed to develop the pop research project"
echo "------------------------------------------------------------------------------"

# Default parameters
#
HOST="127.0.0.1"
PORT="5000"
PROCFILE_PATH="/bin/procfiles/Procfile.dev"
PROCFILE=$WORKING_DIR$PROCFILE_PATH
ENVFILE=".env"

# Parse the command line flags
#
while getopts ":np:e:f:" opt; do
    case $opt in
        n)
          # Get the IP address on mac
          HOST=`ifconfig | grep -E 'inet.[0-9]' | grep -v '127.0.0.1' | awk '{ print $2}' |head -n1`
          ;;

        p)
          # set the port
          #
          PORT=${OPTARG}
          ;;

        e)
          # set the environment file
          #
          ENVFILE=${OPTARG}
          if [[ ! -e "$ENVFILE" ]]; then
              die "... your specified $ENVFILE does not exist"
          fi
          ;;

        f)
          # set the procfile
          #
          PROCFILE=${OPTARG}
          if [[ ! -e "$PROCFILE" ]]; then
              die "... your specified $PROCFILE does not exist"
          fi
          ;;

        \?)
          echo "Invalid option: -$OPTARG" >&2
          ;;

    esac
done

# custom die function
#
die () { echo >&2 -e "\nRUN ERROR: $@\n"; exit 1; }

# check for required programs
HONCHO=$(command -v honcho || command -v foreman || die "...Error: honcho/foreman is not in your path!")

# Print config
#
echo ""
echo "Configuration:"
echo -e "\tProcfile: $PROCFILE"
echo -e "\tENVFILE: $ENVFILE"
echo -e "\tHONCHO: $HONCHO"
echo -e "\tHOST: $HOST"
echo -e "\tPORT: $PORT"
echo -e "\tPATH: $PATH"
echo ""
echo "---------------------------------------------------------"

# start the other processes. See bin/Procfile.dev
#
HOST=$HOST PORT=$PORT $HONCHO start -e $ENVFILE -f $PROCFILE
