# Resume Match - Resume / Job Matching Tool

An intelligent matching system that extracts info from resumes and job descriptions, calculating job-fit scores to streamline the recruitment process.

**Resume Match** is a tool designed to assist **HR professionals** in conducting personality assessments during recruitment. The system evaluates candidates using personality traits and classifies them into meaningful categories.

- Help HRs assess candidates beyond just skills and experience.
- Predict personality traits and recommend roles accordingly.
- Simplify the recruitment process with automated personality insights.
- Improve team fit and long-term performance.

## Extraction phase

This tool quickly extracts structured data from resumes (PDF or DOCX files) using regex patterns and heuristics — no ML models, no external AI APIs.

- **Name and Address** — find using multiple detection strategies
- **Emails, Phone Numbers, Websites** — regex-based extraction
- **Summary / Objective** — detected by section headers
- **Education** — degree, institution, year, GPA, field of study
- **Work Experience** — company, job title, date range, description
- **Skills** — section-based parsing + full-text scan against 200+ known skills
- **Certifications** — listed certifications
- **Projects** — project name, technologies used, description

## Evaluation phase

Then it predicts a candidate’s *personality* by analyzing their extracted resume details.

## Matching phase

A hiring recruiter can filter the candidate pool based on the evaluation.
This enables HRs to make **better hiring decisions** by identifying suitable roles for candidates based on their personality type.

