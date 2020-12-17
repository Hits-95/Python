#type 1
print("--- type 1")
import module
module.show()
print(module.person)

#type 2 Naming as module
print("--- type 2")
import module as hits
hits.show()
print(hits.person)

#type 3
print("--- type 3")
from module import show 
module.show()


