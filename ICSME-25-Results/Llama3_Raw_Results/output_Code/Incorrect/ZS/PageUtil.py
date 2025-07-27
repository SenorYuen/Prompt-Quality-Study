class PageUtil:
    def __init__(self, data, page_size):
        # Initialize the PageUtil object with the given data and page size
        self.data = data
        self.page_size = page_size

    def get_page(self, page_number):
        # Calculate the start and end indices for the specified page
        start_index = (page_number - 1) * self.page_size
        end_index = page_number * self.page_size
        
        # Return the data on the specified page
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        # Calculate the total number of pages
        total_pages = -(-len(self.data) // self.page_size)  # Ceiling division
        
        # Retrieve information about the specified page
        page_info = {
            'current_page': page_number,
            'total_pages': total_pages,
            'page_size': self.page_size,
            'total_items': len(self.data)
        }
        
        return page_info

    def search(self, keyword):
        # Search for items in the data that contain the given keyword
        matching_items = [item for item in self.data if keyword.lower() in str(item).lower()]
        
        # Return search information
        search_info = {
            'keyword': keyword,
            'total_results': len(matching_items),
            'matching_items': matching_items
        }
        
        return search_info