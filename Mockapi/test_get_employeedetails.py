import pytest
import requests

class TestFetchEmployeeDetails:

    
    @pytest.mark.all
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_fetch_employee_details_success(self):
        """Test that fetching employee details returns a 200 status and correct first ID."""
        api_url = "https://699314668f29113acd3fe669.mockapi.io/employee/data/employeedetails"
        response = requests.get(api_url)
        
        # Validation
        assert response.status_code == 200
        data = response.json()
        assert data[0]["id"] == '1'

    @pytest.mark.all
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_fetch_employee_details_not_found(self):
        """Test that a non-existent employee ID returns a 404 status."""
        api_url = "https://699314668f29113acd3fe669.mockapi.io/employee/data/employeedetails/999"
        response = requests.get(api_url)
        
        # Validation
        assert response.status_code == 404