#!/usr/bin/env bash
#This script is for startting the server in a given python venv
#Alternatively one can simply run n2AServer.py

set -e
/dls_sw/i10/scripts/beamline/common/class/NexusAsciiConverter/src/venv/bin/python3 -u /dls_sw/i10/scripts/beamline/common/class/NexusAsciiConverter/src/n2AServer.py 
