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
                    # Do not add to stack, make it a child
#                     self.children.append(XMLNode(nextOpenClose.group(1), {nextOpenClose.group(2)}, self.content[nextOpenClose.start():nextOpenClose.end()]))
                    tagStack = tagStack
                    self.content = self.content[nextOpenClose.end():]
                    print 'branch A'
                # Open tag
                else:
                    if nextOpen.start() > nextClose.start():
                        tagStack = tagStack
                        print 'branch B'
                    else:
                        # Add to stack 
                        tagStack.append(nextOpen.group(1))
                        print 'branch C' 
    #                     print 'before2',tagStack        
                    print 'before open:',nextOpen.group(1),' close:',nextClose.group(1) 
                    stackTop = tagStack.pop()
                    print 'top:', stackTop
                    if stackTop == nextClose.group(1):
                        tagStack = tagStack
                        self.content = self.content[nextClose.end():]
                    else:
                        tagStack.append(stackTop)
                        self.content = self.content[nextOpen.end():]
            else:
                stackTop = tagStack.pop()
                if stackTop == nextClose.group(1):
                    tagStack = tagStack
                    self.content = self.content[nextClose.end():]
                    print 'branch D'
                else:
                    raise Exception("Error: tag inconsistant")
#                     tagStack.append(stackTop)
            print self.content[:500] 
            nextOpen = re.search(XMLNode.openJudgement, self.content)
            nextClose = re.search(XMLNode.closeJudgement, self.content)
            nextOpenClose = re.search(XMLNode.openCloseJudgement, self.content)
#             print nextClose.group(0)
            print 'after open:',nextOpen.group(1),' close:',nextClose.group(1)
            print 'stack after',tagStack
            print '-' * 50
