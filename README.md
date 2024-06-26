# **DBCMetadataTools**
A collection of metadata tools for DigitalBC, used to extract, verify, delete . . . 

# api2csv.py
Pulls title and a URL field from the [DigitalBC](https://info.digitalbc.ca) implementation of the [Supplejack API](https://github.com/DigitalNZ/supplejack_api), and places in a csv file. Extract only the item types (Categories) you specify


# api2csvFull.py
Pulls all records a fields from the [DigitalBC](https://info.digitalbc.ca) implementation of the [Supplejack API](https://github.com/DigitalNZ/supplejack_api), for analysis in a .csv. 

Really, just a more usefuL and bloated version of `api2csv.py`



# thumbchecker.py
Using a .csv file with the thumbnail_url field pulled from the [DigitalBC](https://info.digitalbc.ca) implementation of the [Supplejack API](https://github.com/DigitalNZ/supplejack_api), via `api2csv.py` checks for the presence of a thumbnail (indicated by the presence of a 200 status code - and an image render of ~1mb)

Assumes a csv with a "Thumbnail_URL" column with one url per line



# GetMongoID.py
Using the `internal_identifier` field from the [DigitalBC](https://info.digitalbc.ca) implementation of the [Supplejack API](https://github.com/DigitalNZ/supplejack_api), 
batch extracts the the `_id` from an API record in Mongo. Record this info for a batch deletion in Solr. 

Extract multiple the `internal_identifier` fields from the API with a refined seacrh, or by using `api2csv.py`

example: 

```
https://viurrspace.ca/handle/10613/5030
https://viurrspace.ca/handle/10613/5240
```

returns: 
```
63cafc4cf138a006e13c5717
63cafdb9f138a006d915d4ee
```




# DeleteMongoBatch.py
Batch Mongo delete using the `internal_identifier` field.



example: 

```
https://viurrspace.ca/handle/10613/5030
https://viurrspace.ca/handle/10613/5240
https://viurrspace.ca/handle/10613/24880
```


returns:
```
Found document - _id: 63cafc4cf138a006e13c5717, internal_identifier: https://viurrspace.ca/handle/10613/5240
Found document - _id: 63cafdb9f138a006d915d4ee, internal_identifier: https://viurrspace.ca/handle/10613/5030
Found document - _id: 63eff0c8f138a0ab4d723ae9, internal_identifier: https://viurrspace.ca/handle/10613/7006
```

Then in Solr > Core > Documents (XML)
```
<delete>

<query>id:"SupplejackApi::Record 63d0540147f6ab05c9e4a00e"</query>
<query>id:"SupplejackApi::Record 63d0540647f6ab04cffb3ff7"</query>
<query>id:"SupplejackApi::Record 63d0542247f6ab05c9e4a0a2"</query>
  . . . 
</delete>
<commit/>
```
 
 Your API results should reflect the deleted items
