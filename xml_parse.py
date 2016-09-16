test_snippet = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xml> <!-- not actually valid xml-->
<!-- This is a comment -->
<note date="8/31/12">
    <to>Tove</to>
    <from>Jani</from>
    <heading type="Reminder"/>
    <body>Don't forget me this weekend!</body>
    <!-- This is a multiline comment,
         which take a bit of care to parse -->
</note>
"""

test2 = '''            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand page-scroll" href="#page-top">15-388/688
                 Practical Data Science</a>
            </div>'''


test3 = '''    <header>
        <div class="container">
            <div class="intro-text">
                <div class="intro-lead-in">CMU 15-388/688, Fall 2016</div>
                <div class="intro-heading">Practical Data Science</div>

            </div>
        </div>
    </header>'''


class XMLNode:
    openJudgement = '<([a-zA-Z].*?)( .*?)??[\/]?>'
    closeJudgement = '<\/([a-zA-Z].*?)()>'
    openCloseJudgement = '<([a-zA-Z][^<]*?)( [^<]*?)??\/>'
    
    def __init__(self, tag, attributes, raw_content):
        self.tag = tag
        self.attributes = attributes
        self.children = []
        self.content = raw_content
        
        nextOpen = re.search(XMLNode.openJudgement, self.content)
        nextClose = re.search(XMLNode.closeJudgement, self.content)
        nextOpenClose = re.search(XMLNode.openCloseJudgement, self.content)
        tagStack = []
            
        while nextClose is not None:
            if nextOpen is not None:
                # Open close tag
                if nextOpenClose is not None and nextOpen.start() == nextOpenClose.start():
#                     self.children.append(XMLNode(nextOpenClose.group(1), {nextOpenClose.group(2)}, self.content[nextOpenClose.start():nextOpenClose.end()]))
                    self.content = self.content[nextOpenClose.end():]
#                     print 'branch A'
                # Open tag
                else:
                    if nextOpen.start() > nextClose.start():
                        tagStack = tagStack
#                         print 'branch B'
                    else:
                        # Add to stack 
                        tagStack.append(nextOpen.group(1))
#                         print 'branch C' 
    #                     print 'before2',tagStack        
                    print 'before open:',nextOpen.group(1),' close:',nextClose.group(1) 
                    stackTop = tagStack.pop()
#                     print 'top:', stackTop
                    if stackTop == nextClose.group(1):
                        tagStack = tagStack
                        self.content = self.content[nextClose.end():]
                    else:
                        tagStack.append(stackTop)
                        self.content = self.content[nextOpen.end():]
            # No more open tags
            else:
                stackTop = tagStack.pop()
                if stackTop == nextClose.group(1):
                    tagStack = tagStack
                    self.content = self.content[nextClose.end():]
#                     print 'branch D'
                else:
                    raise Exception("Error: tag inconsistant")
            print self.content[:500] 

            nextOpen = re.search(XMLNode.openJudgement, self.content)
            nextClose = re.search(XMLNode.closeJudgement, self.content)
            nextOpenClose = re.search(XMLNode.openCloseJudgement, self.content)
#             print nextClose.group(0)
#             print 'after open:',nextOpen.group(1),' close:',nextClose.group(1)
            print 'stack after',tagStack
            print '-' * 50
        
#         if nextOpen.start() < nextClose.start() and nextOpen.start() < nextOpenClose.start():
#             nextEnd = nextOpen.end()
#         if nextClose.start() < nextOpen.start() and nextClose.start() < nextOpenClose.start():
#             nextEnd = nextClose.end()
#         if nextOpenClose.start() < nextOpen.start() and nextOpenClose.start() < nextClose.start():
#             nextEnd = nextOpenClose.end()
            
#         tagContent = raw_content[nextOpen.start(): nextOpen.end()]
#         raw_content = raw_content[nextOpen.end():]
#         print tagContent
        
             

            
# root = XMLNode("",{},test3)
root = XMLNode("",{},test2)
# root = XMLNode("", {}, course_webpage)
# root = XMLNode("", {}, test_snippet)
# print root.tagStack.pop()
