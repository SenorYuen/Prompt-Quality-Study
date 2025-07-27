class JobMarketplace:
    def __init__(self):
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        job = {
            'job_title': job_title,
            'company': company,
            'requirements': requirements
        }
        self.job_listings.append(job)

    def remove_job(self, job):
        if job in self.job_listings:
            self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        resume = {
            'name': name,
            'skills': skills,
            'experience': experience
        }
        self.resumes.append(resume)

    def withdraw_resume(self, resume):
        if resume in self.resumes:
            self.resumes.remove(resume)

    def search_jobs(self, criteria):
        return [job for job in self.job_listings if criteria in job['requirements']]

    def get_job_applicants(self, job):
        return [resume for resume in self.resumes if self.matches_requirements(job, resume)]

    def matches_requirements(self, job, resume):
        return all(req in resume['skills'] for req in job['requirements'])