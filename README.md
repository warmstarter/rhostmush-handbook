RhostMUSH Handbook

requirements.txt can be used to build your own python environment if you want to try this out yourself.

source/

This directory includes the documentation and is sourced exclusively from the RhostMUSH git repository and wiki. At present, it should contain all documentation that can found there. The difference, besides some light formatting for RestructuredText is that similar topics have been grouped together in single files. One of the major reasons for this project is the confusion I had from things like README.1st vs README.FIRST. It is the hope that this will allow for the removal of redundant documentation and making everything easier to find. At present, this is not at a stage of re-writing or true beautification, but rather basic organization and de-duplication. Once that latter tasks are completed, the former will commence.


build/

There are a variety of different text formats that are all compiled from the same source. Currently, this is is only at the stage where I am truly paying attention to the 'html' output, so in a lot of cases I have no idea what state some of the other formats are in. Spot checking a few, though, they seem to be shaping up pretty well and it doesn't seem like long before this project will be producing nice documentation in multiple formats.


To get an idea of what this is about, the best bet is to clone this repo and then point a webserver at the build/html directory. Python includes a testing webserver that can be invoked on a directory in a one liner. 

From the build/html directory (or any other build/ directory)
# If Python version returned above is 3.X
python3 -m http.server
# On windows try "python" instead of "python3", or "py -3"
# If Python version returned above is 2.X
python -m SimpleHTTPServer

then connect your webbrowser to http://localhost:8000

Otherwise, while it looks incredibly different, you can get an understanding of this by simply looking at the pdf document in build/latex



If you're interested in helping, please contact me on the RhostMUSH Discord.

Any feedback on this project is appreciated. In addition to that there are ways to help related to documentation or technical tasks, and I would love for this to become much more of a community effort.
