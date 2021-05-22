ielts_score = int(input("IELTS Score: "))
sat_score = int(input("SAT Score: "))

if ielts_score >= 7 or sat_score >= 80:
    print("Congratulations! you are qualified for the university admission.")
else:
    print("Unfortunately, you do not qualify for the admission. Good Luck for next time!")