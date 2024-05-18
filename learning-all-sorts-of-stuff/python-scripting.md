
Python virtual environments

    # for virtual environments: on ubuntu you first need to install the following package (beats me)
    apt install python3.10-venv

    # create the virtual env
    python -m venv myvenv

    # activate the virtual env
    source myvenv/bin/activate
	    #(prompt changes after that)

    # if there is a requirements.txt file:
    pip install -r requirements.txt

    # create requirements (after having installed some pip packages)
    pip freeze > requirements.txt

    Benefit: pip install puts up everything in /site/packages - shared thing, can get clogged up. This way every environment is kind of isolated.

    # deactivate virtual environment myvenv
    deactivate


Pip show installed package version of numpy
     pip show numpy


Show all packages
     pip list

Show all packages as a tree (which one requires which one)

   # need to install the thing
   pip install pipdeptree

   pipdeptree


   # extremely usefull thing - i wonder why they don't have something like that as part of pip, without having to install some package, that is.


Force upgrade a package to latest?

    pip install --upgrade --force-reinstall cryptography

=========

Working with binary data. - Python

(Perl and Python are similar to this respect - they pack/unpack the fields - according to some printf-like text spec (the spec is called 'the template')
Nodejs/Javascript doesn't do that - they have java like readUint8, writeUint8 functions for binary de-serialisation.


https://perldoc.perl.org/perlpacktut


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

