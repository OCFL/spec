# OCFL Validation Codes

## Requirements

 - Levels of validation: ERROR, WARNING, INFO. The ERROR level corresponds with MUST in the specification, the WARNING level corresponds with SHOULD in the specification, and the INFO level is validator implementation specific.
 - OCFL Spec should define error codes to which validators MUST refer; these error codes will refer to sections in the OCFL Spec.
 - Validators MUST validate OCFL Objects
 - Validators MUST validate OCFL Storage Roots

## Errors (corresponding with MUST in specification)

| Code | Reason | Spec Reference
| --- | --- | --- |
| E001 | Missing OCFL Object NamAsTe file | https://ocfl.io/draft/spec/#object-conformance-declaration
| E002 | OCFL Object NamAsTe file name does not match Inventory OCFL Version | https://ocfl.io/draft/spec/#object-conformance-declaration
| E003 | OCFL Object NamAsTe file contents do not match file name | https://ocfl.io/draft/spec/#object-conformance-declaration
| E004 | Version directories are not sequentially named | https://ocfl.io/draft/spec/#version-directories
| E005 | Version directory $DIR is not an integer or does not start with a leading zero. | https://ocfl.io/draft/spec/#version-directories
| E006 | Version directory $DIR does not contain a `content` directory, and no alternative is supplied in the inventory. | https://ocfl.io/draft/spec/#content-directory
| E007 | Version directories starting with a leading zero are not all the same length. | https://ocfl.io/draft/spec/#version-directories
| E008 | Version directories do not use the same naming convention: non-padded or zero-padded. | https://ocfl.io/draft/spec/#version-directories
| E009 | Version directories do not start with '1' | https://ocfl.io/draft/spec/#version-directories
| E010 | Version directory $DIR contains directories other than designated `content` directory | https://ocfl.io/draft/spec/#version-directories
| E011 | Version directory $DIR contains files other than an inventory and inventory digest | https://ocfl.io/draft/spec/#version-directories
| E012 | Version directory $DIR does not contain the `content` directory specified in the inventory | https://ocfl.io/draft/spec/#version-directories
| E013 | Expected version directory $DIR missing from directory list $DIRS | https://ocfl.io/draft/spec/#version-directories
| E014 | Version directory $DIR does not match value supplied in the inventory. |/
| E015 | Content directory value changes across inventory files |/
| E016 | File $FILE in directory $DIR does not have an entry in the manifest for $INVENTORY |/
| E017 | Empty directory in version directory $DIR |/
| E018 | Digest algorithm is not one of the allowed values (sha512 or sha256) |/
| E019 | Fixity algorithm is not one of the allowed values (controlled or extension) |/
| E020 | Fixity algorithm not base16 encoded |/
| E021 | Missing inventory.json $File |/
| E022 | Missing inventory sidecar $FILE |/
| E023 | Inventory sidecar $FILE extension does not match the digest algorithm |/
| E024 | Malformed inventory sidecar $FILE | /
| E025 | Inventory sidecar digest does not match $INVENTORY |/
| E026 | Backslash used as path separator in $INVENTORY |/
| E027 | Missing version directory for $VERSION |/
| E028 | Missing entry in inventory for $VERSION directory |/
| E029 | Inventory $INVENTORY is not well-formed JSON |/
| E030 | Inventory $INVENTORY exists in highest $VERSION directory but does not match $INVENTORY in Object Root |/
| E031 | $FILE in manifest does not exist |
| E032 | Digest for $FILE does not match contents |
| E033 | Digest in $VERSION state does not exist in inventory manifest |/
| E034 | Missing 'id' for OCFL Inventory $FILE |/
| E035 | Missing 'manifest' for OCFL Inventory $FILE |/
| E036 | Missing 'versions' for OCFL Inventory $FILE |/
| E037 | Missing 'message' in $VERSION for OCFL Inventory $FILE (should) |/
| E038 | Missing 'client' in $VERSION for OCFL Inventory $FILE | awoods: where is this in the spec?
| E039 | Missing 'user' in $VERSION for OCFL Inventory $FILE (should) |/
| E040 | Missing 'created' in $VERSION for OCFL Inventory $FILE |/
| E041 | Missing 'digestAlgorithm' for OCFL Inventory $FILE |/
| E042 | Missing 'head' for OCFL Inventory $FILE |/
| E043 | Missing 'type' for OCFL Inventory $FILE |/
| E044 | 'id' in OCFL Inventory $FILE not unique |/
| E045 | 'type' in OCFL Inventory $FILE contains value other than 'https://ocfl.io/1.0/spec/#inventory' |/
| E046 | 'digestAlgorithm' in OCFL Inventory $FILE contains value other than sha512 and sha256 |/
| E047 | 'head' in OCFL Inventory $FILE contains value other than the highest version |/
| E048 | Content path in 'manifest' block OCFL Inventory $FILE not relative to the OCFL Object Root |/
| E049 | 'fixity' block OCFL Inventory $FILE exists, but not one of the allowed values (controlled or extension) |/
| E050 | 'fixity' block OCFL Inventory $FILE exists, but with invalid structure |/
| E051 | Content directory value contains a forward slash in $INVENTORY |
| E052 | Symbolic link used |/
| | Storage Roots |
| E100 | OCFL Object root contains noncompliant directories: $DIRECTORIES | https://ocfl.io/draft/spec/#object-structure
| E101 | OCFL Object root contains noncompliant files: $FILES | https://ocfl.io/draft/spec/#object-structure
| E102 | OCFL Object root does not contain required file: $FILE | https://ocfl.io/draft/spec/#object-structure
| E103 | Empty directory $DIR within OCFL Storage Root |/
| E104 | Directory $DIR is not an OCFL Object or intermediate directory |/
| E105 | Missing OCFL Storage Root Namaste File |/
| E106 | OCFL Storage Root Namaste File contains invalid content |/
| E107 | 'ocfl_layout.json' exists, but missing 'key' |/
| E108 | 'ocfl_layout.json' exists, but missing 'description' |/
| E109 | 'ocfl_layout.json' exists, but with value 'key' not found in "extensions" |/
| E110 | OCFL Object Root must contain only specified files/directories |/
| E911 | An unknown error has occurred. |/

## Warnings  (corresponding with SHOULD in specification)

| Code | Reason | Spec Reference
| --- | --- | --- |
| W005 | Missing inventory.json in $VERSION directory |/
| W006 | Missing inventory.json digest sidecar file in $VERSION directory |/
| W007 | Storage Root should have a copy of the OCFL Specification |/
| WXXX | Mixed-case digests in $INVENTORY |/
