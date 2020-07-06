# Notes on releasing a new version

The 1.0 version uses [respec](https://w3c.github.io/respec/) with a custom profile. A fork of respec with the
OCFL profile is maintained at https://github.com/OCFL/respec. The behaviour of 
respec can be tailored by editing the files in `src/ocfl`. 

A new version of the compiled respec distribution can be made with:

`$ node ./tools/builder.js --profile=ocfl`

in the forked respec repo.

Some of the custom behaviours depend on files located in the `assets` directory 
of the spec. These include SVG images of the coloured flag, and some CSS files that 
will display the correct background image depending on the value used for the `specStatus`.
At present, only `REC` (Recommendation) and `NOTES` have specific behaviours. All 
other values use only the base format.

The CSS files import the base.css file from the W3C.

