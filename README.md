# catia_python

catia_python currently only contains access to the CATIA API Measurable 
object and it's methods without resorting to using visual basic / CATScripts. 

Some of the methods can be accessed simply using the pywin32 module but further 
access to methods such as GetCOG do not seem to be accessible using pure python.
There are several questions on stack overflow and the pywin32 mainling list regarding
this. But, they fail to provide any working examples with the VB Measurable object. 

catia_python accesses these methods by running VBA scripts using the 
`Dispatch('CATIA.Application').SystemService.Evaluate()` function where required and 
passing a small public function to it. Otherwise, catia_python uses the VB method 
directly but exposes it within the same python class.

This has only been tested in CATIA V5 R21.

## Requirements

* python >= 3.6 
* See requirements.txt
* CATIA V5/V6

## Example Usage
1. Open the file catia_measurable.CATPart

        from catia_python import Application
        from catia_python import Document
        from catia_python import create_reference, create_measurable
        from catia_python import CATIAMeasurable
        from catia_python import Part
        from catia_python import create_spa_workbench
        
        catia = Application()
        document = Document(catia.catia).document
        # document.name = caita_measurable_part.CATPart
        spa_workbench = create_spa_workbench(document)
        
        part = Part(document)
        # part.name = caita_measurable_part
        
        bodies = part.get_bodies()
        body_names = part.get_bodies_names()
        # body_names = ['PartBody', 'EmptyPartBody']
        
        # gets first body in bodies list.
        body = bodies[0]
        
        # or get the body by name
        body_by_name = part.get_body_by_name('PartBody')
        
        # equivalent to VB CreateReferenceFromObject()
        # part.part is the VB Part object.
        reference = create_reference(part.part, body)
        
        # equivalent to VB GetMeasurable() 
        measurable = create_measurable(spa_workbench, reference)
        
        # the measurable object
        catia_measurable = CATIAMeasurable(measurable)
        
        # run the VB function Measurable.GetCOG()
        center_of_gravity = catia_measurable.get_cog()
        # center_of_gravity = (86.06520158074527, 81.36458658122612, 10.0)
