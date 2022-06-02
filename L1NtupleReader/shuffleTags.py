import random
import math

files = ['taglist_eg_Pt0To200', 'taglist_eg_Pt200To500', 'taglist_qcdNoPU', 'taglist_pi_Pt0To200', 'taglist_qcdNoPU_Pt50To80', 'taglist_qcdNoPU_Pt80To120', 'taglist_qcdNoPU_Pt120To170']

for file in files:
    f = open('inputBatches/'+file+'.txt', 'r')

    tags = [tag.strip() for tag in f]
    random.shuffle(tags)
    dp = math.ceil(len(tags)/2)

    f.close()

    train = tags[:dp]
    test  = tags[dp:]

    with open('inputBatches/'+file+'.txt', 'w') as newFile:
        for tag in tags:
            newFile.write("%s\n" % tag)
        newFile.truncate(newFile.tell()-1)

    with open('inputBatches/'+file+'_train.txt', 'w') as newFile:
        for tag in train:
            newFile.write("%s\n" % tag)
        newFile.truncate(newFile.tell()-1)

    with open('inputBatches/'+file+'_test.txt', 'w') as newFile:
        for tag in test:
            newFile.write("%s\n" % tag)
        newFile.truncate(newFile.tell()-1)