#BELOW 2 CLASSES WILL ALREADY BE DECLARED IN NISHANTH'S CODE
class ListNode:
    def __init__(self):
        self.value = 0
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListNode()


#THIS IS JENKINS ONE AT A TIME HASH FUNCTION
def calculateKey(hashstr):
    hash = 0
    for i in range(len(hashstr)):
        hash += ord(hashstr[i])
        hash += (hash << 10)
        hash ^= (hash >> 6)
    hash += (hash << 3)
    hash ^= (hash >> 11)
    hash += (hash << 15)
    return hash

def compressKey(key):
    return key % 1007

hashTable = [None] * 1007

#TEST DATA, WILL BE REPLACED WITH URL'S LATER
lis = ['' for i in range(1000)]
lis[0] = "http://www.edhelper.com"
lis[1] = "http://www.schoolexpress.com/"
lis[2] = "http://www.learningpage.com"
lis[3] = "http://www.toolsforeducators.com"
lis[4] = "http://www.britannica.com"
lis[5] = "http://school.discovery.com"
lis[6] = "http://www.geocities.com/homeschooldesk/"
lis[7] = "http://www.ipl.org"
lis[8] = "http://www.nytimes.com/learning"
lis[9] = "www.EnchantedLearning.com"
lis[10] = "http://www.autismtoday.com"
lis[11] = "http://www.ideallives.com"
lis[12] = "http://www.studystack.com"
lis[13] = "http://www.studyspanish.com"
lis[14] = "http://www.howstuffworks.com/"
lis[15] = "http://www.songsforteaching.com/"
lis[16] = "http://www.educationcreations.com/freestuff.htm"
lis[17] = "http://www.lessonplancentral.com/"
lis[18] = "http://www.timesaversforteachers.com/"
lis[19] = "http://www.kids.gov/"
lis[20] = "http://www.time4learning.com"
lis[21] = "http://www.TheMathWorksheetSite.com"
lis[22] = "http://www.mathgoodies.com"
lis[23] = "http://www.mathplayground.com"
lis[24] = "http://www.math-drills.com/"
lis[25] = "http://www.math.com/"
lis[26] = "http://www.algebrahelp.com"
lis[27] = "http://www.webmath.com"
lis[28] = "http://www.coolmath-games.com"
lis[29] = "http://highschoolace.com/ace/ace.cfm"
lis[30] = "http://www.homeworkspot.com"
lis[31] = "http://www.explorelearning.com/index.cfm"
lis[32] = "http://colleges.usnews.rankingsandreviews.com/college"
lis[33] = "http://www.ed.gov/pubs/Prepare/index.html"
lis[34] = "http://www.brainpop.com"
lis[35] = "http://www.chem4kids.com"


for i in range(len(lis)):
    value = compressKey(calculateKey(lis[i]))
    if hashTable[value] is None: #NO ELSE FOR THIS IF, CONSIDERING NO COLLISIONS
        hashTable[value] = LinkedList()
        temp = ListNode()
        temp.value = value
        temp.next = None
        hashTable[value].head.next = temp


print (hashTable)