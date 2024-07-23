grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
stydents={'Johnni','Bilbo','Steve','Khendrik','Aaron'}
grades_sr=[sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]
#print(grades_sr)
stydents=list(stydents)
#print(stydents)
dictionary={stydents[0]:grades_sr[0],stydents[1]:grades_sr[1],stydents[2]:grades_sr[2],stydents[3]:grades_sr[3],stydents[4]:grades_sr[4]}
print(dictionary)