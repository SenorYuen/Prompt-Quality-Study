class JobMarketplace:
    """
    This is a class that provides functionalities to publish positions, remove positions, submit resumes, withdraw resumes, search for positions, and obtain candidate information.
    """

    def __init__(self):
        self.job_listings = []  # List to store job listings
        self.resumes = []       # List to store resumes

    def post_job(self, job_title, company, requirements):
        """
        This function is used to publish positions, and add the position information to the job_listings list.
        :param job_title: The title of the position, str.
        :param company: The company of the position, str.
        :param requirements: The requirements of the position, list.
        :return: None
        """
        # Create a dictionary for the job and append it to job_listings
        job = {
            'job_title': job_title,
            'company': company,
            'requirements': requirements
        }
        self.job_listings.append(job)

    def remove_job(self, job):
        """
        This function is used to remove positions, and remove the position information from the job_listings list.
        :param job: The position information to be removed, dict.
        :return: None
        """
        # Remove the job from job_listings if it exists
        if job in self.job_listings:
            self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        """
        This function is used to submit resumes, and add the resume information to the resumes list.
        :param name: The name of the resume, str.
        :param skills: The skills of the resume, list.
        :param experience: The experience of the resume, str.
        :return: None
        """
        # Create a dictionary for the resume and append it to resumes
        resume = {
            'name': name,
            'skills': skills,
            'experience': experience
        }
        self.resumes.append(resume)

    def withdraw_resume(self, resume):
        """
        This function is used to withdraw resumes, and remove the resume information from the resumes list.
        :param resume: The resume information to be removed, dict.
        :return: None
        """
        # Remove the resume from resumes if it exists
        if resume in self.resumes:
            self.resumes.remove(resume)

    def search_jobs(self, criteria):
        """
        This function is used to search for positions, and return the position information that meets the requirements.
        :param criteria: The requirements of the position, str.
        :return: The position information that meets the requirements, list.
        """
        # Find jobs that meet the criteria
        matching_jobs = [
            job for job in self.job_listings
            if criteria in job['requirements']
        ]
        return matching_jobs

    def get_job_applicants(self, job):
        """
        This function is used to obtain candidate information, and return the candidate information that meets the requirements by calling the matches_requirements function.
        :param job: The position information, dict.
        :return: The candidate information that meets the requirements, list.
        """
        # Find resumes that match the job requirements
        applicants = [
            resume for resume in self.resumes
            if self.matches_requirements(job, resume)
        ]
        return applicants

    def matches_requirements(self, job, resume):
        """
        Helper function to check if a resume matches the job requirements.
        :param job: The job information, dict.
        :param resume: The resume information, dict.
        :return: bool, True if the resume matches the job requirements, False otherwise.
        """
        # Check if all job requirements are in the resume's skills
        return all(req in resume['skills'] for req in job['requirements'])