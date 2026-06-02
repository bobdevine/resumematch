#!/usr/bin/env python3
# coding: utf8

"""Resune analyzer"""

import os
import sys

import parsers
import extraction

import personality

# sections to extract
RESUME_SECTIONS = [
    'summary',
    'objective',
    'skills',
    'work_experience',
    'education',
    'interests',
    'projects',
    'publications',
    'certifications',
    'awards',
    'languages',
    'references',
    'activities',
]

class Resume():
    # parsed/normalized resume format
    # Contact Information: Name, email, phone, LinkedIn, GitHub, address
    # Professional Experience: Job titles, companies, dates, responsibilities, locations
    # Education: Degrees, institutions, graduation dates, GPAs, honors
    # Skills: Categorized by type (programming, tools, languages, etc.)
    # Additional: Projects, certifications, languages, professional summary
    def __init__(self):
        self.fullname = None
        self.contact_emails = None
        self.contact_phones = None
        self.contact_postal = None
        #self.score = 0.0
        self.skills = None
        self.education = None
        self.experience = None
        self.projects = None

    # __str__ creates a human-readable string
    # __repr__ method is meant for debugging
    def __str__(self):
        attributes = vars(self)
        #print(attributes)
        resume_class_values = []
        for k,v in attributes.items():
            #print(" k", k, "v", v)
            if k == 'education':
                resume_class_values.append("-- EDUCATION --")
                for degree in self.education:
                    resume_class_values.append(" +DEGREE: %s" % degree)
            elif k == 'experience':
                resume_class_values.append("-- EXPERIENCE --")
                for job in self.experience:
                    resume_class_values.append(" +JOB: %s" % job)
            else:
                resume_class_values.append(k + ' : ' + str(v))
            
        return '\n'.join(resume_class_values)

    def fill(self, text):
        #print("fill ----")
        #print(text)
        extraction.get_fields(self, RESUME_SECTIONS, text)
        

def handle_resume(directory, file):
    text = None
    if file.endswith(".pdf"):
        print("---PDF FILE:", file)
        path = os.path.join(directory, file)
        text = parsers.extract_PDF(path)
    elif file.endswith(".docx"):
        print("---DOCX FILE:", file)
        path = os.path.join(directory, file)
        text = parsers.extract_DOCX(path)
    else:
        print("UNKNOWN FILE TYPE:", file)
        sys.exit()

    res = Resume()
    res.fill(text)
    """
    if file.endswith(".docx"):
        print("<<< ------ >>>")
        print(res)
    """

    # -- analyze resume for personality
    predictor = personality.Predictor()
    for degree in res.education:
        #print(" DEGREE--", degree)
        predictor.process(degree['degree'])
        predictor.process(degree['field'])
    for skill in res.skills:
        #print(" SKILL--", skill)
        predictor.process(skill)
    for job in res.experience:
        #print(" JOB--", job)
        predictor.process(job["description"])
        
    predictor.calculate_personality()
    predictor.print_personality_type_description()
    predictor.print_personality_type_jobs()

#--------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) == 1:
        # do all in the resumes directory
        directory = "resumes"
        files = os.listdir(directory)
        #print("Files:", files)

        for file in files:
            handle_resume(directory, file)
    else:
        #print("Argument List:", str(sys.argv))
        for file in sys.argv[1:]:
            handle_resume(".", file)
