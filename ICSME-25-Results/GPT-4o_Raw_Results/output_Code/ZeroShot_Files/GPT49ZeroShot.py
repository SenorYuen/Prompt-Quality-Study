class JobMarketplace:
    def __init__(self):
        # Initialize lists to store job listings and resumes
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        """
        This function is used to publish positions, and add the position information to the job_listings list.
        :param job_title: Title of the job
        :param company: Company offering the job
        :param requirements: Requirements for the job
        :return: None
        """
        # Create a job dictionary and append it to the job_listings
        job = {
            'job_title': job_title,
            'company': company,
            'requirements': requirements
        }
        self.job_listings.append(job)

    def remove_job(self, job):
        """
        This function is used to remove positions, and remove the position information from the job_listings list.
        :param job: The job to be removed
        :return: None
        """
        # Remove the job if it exists in the job_listings
        if job in self.job_listings:
            self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        """
        This function is used to submit resumes, and add the resume information to the resumes list.
        :param name: Name of the candidate
        :param skills: Skills of the candidate
        :param experience: Experience of the candidate
        :return: None
        """
        # Create a resume dictionary and append it to the resumes
        resume = {
            'name': name,
            'skills': skills,
            'experience': experience
        }
        self.resumes.append(resume)

    def withdraw_resume(self, resume):
        """
        This function is used to withdraw resumes, and remove the resume information from the resumes list.
        :param resume: The resume to be withdrawn
        :return: None
        """
        # Remove the resume if it exists in the resumes
        if resume in self.resumes:
            self.resumes.remove(resume)

    def search_jobs(self, criteria):
        """
        This function is used to search for positions, and return the position information that meets the requirements.
        :param criteria: The search criteria (e.g., job title, company, etc.)
        :return: The position information that meets the requirements, list.
        """
        # Find jobs that match the criteria
        matched_jobs = [
            job for job in self.job_listings
            if any(criteria.lower() in str(value).lower() for value in job.values())
        ]
        return matched_jobs

    def get_job_applicants(self, job):
        """
        This function is used to obtain candidate information, and return the candidate information that meets the requirements by calling the matches_requirements function.
        :param job: The job for which to find applicants
        :return: The candidate information that meets the requirements, list.
        """
        # Find resumes that match the job requirements
        matched_applicants = [
            resume for resume in self.resumes
            if self.matches_requirements(resume, job['requirements'])
        ]
        return matched_applicants

    def matches_requirements(self, resume, requirements):
        """
        Helper function to check if a resume matches the job requirements.
        :param resume: The resume of the candidate
        :param requirements: The requirements of the job
        :return: True if the resume matches the requirements, False otherwise
        """
        # Check if all requirements are met by the resume's skills
        return all(req.lower() in resume['skills'].lower() for req in requirements)