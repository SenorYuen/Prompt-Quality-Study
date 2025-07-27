class JobMarketplace:
    def __init__(self):
        # Initialize empty lists to store job listings and resumes
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        """
        This function is used to publish positions, and add the position information to the job_listings list.
        :return: None
        """
        # Create a dictionary to store job information
        job = {
            "job_title": job_title,
            "company": company,
            "requirements": requirements,
            "applicants": []
        }
        # Add the job to the job_listings list
        self.job_listings.append(job)

    def remove_job(self, job_title):
        """
        This function is used to remove positions, and remove the position information from the job_listings list.
        :return: None
        """
        # Iterate over the job_listings list to find the job to be removed
        for job in self.job_listings:
            if job["job_title"] == job_title:
                # Remove the job from the job_listings list
                self.job_listings.remove(job)
                break

    def submit_resume(self, name, skills, experience):
        """
        This function is used to submit resumes, and add the resume information to the resumes list.
        :return: None
        """
        # Create a dictionary to store resume information
        resume = {
            "name": name,
            "skills": skills,
            "experience": experience,
            "applied_jobs": []
        }
        # Add the resume to the resumes list
        self.resumes.append(resume)

    def withdraw_resume(self, name):
        """
        This function is used to withdraw resumes, and remove the resume information from the resumes list.
        :return: None
        """
        # Iterate over the resumes list to find the resume to be withdrawn
        for resume in self.resumes:
            if resume["name"] == name:
                # Remove the resume from the resumes list
                self.resumes.remove(resume)
                break

    def search_jobs(self, criteria):
        """
        This function is used to search for positions, and return the position information that meets the requirements.
        :return: The position information that meets the requirements, list.
        """
        # Initialize an empty list to store the search results
        search_results = []
        # Iterate over the job_listings list to find jobs that match the search criteria
        for job in self.job_listings:
            if criteria in job["job_title"] or criteria in job["company"] or criteria in job["requirements"]:
                # Add the job to the search results list
                search_results.append(job)
        # Return the search results
        return search_results

    def get_job_applicants(self, job_title):
        """
        This function is used to obtain candidate information, and return the candidate information that meets the requirements.
        :return: The candidate information that meets the requirements, list.
        """
        # Initialize an empty list to store the applicants
        applicants = []
        # Iterate over the job_listings list to find the job
        for job in self.job_listings:
            if job["job_title"] == job_title:
                # Iterate over the resumes list to find applicants who match the job requirements
                for resume in self.resumes:
                    if self.matches_requirements(job["requirements"], resume["skills"], resume["experience"]):
                        # Add the applicant to the applicants list
                        applicants.append(resume)
                break
        # Return the applicants
        return applicants

    def matches_requirements(self, requirements, skills, experience):
        """
        This function checks if a candidate's skills and experience match the job requirements.
        :return: True if the candidate matches the requirements, False otherwise.
        """
        # Iterate over the requirements to check if the candidate has the required skills and experience
        for requirement in requirements:
            if requirement not in skills and requirement not in experience:
                # Return False if the candidate does not match the requirements
                return False
        # Return True if the candidate matches the requirements
        return True


# Example usage:
job_marketplace = JobMarketplace()
job_marketplace.post_job("Software Engineer", "Google", ["Python", "Java", "5 years of experience"])
job_marketplace.submit_resume("John Doe", ["Python", "Java", "C++"], "5 years of experience")
print(job_marketplace.search_jobs("Software"))
print(job_marketplace.get_job_applicants("Software Engineer"))