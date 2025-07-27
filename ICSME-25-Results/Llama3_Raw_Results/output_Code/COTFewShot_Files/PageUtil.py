class PageUtil:
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

    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        
        Args:
            keyword (str): The keyword to search for.
        
        Returns:
            dict: The search information such as total results and matching items.
        """
        matching_items = [item for item in self.data if str(keyword) in str(item)]
        total_results = len(matching_items)
        total_pages = (total_results + self.page_size - 1) // self.page_size
        search_info = {
            "keyword": keyword,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": matching_items
        }
        return search_info