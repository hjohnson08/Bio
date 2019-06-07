from flask import Flask, render_template, request      
import random
from random import sample

app = Flask(__name__)


@app.route("/")
def bio():
    return render_template("bio.html")

@app.route("/", methods = ["POST"])
def getvalue():
    lname = request.form["lname"]
    
    gender = request.form["gender"]
    
    bio = request.form["bio"]


    
    college_1 = request.form["college_1"]
    degree_1 = request.form["degree_1"]
    major_1 = request.form["major_1"]

    college_2 = request.form["college_2"]
    degree_2 = request.form["degree_2"]
    major_2 = request.form["major_2"]

    company_1 = request.form["company_1"]
    r1_c1 = request.form["r1_c1"]
    r2_c1 = request.form["r2_c1"]
    r3_c1 = request.form["r3_c1"]
    r4_c1 = request.form["r4_c1"]
    
    company_2 = request.form["company_2"]
    r1_c2 = request.form["r1_c2"]
    r2_c2 = request.form["r2_c2"]
    r3_c2 = request.form["r3_c2"]
    r4_c2 = request.form["r4_c2"]

    company_3 = request.form["company_3"]
    r1_c3 = request.form["r1_c3"]
    r2_c3 = request.form["r2_c3"]
    r3_c3 = request.form["r3_c3"]
    r4_c3 = request.form["r4_c3"]

    company_4 = request.form["company_4"]
    r1_c4 = request.form["r1_c4"]
    r2_c4 = request.form["r2_c4"]
    r3_c4 = request.form["r3_c4"]
    r4_c4 = request.form["r4_c4"]

    company_5 = request.form["company_5"]
    r1_c5 = request.form["r1_c5"]
    r2_c5 = request.form["r2_c5"]
    r3_c5 = request.form["r3_c5"]
    r4_c5 = request.form["r4_c5"]

    company_6 = request.form["company_6"]
    r1_c6 = request.form["r1_c6"]
    r2_c6 = request.form["r2_c6"]
    r3_c6 = request.form["r3_c6"]
    r4_c6 = request.form["r4_c6"]

    company_7 = request.form["company_7"]
    r1_c7 = request.form["r1_c7"]
    r2_c7 = request.form["r2_c7"]
    r3_c7 = request.form["r3_c7"]
    r4_c7 = request.form["r4_c7"]

    if gender == "M" and degree_1 == "M.D.":
        pronoun = "Dr."
        noun = "he"
    elif gender == "F" and degree_1 == "M.D.":
        pronoun = "Dr."
        noun = "she"
    elif gender == "M":
        pronoun = "Mr."
        noun = "he"
    else: 
        pronoun = "Ms."
        noun = "she"

    name = pronoun + " " + lname

    #FUNCTIONs

    #starter randomization
    starters = " Prior, ", " Previously, ", " Earlier, ", " Before joining "
    s1, s2, s3, s4 = sample(starters, 4)

    #number_roles function
    def roles(r1_c1, r2_c1, r3_c1, r4_c1):
        if not r2_c1 and not r3_c1  and not r4_c1:
            nr = 1
        elif not r3_c1 and not r4_c1:
            nr = 2
        elif not r4_c1:
            nr = 3
        else:
            nr = 4
        return nr
    
    #article function
    def article_function(x):
        if x == "J.D." or x ==  "B.S." or x == "B.A." or x == "BSA" or x == "BSBA" or x == "BBA" :
            return "a"
        else:
            return "an"

    verbs = " served as ", " held the role of ", " was "
    v1, v2, v3 = sample(verbs, 3)

    #getphrase1 function
    def getphrase1(number_roles, company_1, verb, role_1, role_2, role_3, role_4):
        
        if number_roles == 1:
           
            r1_op1 = verb + role_1 + " at " + company_1 + "."
            r1_op2 = verb + role_1 + " at " + company_1 + "."

            etext = r1_op1, r1_op2

        elif number_roles == 2:
           
            r2_op1 = verb + role_1 + " at " + company_1 + " and formerly was " + role_2 + " at the Company."
            r2_op2 = verb + role_1 + " at " + company_1 + " and formerly was " + role_2 + " at the Company."

            etext = r2_op1, r2_op2 

        elif number_roles == 3:
            r3_op1 = " held various positions at " + company_1 + " including " + role_1 + ", " + role_2 + ", and " + role_3 + "."
            r3_op2 = verb + role_1 + " at " + company_1 + " as well as " + role_2 + " and " + role_3 + "."
            
            etext = r3_op1, r3_op2
        
        elif number_roles == 4:
            r4_op1 = " held various positions at " + company_1 + " including " + role_1 + ", " + role_2 + ", " + role_3 + ", and " + role_4 + "."
            r4_op2 = " held various roles at " + company_1 + " including " + role_1 + ", " + role_2 + ", " + role_3 + ", and " + role_4 + "."
            etext = r4_op1, r4_op1

        fetext = random.choice(etext)
        return fetext
 
    
   
    #experincemaker function
    def experiencemaker1(company_name, phrase, name, starter):
        if not company_name:
             return ""
        else:
            return starter + name + phrase
     
    
    def experiencemaker2(company_name, prior_company, phrase, name, starter):
        if not company_name:
             return ""
        elif starter == " Prior, " or starter == " Previously, " or starter == " Earlier, ":
            return starter + name  + phrase
        else:
            return starter + prior_company + ", " + name  + phrase
    
    #addcollege
    def nodegree_2(article, degree, college, major):
        if degree_2 == "none": 
            education2 = ""
        else:
            education2 = " and " + article + " " + degree + major + " from " + college
        return education2

    #addmajor
    def major(major):
        if not major:
            return ""
        else:
            return " in " + major
    

     
     
    c1number_roles = roles(r1_c1, r2_c1, r3_c1, r4_c1)
    c2number_roles = roles(r1_c2, r2_c2, r3_c2, r4_c2)
    c3number_roles = roles(r1_c3, r2_c3, r3_c3, r4_c3)
    c4number_roles = roles(r1_c4, r2_c4, r3_c4, r4_c4)
    c5number_roles = roles(r1_c5, r2_c5, r3_c5, r4_c5)
    c6number_roles = roles(r1_c6, r2_c6, r3_c6, r4_c6)
    c7number_roles = roles(r1_c7, r2_c7, r3_c7, r4_c7)

    phrase1 = getphrase1(c1number_roles, company_1, v1, r1_c1, r2_c1, r3_c1, r4_c1)
    phrase2 = getphrase1(c2number_roles, company_2, v2, r1_c2, r2_c2, r3_c2, r4_c2)
    phrase3 = getphrase1(c3number_roles, company_3, v3, r1_c3, r2_c3, r3_c3, r4_c3)
    phrase4 = getphrase1(c4number_roles, company_4, v1, r1_c4, r2_c4, r3_c4, r4_c4)
    phrase5 = getphrase1(c5number_roles, company_5, v2, r1_c5, r2_c5, r3_c5, r4_c5)
    phrase6 = getphrase1(c6number_roles, company_6, v3, r1_c6, r2_c6, r3_c6, r4_c6)
    phrase7 = getphrase1(c7number_roles, company_7, v1, r1_c7, r2_c7, r3_c7, r4_c7)

    experience1 = experiencemaker1(company_1, phrase1, name, s1)
    experience2 = experiencemaker2(company_2, company_1, phrase2, noun, s2)
    experience3 = experiencemaker2(company_3, company_2, phrase3, name, s3)
    experience4 = experiencemaker2(company_4, company_3, phrase4, noun, s4)
    experience5 = experiencemaker2(company_5, company_4, phrase5, name, s1)
    experience6 = experiencemaker2(company_6, company_5, phrase6, noun, s2)
    experience7 = experiencemaker2(company_7, company_6, phrase7, name, s3)

    
    
    education1 = article_function(degree_1) + " " + degree_1 + major(major_1) + " from " + college_1
    education = " " + name + " holds " + education1 + nodegree_2(article_function(degree_2), degree_2, college_2, major(major_2)) + "."


    fullbio = bio + experience1 + experience2 + experience3 + experience4 + experience5 + experience6 + experience7 + education 

    return render_template("home.html", fullbio = fullbio)

if __name__ == "__main__":
    app.run(debug=True)