#!/bin/bash
# Get departure times from some subway stations.
# launch: ./subway.sh [flag] [station]
# flags "--E" and "--W" print only eastbound or westbound subways, default is print all
# Specify stations "Blindern" or "Kolsaas" if wanted, or use Forskningsparken (default)

selectedPlatform="-1"
[ "$1" == "--E" ] && ((selectedPlatform=2)) && shift
[ "$1" == "--W" ] && ((selectedPlatform=1)) && shift

print () { echo "$line towards $stationName is leaving in/at $displayTime from plattform $platform."; }

if [ "$1" == "Kolsås"  ] || [ "$1" == "Kolsaas" ] || [ "$1" == "Kolsas" ]; then
    originalpage=$(curl -s "http://mon.ruter.no/SisMonitor/Refresh?stopid=2190450&computerid=acba4167-b79f-4f8f-98a6-55340b1cddb3&isOnLeftSide=true&blocks=&rows=&test=&stopPoint=") #Link Kolsås
    station="Kolsås"
elif [ "$1" == "Blindern" ]; then
    originalpage=$(curl -s "http://mon.ruter.no/SisMonitor/Refresh?stopid=3010360&computerid=acba4167-b79f-4f8f-98a6-55340b1cddb3&isOnLeftSide=true&blocks=&rows=&test=&stopPoint=") #Link Blindern
    station="Blindern"
else
    originalpage=$(curl -s "http://mon.ruter.no/SisMonitor/Refresh?stopid=3010370&computerid=acba4167-b79f-4f8f-98a6-55340b1cddb3&isOnLeftSide=true&blocks=&rows=&test=&stopPoint=") #Link Forskningsparken (default)
    station="Forskningsparken"
fi

page="$originalpage"
page=${page#*<tr>}  #Remove the first stuff
echo "Departures from $station:"

declare i; i=0

while [ ${#page} -gt "300" ]; do
    selection="$page"  #Select the beginning
    selection=${selection%% </tr>*} #narrow selection

    page=${page#*$selection}  #Make sure we skip last part
    page=${page#*<tr>}  #Remove the beginning

    #order to read file: line #, name, dep. time, platform #.
    line=${selection#*>}
    line=${line%% <*}
    line=$(echo "$line" | tr -d '\040\011\012\015') # Remove line-break etc.

    stationName=${selection#*$linje*<td>}
    stationName=${stationName%% <*}
    stationName=$(echo "$stationName" | tr -d '\011\012\015') # Remove stuff, but keep spaces
    stationName="$(echo -e "${stationName}" | sed -e 's/[[:space:]]*$//')" #remove trailing whitespace, however

    time=${selection#*$stationName*<td>*<td>}
    time=${time%% <*}
    time=$(echo "$time" | tr -d '\011\012\015') # Remove stuff, but keep spaces
    time="$(echo -e "${time}" | sed -e 's/[[:space:]]*$//')" #remove trailing whitespace
    displayTime="$time"

    [ "$time" == "n&#229;" ] && displayTime="now" #doing something with "n&#229;" (the word 'nå')

    platform=${selection#*$time*>*>}
    platform=${platform%%<*}

    if [ "$selectedPlatform" == "-1" ]; then
	print
    elif [ "$selectedPlatform" == "$platform" ]; then
	print
    fi
    ((i++))
    [ "$station" == "Forskningsparken" ] && [ "$i" == "6" ] && break #The assignment does not say that we _only_ can print one departure from each of the six subways,
done                                                                 #but I'm doing it here just to be sure.
                                                                     #For the other stations it's unspecified.

