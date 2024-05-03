### SETUP ###

# sets the api key to ebirdapitoken
source ../DO-NOT-COMMIT/api-key.sh

### REQUESTS ###
# POSTMAN DOCS: https://documenter.getpostman.com/view/664302/S1ENwy59#auth-info-124a9625-7cc9-48d5-be64-bb4fa0d59f46

# get id for Montrose
curl -i --location -g 'https://api.ebird.org/v2/ref/hotspot/geo?lat=41.96&lng=-87.63' --header "X-eBirdApiToken: $ebirdapitoken" | grep Montrose

# get info for Montrose
curl --location -g 'https://api.ebird.org/v2/ref/hotspot/info/L161180' --header "X-eBirdApiToken: $ebirdapitoken"

# get recent observations for Montrose Point Bird Sanctuary
curl --location -g 'https://api.ebird.org/v2/data/obs/L161180/recent' --header "X-eBirdApiToken: $ebirdapitoken"

# get recent observations for all Montrose hotspots
curl --location -g 'https://api.ebird.org/v2/data/obs/US-IL-031/recent?r=L22074224,L813972,L2057479,L161180,L1222076' --header "X-eBirdApiToken: $ebirdapitoken"
