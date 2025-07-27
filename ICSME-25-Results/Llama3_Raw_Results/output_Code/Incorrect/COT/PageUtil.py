class PageUtil:
    # Constructor to initialize the PageUtil object
    def __init__(self, data, page_size):
        """
        Initialize the PageUtil object with the given data and page size.

        Args:
            data (list): The data to be paginated.
            page_size (int): The number of items per page.
        """
        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size

    # Method to retrieve a specific page of data
    def get_page(self, page_number):
        """
        Retrieve a specific page of data.

        Args:
            page_number (int): The page number to fetch.

        Returns:
            list: The data on the specified page.
        """
        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]

    # Method to retrieve information about a specific page
    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.

        Args:
            page_number (int): The page number to fetch information about.

        Returns:
            dict: The page information such as current page number, total pages, etc.
        """
        has_previous = page_number > 1
        has_next = page_number < self.total_pages
        page_info = {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": self.get_page(page_number)
        }
        return page_info

    # Method to search for items in the data
    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            dict: The search information such as total results and matching items.
        """
        # Convert the data to string for searching
        str_data = [str(item) for item in self.data]
        # Find the indices of the matching items
        indices = [i for i, item in enumerate(str_data) if keyword in item]
        # Get the matching items
        results = [self.data[i] for i in indices]
        # Calculate the total pages for the search results
        total_pages = (len(results) + self.page_size - 1) // self.page_size
        search_info = {
            "keyword": keyword,
            "total_results": len(results),
            "total_pages": total_pages,
            "results": results
        }
        return search_info