#import re

import extract_sections
import extract_name
import extract_email
import extract_postal
import extract_telephone
import extract_education
import extract_experience
import extract_skills


def get_fields(res, resume_sections, text):
    sections = extract_sections.detect_sections(text, resume_sections)
    #print(sections)
    """
    for key, value in sections.items():
        print(f"----SECTION = {key}")
        print(f"{value}")
    """

    header_section = sections.get("header", "")
    if not header_section:
        header_section = text[:1000]
    
    # Extract name (heuristic - from header)
    name = extract_name.extract_name(header_section)
    #print("-- NAME :", name)
    res.fullname = name

    # Extract contact info (heuristic — from header)
    # telephone numbers (can be cell, FAX)
    res.contact_phones = extract_telephone.find_telephone_numbers(header_section)
    res.contact_emails = extract_email.find_email_addresses(header_section)
    addresses = extract_postal.find_postal_addresses(header_section)
    #print("-- ADDRESSES :", addresses)
    if len(addresses) > 0:
        res.contact_postal = addresses[0]

    # Extract education records
    edu_section = sections.get("education", "")
    if not edu_section:
        edu_section = text
    education = extract_education.extract_education(edu_section)
    #print("-- EDUCATION :", education)
    res.education = education

    # Extract work experience
    exp_section = sections.get("work_experience", "")
    if not exp_section:
        exp_section = text
    res.experience = extract_experience.find_jobs(exp_section)

    # Extract skills
    skills_section = sections.get("skills", "")
    res.skills = extract_skills.get_skills(skills_section)


############################
TEST_RESUME_TEXT = """
John Smith
Software Engineer
john.smith@email.com
(555) 123-4567
LinkedIn: linkedin.com/in/johnsmith

EXPERIENCE
Senior Software Engineer
Tech Corporation, San Francisco, CA
January 2020 - Present
• Led development of microservices architecture
• Mentored team of 5 junior developers

Software Developer
StartupXYZ, Austin, TX
June 2018 - December 2019
- Built web applications using React and Node.js
- Collaborated with cross-functional teams

EDUCATION
Bachelor of Science in Computer Science
University of California, Berkeley
2014 - 2018

SKILLS
Python, JavaScript, React, AWS, Docker
"""

# Sample resume with complex formatting
TEST_COMPLEX_RESUME = """
Wesley Piper | Software Engineer
wes.piper@gmail.com • 402.981.0715 • Stafford County, VA

SUMMARY
Engineer with 10+ years building human-centered technology systems. Currently
researching AI's impact on education through Scribe Tree Writer, an experimental
platform that transforms AI from answer-provider to thinking partner.

PROFESSIONAL EXPERIENCE

PBS Distribution, Arlington, VA — Senior Software Engineer
May 2023 - Present
• Led development of enterprise Product Information Management system serving 100+ employees across departments
• Reduced training time by 30% through intuitive interface design based on user research and cognitive load principles
• Built scalable state management with React Query for real-time data sync

Foreign Policy Magazine, Washington, DC — Software Engineer
August 2021 - May 2023
• Increased subscriptions 40% through complete rebuild of subscription services using React, Angular, and RESTful APIs
• Improved user retention 25% by redesigning onboarding experience with data-driven UX optimizations and A/B testing

EDUCATION

Queen's University Belfast — M.A. English, 2009
Creighton University — B.S. Digital Design & Development, 2013

SKILLS
Languages: Python, TypeScript, JavaScript, PHP
Frontend: React, Next.js, Vue, Angular
Backend: Node.js, Django, Flask
"""

TEST_FOREIGN_RESUME = """
John Doe
johndoe@gmail.com | +91-9876543210 | linkedin.com/in/johndoe
Bangalore, Karnataka, India

Summary
Full Stack Developer with 5 years of experience in building web applications.

Experience
Senior Software Engineer at TCS Ltd
Jan 2021 - Present
- Built microservices using Python and FastAPI
- Deployed on AWS using Docker and Kubernetes

Jun 2018 - Dec 2020
Software Developer at Infosys Ltd
- Developed REST APIs using Java Spring Boot
- Worked with PostgreSQL and Redis

Education
B.Tech in Computer Science
Indian Institute of Technology, Delhi
2018
CGPA: 8.5/10

Skills
Python, Java, JavaScript, React, FastAPI, Spring Boot, Docker, Kubernetes, AWS, PostgreSQL, Redis, Git

Certifications
AWS Certified Solutions Architect
Kubernetes Administrator (CKA)

Projects
E-Commerce Platform | React, Node.js, MongoDB
"""

class TEST_RESUME():
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
                continue
            if k == 'experience':
                continue
            resume_class_values.append(k + ' : ' + str(v))            
        for degree in self.education:
            resume_class_values.append("DEGREE: %s" % degree)
        for job in self.experience:
            resume_class_values.append("JOB: %s" % job)
        return '\n'.join(resume_class_values)

if __name__ == "__main__":
    test_resume_object = TEST_RESUME()
    get_fields(test_resume_object, TEST_RESUME_TEXT)
    print(test_resume_object)

    test_resume_object = TEST_RESUME()
    get_fields(test_resume_object, TEST_COMPLEX_RESUME)
    print(test_resume_object)

    test_resume_object = TEST_RESUME()
    get_fields(test_resume_object, TEST_FOREIGN_RESUME)
    print(test_resume_object)
