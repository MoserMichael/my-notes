
====================
mongodb

https://www.mongodb.com/docs/manual/reference/command/

Mongo (just like Elasticsearch) is a document oriented database. 

Mongo DB - holds a set of "collections"
    DB identified by name 
        - may not have following chars in it:  /, \, ., ", *, <, >, :, |, ?, $, space, \0, 
        - limited to 64 chars length
        - case sensitive

Mongo "collection" - similar to SQL table (but you don't have to define a schema in Mongo).
     - "collection" identified by its name ( "" is not a valid collection name, no $ chars or \0 chars in the name; may not start with prefix "system.")
     - can store very different json documents in a collection, but that's not a good idea!
     - Recommendation: store json docs of similar structure in the same collection (this allows you to do search)
        
    
A "document" in Mongo is an entry in a "collection" (it's a JSon file)- equivalent to a db "Row"; 
    - each "document" gets it's generated special _id field (12 bytes long - binary value)
    - id structure: 
            [4 bytes timestamp]
            [4 bytes - machine id]
            [2 bytes - pid]
            [3 bytes - incremented counter]
    - id field is always indexed, so you can lookup a document by it's id value!

Didn't know that mongo-db is used for search; so in what sense there is a equivalence with ElasticSearch ?

        - https://cloud.netapp.com/blog/cvo-blg-elasticsearch-vs-mongodb-6-key-differences

            - inserts are faster in mongo,  (mongo is written in C++, whereas elasticsearch is java)
                - better suited for document structured data (? don't you have a schema in elasticsearch too?)
            - text search is faster in elasticsearch

- mongo daemon (by default it listens on port 27017) 
  HTTP admin UI is listening port + 1000 (default: 28017)

- mongo shell: can enter expressions in json - that's very natural, as you can look at json documents as javacript maps/arrays. 
    - the document _id is represented as ObjectId class,.

    (or you can use alternative GUI based clients - like "Robo 3T")

    - shell commands
        var coll = db.getCollection("collectionName");  // lookup of collection object; or you can do as db.collectionName - but get an error if hte collection does not exist.
        
        - collection thing has all sorts of manipulation methods 
                - coll.insert({"person","Bob", "profession" : "Drummer"})  // insert doc, _id field is added upon insertion
                - var existingDoc = coll.findOne({"person" : "Bob"});    // find one doc, given a field
                - coll.update({"person":"Bob"}, { '$set' : { "profession":"Teacher" }}) ;  // first argument: query for doc like this, second argument: how to change the entry, once it was found. 
                - coll.find({}) // find all of them
    
        - update expressions can have all sorts of operators,
                $set - set the value of a field

                $inc, 

                $rename (rename field) 

                $push (adding to array)
                    coll.update({"person","Aob"}, {"$push", {"children" : { "Andrew" } } });

                $addToSet - like push, but prevents duplication of entries

                {$pop : { "key": 1}} - remove element from beginning of array "key", {$pop : { "key": -1}} - remove from the end 
                
                $pull - remove matching documents

                $each - push more than one entry (in an array)

                $slice - limit the size of an array to maximum n elements (or remove n - if n is negative)
                
                $sort - sort array by given key entry (provided that array has objects where all objects have the given key attribute)

            https://www.mongodb.com/docs/manual/reference/operator/update/
            https://www.mongodb.com/docs/manual/reference/operator/

        - find queries can have a lot of these (that one tries to be similar to sql SELECT...)  https://www.mongodb.com/docs/manual/reference/operator/query/    

    - Example session:

====

mongosh - the mongo shell

Accessing mongo: use the mogosh shell (mongo - that is the old shell, it was deprecated)
        (installation instructions: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/ )

- in mongosh every map on a collection will return a Cursor object. You can convert it into a javascript array with toArray (big difference!!!)
    - but toArray() will take a lot of time - the cursor is evaluated just as it is needed, whereas toArray() will walk the whole query!!!
      (i had to do it, when translating an index from one db into another one, they were using the same index field values, so I had to get them all...)

Reference on db.collection.find - query, projection, etc. etc.

    https://www.mongodb.com/docs/manual/reference/method/db.collection.find/

mongosh

    working with really large datasets

    - makes sense to save a result to file (use node trick)
        fs.writeFileSync('file_big_array.json', JSON.stringify( variable_you_want_to_store ) )

    - in the new shell mongosh
        a=fs.readFileSync('file_big_array.json').toString()

---

    # show db names - select a particular db name as the current one
        show dbs
        use <dbname>

    # show name of all collections in current db.
        show collections

        db.getCollectionNames() // this one returns an iterator - won't show all of them.

    
    # other stuff when working in shell.

---

> c=db.createCollection("tst")
{ "ok" : 1 }

> c=db.getCollection("tst")

> c.update({_id: 123}, { '$addToSet': {'a': 1, 'b': 2, 'c' :3} }, { 'upsert': 'true'})
WriteResult({ "nMatched" : 0, "nUpserted" : 1, "nModified" : 0, "_id" : 123 })

> c.find({_id: 123})
{ "_id" : 123, "a" : [ 1 ], "b" : [ 2 ], "c" : [ 3 ] }

> c.update({_id: 123}, { '$addToSet': {'d': 4, 'e': 5, 'e' :5} }, { 'upsert': 'true'})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

> c.find({_id: 123})
{ "_id" : 123, "a" : [ 1 ], "b" : [ 2 ], "c" : [ 3 ], "d" : [ 4 ], "e" : [ 5 ] }

---

Aggregation queries: (that's what they do for 'join')
/these get complex, but are terribly important/
    
    https://www.mongodb.com/docs/manual/core/aggregation-pipeline/#std-label-aggregation-pipeline


-----

Interesting detail: they often add a field that tells if an entry has been deleted or not.
That looks crazy - in SQL one would always delete a record, instead of adding a 'isactive' or 'isdeleted' field.


It seems that this is a kind of historical artifact: - from prior to 2019

https://stackoverflow.com/questions/6086245/is-remove-an-expensive-operation-in-mongodb

    
    this answer is a historical artifact from 2011 and it refers to the old MMAPv1 engine which was removed in 2019.

    MongoDB stores the data in a double linked list and so removing results is adjusting two links, the next link of the previous document and the previous link of the next document. There is no autocompacting. 
    Updating, if you have a value already stored, happens in place, changing one value. Now... you think, great, update one int instead of two pointers, surely faster! Not so -- you now need to index on this flag and creating indexes is "slow".


Culture, my ass...

----

-----

A function that shows all collections in all DB instances into a file - can run it from the mongo shell.

    function showAllCollectionsInAllDBS() {

        const fs=require("node:fs");

        let dbs = db.adminCommand(
           {
             listDatabases: 1
           }
        );


        let lstIt = ""

        for(let i=0; i < dbs.databases.length; ++i) {

            try {
                let dbname = dbs.databases[i].name;

                let dbnow = db.getSiblingDB(dbname);

                lstIt += "databaseName: " + dbname + "\n";

                let colNames = dbnow.getCollectionNames();

                for(let j=0; j< colNames.length;++j) {

                    lstIt += "\tcollection: " + colNames[j] + "\n";
                }
            } catch(er) {
                lstIt += "error: " + er;
            }
        }

        fs.writeFileSync("listdbs.txt", lstIt);

        console.log("see file llistdbs.tx for list of dbs an collections...");
    }

