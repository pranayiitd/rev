rev
===

Basic parser to convert rev document to data model and Serializer to convert to XML

Assumption
==========
 + chronological for monologue not given in Problem, hence input order is
   assumed
 + Speaker name, text etc. can contain extra white spaces and hence not ignored.
 + Have put new line after xml for each monologue, just to pretty display.
 + Events tags are always sperated by space.
 + 

Instruction
==========
 + Running from inside src folder
   <code>
   $ python run.py ../test/document.txt output.xml
  </code>

  document.txt : path of the input rev text
  output.xml : path of the output xml

