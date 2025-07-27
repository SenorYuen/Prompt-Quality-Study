class PageUtil:
    """
    PageUtil class is a versatile utility for handling pagination and search functionalities in an efficient and convenient manner.
    """

    def __init__(self, data, page_size):
        """
        Initialize the PageUtil object with the given data and page size.
        :param data: list, the data to be paginated
        :param page_size: int, the number of items per page
        """
        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size

    def get_page(self, page_number):
        """
        Retrieve a specific page of data.
        :param page_number: int, the page number to fetch
        :return: list, the data on the specified page
        """
        # Calculate the start and end indices for the specified page
        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        
        # Return the data on the specified page
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.
        :param page_number: int, the page number to fetch information about
        :return: dict, containing page information such as current page number, total pages, etc.
        """
        # Calculate the start and end indices for the specified page
        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        
        # Determine if there are previous and next pages
        has_previous = page_number > 1
        has_next = page_number < self.total_pages
        
        # Return the page information
        return {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": self.data[start_index:end_index]
        }

    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        """
        # Initialize the search results
        search_results = [item for item in self.data if str(keyword) in str(item)]
        
        # Calculate the total pages for the search results
        total_pages = (len(search_results) + self.page_size - 1) // self.page_size
        
        # Return the search information
        return {
            "keyword": keyword,
            "total_results": len(search_results),
            "total_pages": total_pages,
            "results": search_results
        }