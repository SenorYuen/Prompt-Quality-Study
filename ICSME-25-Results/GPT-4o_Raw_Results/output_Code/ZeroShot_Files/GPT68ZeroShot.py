class PageUtil:
    def __init__(self, data, page_size):
        """
        Initialize the PageUtil object with the given data and page size.
        :param data: list, the dataset to paginate
        :param page_size: int, the number of items per page
        """
        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size  # Calculate total pages

    def get_page(self, page_number):
        """
        Retrieve a specific page of data.
        :param page_number: int, the page number to retrieve
        :return: list, the data on the specified page
        """
        if page_number < 1 or page_number > self.total_pages:
            return []  # Return an empty list if the page number is out of range
        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.
        :param page_number: int, the page number to retrieve information for
        :return: dict, containing page information such as current page number, total pages, etc.
        """
        return {
            "current_page": page_number,
            "total_pages": self.total_pages,
            "page_size": self.page_size,
            "total_items": self.total_items,
            "has_previous": page_number > 1,
            "has_next": page_number < self.total_pages
        }

    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        """
        matching_items = [item for item in self.data if keyword.lower() in str(item).lower()]
        return {
            "total_results": len(matching_items),
            "items": matching_items
        }