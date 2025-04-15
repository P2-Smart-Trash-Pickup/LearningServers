import os, time
from influxdb_client_3 import InfluxDBClient3, Point

token = "iq7ZpTRE-DmrJ_90oWBCLV14IM2k9xxUweVJqpDDn5wZ_5OY5v83ut4pFTyE_P83nRHTbP0p8vvjoVQAW8-atA=="
org = "Gruppe 251"
host = "https://eu-central-1-1.aws.cloud2.influxdata.com/"

client = InfluxDBClient3(host=host, token=token, org=org)
database="hovedpine"

data = [
    {
        "køn":"mand", 
        "navn":"marton",
        "alder":8,

    },{
        "køn":"mand", 
        "navn":"mortin",
        "alder":23,
    },{
        "køn":"mand", 
        "navn":"william",
        "alder":21,
    },{
        "køn":"mand", 
        "navn":"alexander",
        "alder":17,
    },{
        "køn":"mand", 
        "navn":"emil",
        "alder":29,
    },{
        "køn":"ikke mand", 
        "navn":"josephine",
        "alder":72+16,
    }

]
for point in data:
    output = (
        Point("alder")
        .tag("køn",point["køn"])
        .field(point["navn"],point["alder"])
    )
    client.write(database=database,record=output)
    time.sleep(1)
    