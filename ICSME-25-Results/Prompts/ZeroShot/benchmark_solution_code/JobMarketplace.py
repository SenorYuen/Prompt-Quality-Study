'''
# This is a class that provides functionalities to publish positions, remove positions, submit resumes, withdraw resumes, search for positions, and obtain candidate information.

class JobMarketplace:
    def __init__(self):

    def post_job(self, job_title, company, requirements):
        """
        This function is used to publish positions,and add the position information to the job_listings list.
        :return: None
        """

    def remove_job(self, job):
        """
        This function is used to remove positions,and remove the position information from the job_listings list.
        :return: None
        """

    def submit_resume(self, name, skills, experience):
        """
        This function is used to submit resumes,and add the resume information to the resumes list.
        :return: None
        """

    def withdraw_resume(self, resume):
        """
        This function is used to withdraw resumes,and remove the resume information from the resumes list.
        :return: None
        """

    def search_jobs(self, criteria):
        """
        This function is used to search for positions,and return the position information that meets the requirements.
        :return: The position information that meets the requirements,list.
        """

    def get_job_applicants(self, job):
        """
        This function is used to obtain candidate information,and return the candidate information that meets the requirements by calling the matches_requirements function.
        :return: The candidate information that meets the requirements,list.
        """



'''

class JobMarketplace:
    def __init__(self):
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        # requirements = ['requirement1', 'requirement2']
        job = {"job_title": job_title, "company": company, "requirements": requirements}
        self.job_listings.append(job)

    def remove_job(self, job):
        self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        resume = {"name": name, "skills": skills, "experience": experience}
        self.resumes.append(resume)

    def withdraw_resume(self, resume):
        self.resumes.remove(resume)

    def search_jobs(self, criteria):
        matching_jobs = []
        for job_listing in self.job_listings:
            if criteria.lower() in job_listing["job_title"].lower() or criteria.lower() in [r.lower() for r in job_listing["requirements"]]:
                matching_jobs.append(job_listing)
        return matching_jobs

    def get_job_applicants(self, job):
        applicants = []
        for resume in self.resumes:
            if self.matches_requirements(resume, job["requirements"]):
                applicants.append(resume)
        return applicants

    @staticmethod
    def matches_requirements(resume, requirements):
        for skill in resume["skills"]:
            if skill not in requirements:
                return False
        return True