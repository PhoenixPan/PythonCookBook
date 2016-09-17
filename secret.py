class XMLNode:
    openJudgement = '<([a-zA-Z].*?)( .*?)??[\/]?>'
    closeJudgement = '<\/([a-zA-Z].*?)()>'
    openCloseJudgement = '<([a-zA-Z][^<]*?)( [^<]*?)??\/>'
    attrJudgement = '([a-zA-z].*?)="(.*?)"'
    
    #root = XMLNode("", {}, test_snippet)
    def __init__(self, tag, attributes, raw_content):
        self.tag = tag
        self.attributes = attributes
        self.children = []
        self.content = raw_content
        
        nextOpen = re.search(XMLNode.openJudgement, self.content)
        nextClose = re.search(XMLNode.closeJudgement, self.content)
        nextOpenClose = re.search(XMLNode.openCloseJudgement, self.content)
        tagStack = []
        
        ##### should be while loop
        while nextOpen is not None:
            # Child tag
            childTag = nextOpen.group(1)
            
            # Child attributes
            childAttr = {}
            attrContent = nextOpen.group(0)
            attr = re.search(XMLNode.attrJudgement, attrContent)
            while attr is not None:
                childAttr[attr.group(1)] = attr.group(2)
                attrContent = attrContent[attr.end():]
                attr = re.search(XMLNode.attrJudgement, attrContent)
            
            # Child content
            contentStart = nextOpen.start()
            contentEnd = nextOpen.end()
            tagStack.append(childTag)
            first = True
            tagContent = self.content[contentEnd:]
            
            nextOpen = re.search(XMLNode.openJudgement, tagContent)
            nextClose = re.search(XMLNode.closeJudgement, tagContent)
            nextOpenClose = re.search(XMLNode.openCloseJudgement, tagContent)
            
###############################################################################################################           
            # One loop = one child content located
            while tagStack:
                if nextOpen is not None:
                    if nextOpenClose is not None and nextOpen.start() == nextOpenClose.start():
                        if first:
                            first = False   
#                         print 'Branch A:'
#                         print 'Nothing changed'
                        tagContent = tagContent[nextOpenClose.end():]
                        contentEnd += nextOpenClose.end()
                        nextOpen = re.search(XMLNode.openJudgement, tagContent)
                        nextClose = re.search(XMLNode.closeJudgement, tagContent)
                        nextOpenClose = re.search(XMLNode.openCloseJudgement, tagContent)
                        continue
                    else:                    
                        nextNextOpen = re.search(XMLNode.openJudgement, tagContent[nextOpen.end():])
                        if nextOpen.start() > nextClose.start():
                            if tagStack[-1] == nextClose.group(1):
#                                 print 'Branch B:'
                                tagStack.pop()
                                tagContent = tagContent[nextClose.end():]
#                                 print 'Content:',tagContent
                                contentEnd += nextClose.end()
                                nextOpen = re.search(XMLNode.openJudgement, tagContent)
                                nextClose = re.search(XMLNode.closeJudgement, tagContent)
                                nextOpenClose = re.search(XMLNode.openCloseJudgement, tagContent)
                                first = False
                                continue
                            else:
                                raise Exception("Error: tag inconsistant")
                        elif nextNextOpen is not None and nextNextOpen.start() < nextClose.start():
                            tagStack.append(nextOpen.group(1))
#                             print '-' * 50
#                             print 'Branch C:'
#                             print 'Before content:',tagContent
#                             print 'Add tag:',nextOpen.group(1)," Current stack:", tagStack
                            tagContent = tagContent[nextOpen.end():]
#                             print 'After content:',tagContent
                            contentEnd += nextOpen.end()
                            nextOpen = re.search(XMLNode.openJudgement, tagContent)
                            nextClose = re.search(XMLNode.closeJudgement, tagContent)
                            nextOpenClose = re.search(XMLNode.openCloseJudgement, tagContent)
                            first = False
                            continue
                        elif nextOpen.group(1) ==  nextClose.group(1):
#                             print '-' * 50
#                             print 'Branch D:'
#                             print 'Nothing changed, current stack:',tagStack
                            tagContent = tagContent[nextClose.end():]
#                             print 'Content:',tagContent
#                             print 'Content:',tagContent
                            contentEnd += nextClose.end()
                            nextOpen = re.search(XMLNode.openJudgement, tagContent)
                            nextClose = re.search(XMLNode.closeJudgement, tagContent)
                            nextOpenClose = re.search(XMLNode.openCloseJudgement, tagContent)
                            continue
                    
                        elif tagStack[-1] == nextClose.group(1):
#                             print '-' * 50
#                             print 'Branch E:'
                            tagStack.pop()
                            tagContent = tagContent[nextClose.end():]
#                             print 'Content:',tagContent
                            contentEnd += nextClose.end()
                            nextOpen = re.search(XMLNode.openJudgement, tagContent)
                            nextClose = re.search(XMLNode.closeJudgement, tagContent)
                            nextOpenClose = re.search(XMLNode.openCloseJudgement, tagContent)
                            first = False
                            continue
                        else:
                            print 'should not happen'
                                
                elif nextOpen is None:
#                     print '-' * 50
#                     print 'Branch F:'
#                     print 'Before stack:', tagStack
#                     print 'Next close:',nextClose.group(1)
#                     print 'Pop tag:',tagStack[-1]
                    if tagStack[-1] == nextClose.group(1):
                        tagStack.pop()
#                         print 'After stack:', tagStack
                        tagContent = tagContent[nextClose.end():]
#                         print 'Content:',tagContent
                        contentEnd += nextClose.end()
                        nextOpen = re.search(XMLNode.openJudgement, tagContent)
                        nextClose = re.search(XMLNode.closeJudgement, tagContent)
                        nextOpenClose = re.search(XMLNode.openCloseJudgement, tagContent)
                        first = False
                        continue
                    else:
                        raise Exception("Error: tag inconsistant")
#########################################################################################################################            
            # child while ends here
            print 'why'
            self.children.append(childTag, childAttr, self.content[contentStart: contentEnd]
            self.content = self.content[contentEnd:]                          
#         print "result:",self.content[contentStart: contentEnd]
               

# root = XMLNode("",{},test2)         
# root = XMLNode("",{},test3)
# root = XMLNode("",{},testattr)
root = XMLNode("", {}, course_webpage)
# root = XMLNode("", {}, test_snippet)
