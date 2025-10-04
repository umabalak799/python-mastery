muthuSubjects = {"Maths", "Physics", "Chemistry"}
karthikSubjects = {"Science", "English", "Maths"}
ganeshSubjects = {"History", "Civics", "Maths"}

#common subjects for all
commonSub = muthuSubjects & karthikSubjects & ganeshSubjects
print ("Common subjects of all: ", commonSub)

#all subjects
allSub = muthuSubjects | karthikSubjects | ganeshSubjects
print ("All the subjects in Set: ", allSub)

#subject chose only by Muthu
muthuChoice = muthuSubjects - (karthikSubjects | ganeshSubjects)
print ("Muthu choice of subjects: ", muthuChoice)

#