class JobMarketplace:
    """
    This is a class that provides functionalities to publish positions, remove positions, submit resumes, withdraw resumes, search for positions, and obtain candidate information.
    """

    def __init__(self):
        # Initialize empty lists for job listings and resumes
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        # Create a dictionary for the job listing and add it to the job_listings list
        job = {'job_title': job_title, 'company': company, 'requirements': requirements}
        self.job_listings.append(job)

    def remove_job(self, job):
        # Check if the job is in the job_listings list and remove it if found
        if job in self.job_listings:
            self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        # Create a dictionary for the resume and add it to the resumes list
        resume = {'name': name, 'skills': skills, 'experience': experience}
        self.resumes.append(resume)

    def withdraw_resume(self, resume):
        # Check if the resume is in the resumes list and remove it if found
        if resume in self.resumes:
            self.resumes.remove(resume)

    def search_jobs(self, criteria):
        # Filter the job_listings list to find jobs that match the given criteria
        matching_jobs = [job for job in self.job_listings if criteria in job['requirements']]
        return matching_jobs

    def get_job_applicants(self, job):
        # Filter the resumes list to find resumes that match the requirements of the given job
        matching_resumes = [resume for resume in self.resumes if all(requirement in resume['skills'] for requirement in job['requirements'])]
        return matching_resumes

    def matches_requirements(self, resume, job):
        # Check if the resume matches the requirements of the job
        return all(requirement in resume['skills'] for requirement in job['requirements'])