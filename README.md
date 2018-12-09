# pycatia

pycatia currently only contains access to the CATIA API Measurable 
object and it's methods without the need of visual basic / CATScripts. 

Some of the methods can be accessed simply using the pywin32 module but further 
access to methods such as GetCOG do not seem to be accessible using pure python.
There are several questions on stack overflow and the pywin32 mailing list regarding
this. But, they fail to provide any working examples with the VB Measurable object 
in python. 

pycatia accesses these methods by running VBA scripts using the 
`Dispatch('CATIA.Application').SystemService.Evaluate()` function where required
 and passing a small public function to it. Otherwise, pycatia uses the VB method 
directly but exposes it within the same python class.

This has currently only been tested in CATIA V5 R21.

## Requirements

* python >= 3.6 
* CATIA V5/V6
* see requirements.txt

## Installation

## Using pip

### Using git
Clone the master branch from github into your working folder.

    git clone https://github.com/evereux/pycatia.git

### Download Zip
Download and unpack the  [master branch zip](https://github.com/evereux/pycatia/archive/master.zip) into your working folder.


## Example Usage

1. Open the file catia_measurable.CATPart from the folder tests.
2. Run the example scripts.

    [Example 1](https://github.com/evereux/pycatia/blob/master/example_1.py):

    Shows how to access the CATIA COM object with a .CATPart open and get the center
    of gravity for the part body 'PartBody'.
    
    [Example 2](https://github.com/evereux/pycatia/blob/master/example_2.py):

    Shows how to get all the points in the geometrical set 'Points' and get the co-ordinate.
    
    [Example 3](https://github.com/evereux/pycatia/blob/master/example_3.py):
    
    Shows how to search for all points in the document and return the co-ordinates.
    
## Running The Tests
* CATIA must be running the the part catia_measurable_part.CATPart open.
* You will
* Run the command: `py.test -v --cov-report term-missing --cov=pycatia tests/`
