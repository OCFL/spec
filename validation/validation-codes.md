# OCFL Validation Codes

## Requirements

 - Levels of validation: ERROR, WARNING, INFO. The ERROR level corresponds with MUST in the specification, the WARNING level corresponds with SHOULD in the specification, and the INFO level is validator implementation specific.
 - OCFL Spec should define error codes to which validators MUST refer; these error codes will refer to sections in the OCFL Spec.
 - Validators MUST validate OCFL Objects
 - Validators MUST validate OCFL Storage Roots

## Object Errors (corresponding with MUST in specification)

| Code | Description | Reference
| --- | --- | --- |
| E001 | 'The OCFL Object Root must not contain files or directories other than those specified in the following sections.' | https://ocfl.io/draft/spec/#E001
| E002 | 'The version declaration must be formatted according to the NAMASTE specification.' | https://ocfl.io/draft/spec/#E002
| E003 | '[The version declaration] must be a file in the base directory of the OCFL Object Root giving the OCFL version in the filename.' | https://ocfl.io/draft/spec/#E003
| E004 | 'The [version declaration] filename MUST conform to the pattern T=dvalue, where T must be 0, and dvalue must be ocfl_object_, followed by the OCFL specification version number.' | https://ocfl.io/draft/spec/#E004
| E005 | 'The [version declaration] filename must conform to the pattern T=dvalue, where T MUST be 0, and dvalue must be ocfl_object_, followed by the OCFL specification version number.' | https://ocfl.io/draft/spec/#E005
| E006 | 'The [version declaration] filename must conform to the pattern T=dvalue, where T must be 0, and dvalue MUST be ocfl_object_, followed by the OCFL specification version number.' | https://ocfl.io/draft/spec/#E006
| E007 | 'The text contents of the [version declaration] file must be the same as dvalue, followed by a newline (\n).' | https://ocfl.io/draft/spec/#E007
| E008 | 'OCFL Object content must be stored as a sequence of one or more versions.' | https://ocfl.io/draft/spec/#E008
| E009 | 'The version number sequence MUST start at 1 and must be continuous without missing integers.' | https://ocfl.io/draft/spec/#E009
| E010 | 'The version number sequence must start at 1 and MUST be continuous without missing integers.' | https://ocfl.io/draft/spec/#E010
| E011 | 'If zero-padded version directory numbers are used then they must start with the prefix v and then a zero.' | https://ocfl.io/draft/spec/#E011
| E012 | 'All version directories of an object must use the same naming convention: either a non-padded version directory number, or a zero-padded version directory number of consistent length.' | https://ocfl.io/draft/spec/#E012
| E013 | 'Operations that add a new version to an object must follow the version directory naming convention established by earlier versions.' | https://ocfl.io/draft/spec/#E013
| E014 | 'In all cases, references to files inside version directories from inventory files must use the actual version directory names.' | https://ocfl.io/draft/spec/#E014
| E015 | 'There must be no other files as children of a version directory, other than an inventory file and a inventory digest.' | https://ocfl.io/draft/spec/#E015
| E016 | 'Version directories must contain a designated content sub-directory if the version contains files to be preserved, and should not contain this sub-directory otherwise.' | https://ocfl.io/draft/spec/#E016
| E017 | 'The contentDirectory value MUST NOT contain the forward slash (/) path separator and must not be either one or two periods (. or ..).' | https://ocfl.io/draft/spec/#E017
| E018 | 'The contentDirectory value must not contain the forward slash (/) path separator and MUST NOT be either one or two periods (. or ..).' | https://ocfl.io/draft/spec/#E018
| E019 | 'If the key contentDirectory is set, it MUST be set in the first version of the object and must not change between versions of the same object.' | https://ocfl.io/draft/spec/#E019
| E020 | 'If the key contentDirectory is set, it must be set in the first version of the object and MUST NOT change between versions of the same object.' | https://ocfl.io/draft/spec/#E020
| E021 | 'If the key contentDirectory is not present in the inventory file then the name of the designated content sub-directory must be content.' | https://ocfl.io/draft/spec/#E021
| E022 | 'OCFL-compliant tools (including any validators) must ignore all directories in the object version directory except for the designated content directory.' | https://ocfl.io/draft/spec/#E022
| E023 | 'Every file within a version\'s content directory must be referenced in the manifest section of the inventory.' | https://ocfl.io/draft/spec/#E023
| E024 | 'There must not be empty directories within a version\'s content directory.' | https://ocfl.io/draft/spec/#E024
| E025 | 'For content-addressing, OCFL Objects must use either sha512 or sha256, and should use sha512.' | https://ocfl.io/draft/spec/#E025
| E026 | 'For storage of additional fixity values, or to support legacy content migration, implementers must choose from the following controlled vocabulary of digest algorithms, or from a list of additional algorithms given in the [Digest-Algorithms-Extension].' | https://ocfl.io/draft/spec/#E026
| E027 | 'OCFL clients must support all fixity algorithms given in the table below, and may support additional algorithms from the extensions.' | https://ocfl.io/draft/spec/#E027
| E028 | 'Optional fixity algorithms that are not supported by a client must be ignored by that client.' | https://ocfl.io/draft/spec/#E028
| E029 | 'SHA-1 algorithm defined by [FIPS-180-4] and must be encoded using hex (base16) encoding [RFC4648].' | https://ocfl.io/draft/spec/#E029
| E030 | 'SHA-256 algorithm defined by [FIPS-180-4] and must be encoded using hex (base16) encoding [RFC4648].' | https://ocfl.io/draft/spec/#E030
| E031 | 'SHA-512 algorithm defined by [FIPS-180-4] and must be encoded using hex (base16) encoding [RFC4648].' | https://ocfl.io/draft/spec/#E031
| E032 | '[blake2b-512] must be encoded using hex (base16) encoding [RFC4648].' | https://ocfl.io/draft/spec/#E032
| E033 | 'An OCFL Object Inventory MUST follow the [JSON] structure described in this section and must be named inventory.json.' | https://ocfl.io/draft/spec/#E033
| E034 | 'An OCFL Object Inventory must follow the [JSON] structure described in this section and MUST be named inventory.json.' | https://ocfl.io/draft/spec/#E034
| E035 | 'The forward slash (/) path separator must be used in content paths in the manifest and fixity blocks within the inventory.' | https://ocfl.io/draft/spec/#E035
| E036 | 'An OCFL Object Inventory must include the following keys: [id, type, digestAlgorithm, head]' | https://ocfl.io/draft/spec/#E036
| E037 | '[id] must be unique in the local context, and should be a URI [RFC3986].' | https://ocfl.io/draft/spec/#E037
| E038 | '[type] must be the URI of the inventory section of the specification, https://ocfl.io/1.0/spec/#inventory.' | https://ocfl.io/draft/spec/#E038
| E039 | '[digestAlgorithm] must be the algorithm used in the manifest and state blocks.' | https://ocfl.io/draft/spec/#E039
| E040 |[head] must be the version directory name with the highest version number.' | https://ocfl.io/draft/spec/#E040
| E041 | 'In addition to these keys, there must be two other blocks present, manifest and versions, which are discussed in the next two sections.' | https://ocfl.io/draft/spec/#E041
| E042 | 'Content paths within a manifest block must be relative to the OCFL Object Root.' | https://ocfl.io/draft/spec/#E042
| E043 | 'An OCFL Object Inventory must include a block for storing versions.' | https://ocfl.io/draft/spec/#E043
| E044 | 'This block MUST have the key of versions within the inventory, and it must be a JSON object.' | https://ocfl.io/draft/spec/#E044
| E045 | 'This block must have the key of versions within the inventory, and it MUST be a JSON object.' | https://ocfl.io/draft/spec/#E045
| E046 | 'The keys of [the versions object] must correspond to the names of the version directories used.' | https://ocfl.io/draft/spec/#E046
| E047 | 'Each value [of the versions object] must be another JSON object that characterizes the version, as described in the 3.5.3.1 Version section.' | https://ocfl.io/draft/spec/#E047
| E048 | 'A JSON object to describe one OCFL Version, which must include the following keys: [created, state, message, user]' | https://ocfl.io/draft/spec/#E048
| E049 | '[the value of the "created" key] must be expressed in the Internet Date/Time Format defined by [RFC3339].' | https://ocfl.io/draft/spec/#E049
| E050 | 'The keys of [the "state" JSON object] are digest values, each of which must correspond to an entry in the manifest of the inventory.' | https://ocfl.io/draft/spec/#E050
| E051 | 'The logical path [value of a "state" digest key] must be interpreted as a set of one or more path elements joined by a / path separator.' | https://ocfl.io/draft/spec/#E051
| E052 | '[logical] Path elements must not be ., .., or empty (//).' | https://ocfl.io/draft/spec/#E052
| E053 | 'Additionally, a logical path must not begin or end with a forward slash (/).' | https://ocfl.io/draft/spec/#E053
| E054 | 'The value of the user key must contain a user name key, "name" and should contain an address key, "address".' | https://ocfl.io/draft/spec/#E054
| E055 | 'This block must have the key of fixity within the inventory.' | https://ocfl.io/draft/spec/#E055
| E056 | 'The fixity block must contain keys corresponding to the controlled vocabulary given in the digest algorithms listed in the Digests section, or in a table given in an Extension.' | https://ocfl.io/draft/spec/#E056
| E057 | 'The value of the fixity block for a particular digest algorithm must follow the structure of the manifest block; that is, a key corresponding to the digest value, and an array of content paths that match that digest.' | https://ocfl.io/draft/spec/#E057'
| E058 | 'Every occurrence of an inventory file must have an accompanying sidecar file stating its digest.' | https://ocfl.io/draft/spec/#E058
| E059 | 'This value must match the value given for the digestAlgorithm key in the inventory.' | https://ocfl.io/draft/spec/#E059
| E060 | 'The digest sidecar file must contain the digest of the inventory file.' | https://ocfl.io/draft/spec/#E060
| E061 | '[The digest sidecar file] must follow the format: DIGEST inventory.json' | https://ocfl.io/draft/spec/#E061
| E062 | 'The digest of the inventory must be computed only after all changes to the inventory have been made, and thus writing the digest sidecar file is the last step in the versioning process.' | https://ocfl.io/draft/spec/#E062
| E063 | 'Every OCFL Object must have an inventory file within the OCFL Object Root, corresponding to the state of the OCFL Object at the current version.' | https://ocfl.io/draft/spec/#E063
| E064 | 'Where an OCFL Object contains inventory.json in version directories, the inventory file in the OCFL Object Root must be the same as the file in the most recent version.' | https://ocfl.io/draft/spec/#E064
| E066 | 'Each version block in each prior inventory file must represent the same object state as the corresponding version block in the current inventory file.' | https://ocfl.io/draft/spec/#E066
| E067 | 'The extensions directory must not contain any files, and no sub-directories other than extension sub-directories.' | https://ocfl.io/draft/spec/#E067
| E068 | 'The specific structure and function of the extension, as well as a declaration of the registered extension name must be defined in one of the following locations: The OCFL Extensions repository OR The Storage Root, as a plain text document directly in the Storage Root.' | https://ocfl.io/draft/spec/#E068
| E069 | 'An OCFL Storage Root MUST contain a Root Conformance Declaration identifying it as such.' | https://ocfl.io/draft/spec/#E069
| E070 | 'If present, [the ocfl_layout.json document] MUST include include the following two keys in the root JSON object: [key, description]' | https://ocfl.io/draft/spec/#E070
| E071 | 'The value of [the ocfl_layout.json key "key"] is not defined in the OCFL specification, but MUST correspond to a value given in an Extension.' | https://ocfl.io/draft/spec/#E071
| E072 | 'Sub-directories within an OCFL Storage Root MUST NOT contain files that are not part of an OCFL Object.' | https://ocfl.io/draft/spec/#E072
| E073 | 'Empty directories MUST NOT appear within a storage root.' | https://ocfl.io/draft/spec/#E073
| E074 | 'Although implementations may require multiple OCFL Storage Roots - that is, several logical or physical volumes, or multiple "buckets" in an object store - each OCFL Storage Root MUST be independent.' | https://ocfl.io/draft/spec/#E074
| E075 | 'The OCFL version declaration <span id="E075">MUST</span> be formatted according to the NAMASTE specification.' | https://ocfl.io/draft/spec/#E075
| E076 | '[The OCFL version declaration] MUST be a file in the base directory of the OCFL Storage Root giving the OCFL version in the filename.' | https://ocfl.io/draft/spec/#E076
| E077 | '[The OCFL version declaration filename] MUST conform to the pattern T=dvalue, where T must be 0, and dvalue must be ocfl_, followed by the OCFL specification version number.' | https://ocfl.io/draft/spec/#E077
| E078 | '[The OCFL version declaration filename] must conform to the pattern T=dvalue, where T MUST be 0, and dvalue must be ocfl_, followed by the OCFL specification version number.' | https://ocfl.io/draft/spec/#E078
| E079 | '[The OCFL version declaration filename] must conform to the pattern T=dvalue, where T must be 0, and dvalue MUST be ocfl_, followed by the OCFL specification version number.' | https://ocfl.io/draft/spec/#E079
| E080 | 'The text contents of [the OCFL version declaration file] MUST be the same as dvalue, followed by a newline (\n).' | https://ocfl.io/draft/spec/#E080
| E081 | 'OCFL Objects within the OCFL Storage Root also include a conformance declaration which MUST indicate OCFL Object conformance to the same or earlier version of the specification.' | https://ocfl.io/draft/spec/#E081
| E082 | 'OCFL Object Roots MUST be stored either as the terminal resource at the end of a directory storage hierarchy or as direct children of a containing OCFL Storage Root.' | https://ocfl.io/draft/spec/#E082
| E083 | 'There MUST be a deterministic mapping from an object identifier to a unique storage path.' | https://ocfl.io/draft/spec/#E083
| E084 | 'Storage hierarchies MUST NOT include files within intermediate directories.' | https://ocfl.io/draft/spec/#E084
| E085 | 'Storage hierarchies MUST be terminated by OCFL Object Roots.' | https://ocfl.io/draft/spec/#E085
| E086 | 'The storage root extensions directory MUST conform to the same guidelines and limitations as those defined for object extensions.' | https://ocfl.io/draft/spec/#E086
| E087 | 'An OCFL validator MUST ignore any files in the storage root it does not understand.' | https://ocfl.io/draft/spec/#E087
| E088 | 'Additional files MUST NOT appear in other directories under the storage root.' | https://ocfl.io/draft/spec/#E088
| E089 | 'If the preservation of non-OCFL-compliant features is required then the content MUST be wrapped in a suitable disk or filesystem image format which OCFL can treat as a regular file.' | https://ocfl.io/draft/spec/#E089
| E090 | 'Hard and soft (symbolic) links are not portable and <span id="E090">MUST NOT</span> be used within OCFL Storage hierachies.' | https://ocfl.io/draft/spec/#E090
| E091 | 'Filesystems MUST preserve the case of OCFL filepaths and filenames.' | https://ocfl.io/draft/spec/#E091
| E092 | 'The value for each key in the manifest must be an array containing the content paths of files in the OCFL Object that have content with the given digest.' | https://ocfl.io/draft/spec/#E092
| E093 | 'Where included in the fixity block, the digest values given must match the digests of the files at the corresponding content paths.' | https://ocfl.io/draft/spec/#E093
| E094 | 'The value of [the message] key is freeform text, used to record the rationale for creating this version. It must be a JSON string.' | https://ocfl.io/draft/spec/#E094
| E095 | 'Within a version, logical paths must be unique and non-conflicting, so the logical path for a file cannot appear as the initial part of another logical path.' | https://ocfl.io/draft/spec/#E095
| E096 | 'As JSON keys are case sensitive, while digests may not be, there is an additional requirement that each digest value must occur only once in the manifest regardless of case.' | https://ocfl.io/draft/spec/#E096
| E097 | 'As JSON keys are case sensitive, while digests may not be, there is an additional requirement that each digest value must occur only once in the fixity block for any digest algorithm, regardless of case.' | https://ocfl.io/draft/spec/#E097

## Warnings (corresponding with SHOULD in specification)

| Code | Reason | Spec Reference |
| --- | --- | --- |
| W001 | 'Implementations SHOULD use version directory names constructed without zero-padding the version number, ie. v1, v2, v3, etc.'' | https://ocfl.io/draft/spec/#W001
| W002 | 'The version directory SHOULD NOT contain any directories other than the designated content sub-directory. Once created, the contents of a version directory are expected to be immutable.' | https://ocfl.io/draft/spec/#W002
| W003 | 'Version directories must contain a designated content sub-directory if the version contains files to be preserved, and SHOULD NOT contain this sub-directory otherwise.'| https://ocfl.io/draft/spec/#W003
| W004 | 'For content-addressing, OCFL Objects SHOULD use sha512.' | https://ocfl.io/draft/spec/#W004
| W005 | 'The OCFL Object Inventory id SHOULD be a URI.' | https://ocfl.io/draft/spec/#W005
| W007 | 'In the OCFL Object Inventory, the JSON object describing an OCFL Version, SHOULD include the message and user keys.' | https://ocfl.io/draft/spec/#W007
| W008 | 'In the OCFL Object Inventory, in the version block, the value of the user key SHOULD contain an address key, address.' | https://ocfl.io/draft/spec/#W008
| W009 | 'In the OCFL Object Inventory, in the version block, the address value SHOULD be a URI: either a mailto URI [RFC6068] with the e-mail address of the user or a URL to a personal identifier, e.g., an ORCID iD.' | https://ocfl.io/draft/spec/#W009
| W010 | 'In addition to the inventory in the OCFL Object Root, every version directory SHOULD include an inventory file that is an Inventory of all content for versions up to and including that particular version.' | https://ocfl.io/draft/spec/#W010
| W011 | 'In the case that prior version directories include an inventory file, the values of the created, message and user keys in each version block in each prior inventory file SHOULD have the same values as the corresponding keys in the corresponding version block in the current inventory file.' | https://ocfl.io/draft/spec/#W011
| W012 | 'Implementers SHOULD use the logs directory, if present, for storing files that contain a record of actions taken on the object.' | https://ocfl.io/draft/spec/#W012
| W013 | 'In an OCFL Object, extension sub-directories SHOULD be named according to a registered extension name.' | https://ocfl.io/draft/spec/#W013
| W014 | 'Storage hierarchies within the same OCFL Storage Root SHOULD use just one layout pattern.' | https://ocfl.io/draft/spec/#W014
| W015 | 'Storage hierarchies within the same OCFL Storage Root SHOULD consistently use either a directory hierarchy of OCFL Objects or top-level OCFL Objects.' | https://ocfl.io/draft/spec/#W015
