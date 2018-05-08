# 1. Introduction

## 1.1 Purpose

The Oxford Common File Layout (OCFL) is a file-and-folder hierarchy designed to promote long-term, application-independent file management best practices within digital repositories.

This specification covers two principle areas:

1. Structure. A normative specification of the nature of an OCFL Object (the "object-at-rest");
2. Client Behaviours. A set of recommendations for how OCFL Objects should be acted upon (the "object-in-motion")

## 1.2 Need

The OCFL initiative arose from a need to have well-defined application-independent file management within digital repositories. 

A general observation is that the contents of a digital repository -- that is, the digital files and metadata that an institution might wish to manage -- are largely stable. Once content has been accessioned, it is unlikely to change significantly over its lifetime. This is in contrast to the software applications that manage these contents, which are ephemeral, requiring constant updating and replacement. Thus, transitions between application-specific methods of file management to support software upgrades and replacement cycles can be seen as unnecessary and risky change, changing the long-term stable objects to support the short-term, ephemeral software.

By providing a specification for the file-and-folder layout on disk, the OCFL is an attempt at reducing, or even eliminating, the need for these transitions. As an application-independent specification, conforming applications will natively 'understand' the underlying file structure without needing to first transition these contents to their own format.

## 1.3 Scope

## 1.4 Terminology

Consult the glossary for further definitions.

<dl>
    <dt>base directory</dt>
    <dd>The root directory of an OCFL Object.</dd>
</dl>

# 2. Structure

## 2.1 The OCFL Object

An OCFL Object is a base directory that contains a set of required and optional files and folders.

## 2.2 Basic Structure

!CAPTION A basic OCFL Object Structure
```
<base-directory>
├── 0=ocfl_object_1.0
├── inventory.jsonld
├── logs
│   └── .keep
└── v1
    └── .keep
```

## 2.3 Specifications Conformance

The OCFL specification will change over time, and these changes will be published as versioned updates. OCFL Objects are self-describing, and provide an indication of the version of the specification to which they should conform.

### 2.3.1 OCFL Version declaration

The version declaration MUST be an empty file in the base directory of the object giving the OCFL object version in the filename. This MUST be formatted with a leading zero-equals (0=), 'ocfl_object', and the version number. A regular expression intended to validate this name is provided below.

!CAPTION Example filename as version declaration
```
0=ocfl_object_1.0
```

!CAPTION OCFL Version File Regex for validation
```
^0=ocfl_object_[\d]+.[\d]+$
```

## 2.X Object Identity

An OCFL Object MUST have a unique ID. The scope of this "uniqueness" can be either global, or local The OCFL Object MUST also "wear" this identifier by using it as the name of the base directory of the object.

When choosing an object identity scheme, consideration should be given to the likelihood of identifier collision in the near, or distant, future. Some identifier schemes, such as accession numbering (object-1, object-2, etc.) have a very high probability of identifier collision, while others, such as UUIDs, have an extremely low probability.

### 2.X.X Special Characters in Identifiers

Some identifier schemes (e.g., ARKs and DOIs) have characters in them that are reserved as special characters on some filesystems. This includes colons (":") and both forward ("/") and back ("\") slashes.

OCFL Objects MUST NOT contain these reserved characters in their base directory name, but MAY contain them in their "@id" property in the `inventory.jsonld` file.

## 2.X Object Versioning

OCFL Objects are versioned. They provide object versioning through a combination of version directories and an `inventory.jsonld` file, which describes the contents of each version.

OCFL Objects are 'forward-delta' versioned [REF]. The original structure of the object is contained in the first version. Later versions of the object will store only the content that is changed from the previous versions. Reconstructing the latest version of the object means constructing the current contents of the object through all previous versions.

The `inventory.jsonld` tracks all known files in the OCFL Object, along with a SHA512 digest of that object's contents. Version information is tracked in the `inventory.jsonld` file in a list of digests for the files that are part of a given version. 

Getting a list of the files from that object for a particular version is done with the following steps:

1. Read the `inventory.jsonld` file for the list of SHA512 digests for a given version;
2. Find those digests listed in the `manifest` section. This will provide a list of filepaths within the OCFL object.
3. Deliver the object as a list of those filepaths.

The most recent version of an object may be referred to as the 'HEAD', following the conventions of version control software.

### X.X.X Version Immutability

An OCFL Object Version is immutable. This immutability means that once content has been accessioned and inventoried, content in the version folders MUST NOT change, except in exceptional circumstances.

The one exception to this is the addition of the `inventory.jsonld` file to a version folder when a new version is created. See section X.X.X.X for further information about this.

#### X.X.X.X Exceptional Circumstances

In some exceptional circumstances, digital content may need to be deaccessioned from an OCFL object. This should be considered an act of destruction, and should not be part of day-to-day operations. Cases where this may be permissible include exposure of sensitive personal information (e.g., medical records), or hosting contents for which the institution has no rights (e.g., copyright infringement).

The forward-versioning scheme used in OCFL makes file deletion difficult, as the most recent version of the object depends on all previous versions. Permanently removing files from previous versions may cause problems in ensuring the object's integrity.

In the case where only some files within the object are being deaccessioned, a full version history rewrite should be performed. This might consist of:

1. Identify all files in the current version of the OCFL Object, copying them to a temporary space.
2. Delete all versions from the OCFL Object, and reset the object to version 1.
3. Copy only the non-offending files back to the version 1 folder.
4. Proceed as if the object were newly accessioned (e.g., populate inventory files with SHA512 digests, etc.)

Depending on when in the object's history the offending content was accessioned, it may also be possible to 'roll back' an object's history to the version prior, and reconstruct the object from there. Implementers should be aware that this would still mean losing the object's history past that point.

It is NOT permissible for an OCFL Client to provide support for 'excising' files from an object, as this may have unintended consequences. For example, excising a file from a version folder containing only that file would lead to an empty version folder, which is not permitted.

### X.X.X Version Folders

#### X.X.X.X Version Folder Naming

Version folders MUST be numbered with whole numbers, and MUST start with the 'v' prefix. There are no leading zeros on a version folder. Implementers should be aware that this may cause problems with alphanumeric sorting of folders in some systems. (The alternative is to zero-pad the version numbers, but this artificially limits the number of versions that could be tracked.)

#### X.X.X.X Version Folder Contents

The contents of version folders is opaque to the OCFL specifications, and there is no defined file or folder hierachy within a version folder. Implementers are free to use local conventions, or this may form part of a complementary specification.

The only exception to this is that a copy of the `inventory.jsonld` file MUST be placed in the root of a version folder as a record of the state of the object at that version. This only applies when that folder no longer represents the most recent version of the object.

#### X.X.X.X Empty Version Folders

Empty version folders are not permitted. This implies, also, that an OCFL Object is non-conformant to the specification if it does not at least have one version.

### 2.4.2 Inventory

#### X.X.X.X inventory.jsonld

An OCFL Object MUST have a file called `inventory.jsonld` in the base directory.

#### X.X.X.X Use of JSON-LD

The `inventory.jsonld` file should conform to the [JSON-LD 1.1 specification](https://json-ld.org/spec/latest/json-ld/). JSON-LD was chosen as it is both easily processable by non-LD-aware clients, while providing a self-describing context for OCFL inventories.

#### X.X.X.X SHA512 Digests

All digests in OCFL objects MUST be SHA512. Truncated forms are NOT acceptable.

#### X.X.X.X Inventory File Versioning

Inventory files in the root of the OCFL Object MUST represent the most recent state of the object. Copies of the previous state of the inventory file MUST be kept in the root of the folder of that previous version.

An OCFL Object at version 2 has a new file added, thus bringing it to version 3. A copy of the `inventory.jsonld` file is created in the root of the `v2` folder. A modified version of the `inventory.jsonld` is created, and contains a SHA512 digest of both the new file being added, and of the previous inventory now stored in the `v2` folder.

#### X.X.X.X Structure of the Inventory File

The `inventory.jsonld` has the following structure.

1. It MUST contain a '@context' key, and the value of this MUST be "https://ocfl.org/v1.0/"
2. It MUST contain a 'type' key, and the value of this MUST be 'ocfl:Object'.
3. It MUST contain an 'id' key, and the value of this MUST be a URI. 
    3a. This URI MAY be a URN, e.g., `urn:uuid:...`
4. It MUST contain a 'manifest' key, which MUST be a JSON Object.
5. It MUST contain a 'versions' key, which MUST be an Array.

Within the `versions` array are Version objects. These have the following structure:

1. It MUST contain a 'type' key, and the value of this MUST be 'ocfl:Version'.
2. It MUST contain a 'created' key containing the date in ISO 8601 "Combined Date and Time" format
3. It MUST contain a 'members' key, which MUST be an Array.
4. It MUST contain an 'id' key uniquely identifying this version within this object. By convention this MAY be the string corresponding to the folder name for this version, e.g., 'v1', 'v2', etc.
5. It MAY contain a 'message' key, to store a short description of this version.
6. It MAY contain a 'client' key, where a record may be kept of a software library that created this version.
7. It MAY contain a 'user' key, which MUST be a JSON Object containing a person's name and e-mail address as a record of responsibility.

## 2.X Action Logging

OCFL Objects support digital content monitoring by providing a location in which logging information about this object may be stored. This logging information is stored in the `logs` directory in the base directory of the OCFL Object.

### 2.X.X Structure of Logs Directory

There is no defined structure for the logging directory.

### 2.X.X Logged Events

The OCFL specification has no opinion on what might be considered a 'loggable' event. Some implementers may wish to maintain logs only when an object has changed, while others may wish to note every time an object was checked, regardless of if it changed.

### 2.X.X Log Format

No particular log file format is specified. Implementers may wish to consider complementary specifications like PREMIS or PROV-O for capturing loggable events.

### 2.X.X Logs and Versions

Additions to the logs directory are NOT versionable events. A version of the object MUST NOT be created if the only action is to add a record to the logs directory.

# 3. Client Behaviours
