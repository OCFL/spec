# Introduction

The OCFL initiative is an effort to define a shared approach to file hierarchy for long-term preservation.
It is targeted specifically at "memory institutions" -- libraries, archives, museums, and other cultural 
heritage organizations -- who are engaged with storing and preserving digital content for the long term.

This effort is an attempt to decouple the structure of the files-on-disk from the software
that might manage it by creating an expectation of file and folder hierarchy to which software applications
must conform -- effectively making the file and folder structure function as an Application Programming Interface (API).
 
The need for this can be expressed in three broad themes:

## 1. Software is inherently more unstable than the content it manages.
 
Software upgrades, or transitions between different platforms, often require
a complete shift from one file hierarchy to another to make them compatible. This poses significant risk as
files need to be moved around and placed in hierarchies that conform to the target
platform, placing them at risk of corruption through network transfers, or loss of context
from renaming.
 
## 2. Enumerate and address risk vectors for digital content storage.

OCFL attempts to address the need for 'rebuildability' -- that is, the ability to rebuild a digital
collection with only files on disk. This ability is rooted in several assumptions:
 
 1. File storage is, perhaps, the most well-understood, cross-compatible, and stable computing concept.
 There is a broad need to have files read across operating systems, and legacy compatibility is extremely
 robust.
 2. The number of software systems required to make sense of the content should be minimized. Contrast with
 content stored in relational databases or 'proprietary' folder hierarchies, which impose additional
 requirements above the ability to inspect and understand the content and its contexts.
  

While content considerations are fairly well understood (i.e., 
the risk of storing content in proprietary formats), how those files are written to disk, managed, and
secured are not. The OCFL initiative is an attempt at addressing a constrained set of risk
vectors, with a view towards enabling long-term digital preservation. 

## 3. There is no common approach to digital object versioning.

This specification takes a broad, but opinionated, definition of what constitutes a "digital object". 
It further defines a method for tracking the history and provenance of that digital object. There
are currently no commonly-held approaches to techniques for implementing this, leaving it to indidvidual
institutions to implement this in bespoke ways, or to disregard it altogether.



 