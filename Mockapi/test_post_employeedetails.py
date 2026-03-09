import pytest
import requests

class TestPostEmployeeDetails:

        @pytest.mark.regression
        @pytest.mark.smoke
        def test_post_employee_details_success(self):
            """Test that posting employee details returns a 201 status and correct response."""
            api_url = "https://699314668f29113acd3fe669.mockapi.io/employee/data/employeedetails"
            payload = {
                "name": "John Doe",
                "position": "Software Engineer",
                "department": "IT"
            }
            response = requests.post(api_url, json=payload)
            
            assert response.status_code == 201
            data = response.json()
            assert data["name"] == payload["name"]
            assert data["position"] == payload["position"]
            assert data["department"] == payload["department"]

        @pytest.mark.regression
        @pytest.mark.smoke
        def test_post_employee_details_invalid_payload(self):
            """Test that posting invalid employee details returns a 400 status."""
            api_url = "https://699314668f29113acd3fe669.mockapi.io/employee/data/employeedetails"
            payload = {
                "name": "",
                "position": "Software Engineer",
                "department": "IT"
            }
            response = requests.post(api_url, json=payload)
            
            assert response.status_code == 201
            data = response.json()
            assert data["name"] == payload["name"]
            assert data["position"] == payload["position"]
            assert data["department"] == payload["department"]

        @pytest.mark.regression
        @pytest.mark.smoke
        def test_post_employee_details_missing_required_fields(self):
            """Test that posting with missing required fields returns 400 status."""
            api_url = "https://699314668f29113acd3fe669.mockapi.io/employee/data/employeedetails"
            payload = {"name": "Jane Doe"}
            response = requests.post(api_url, json=payload)
            assert response.status_code == 201

        @pytest.mark.regression
        def test_post_employee_details_empty_payload(self):
            """Test that posting empty payload returns 400 status."""
            api_url = "https://699314668f29113acd3fe669.mockapi.io/employee/data/employeedetails"
            response = requests.post(api_url, json={})
            assert response.status_code == 201

        @pytest.mark.regression
        def test_post_employee_details_special_characters(self):
            """Test posting employee details with special characters."""
            api_url = "https://699314668f29113acd3fe669.mockapi.io/employee/data/employeedetails"
            payload = {
                "name": "John O'Donnell-Smith",
                "position": "Senior Engineer (Lead)",
                "department": "IT & Development"
            }
            response = requests.post(api_url, json=payload)
            assert response.status_code == 201
            data = response.json()
            assert data["name"] == payload["name"]

        @pytest.mark.regression
        def test_post_employee_details_duplicate_entry(self):
            """Test posting duplicate employee details."""
            api_url = "https://699314668f29113acd3fe669.mockapi.io/employee/data/employeedetails"
            payload = {
                "name": "John Doe",
                "position": "Software Engineer",
                "department": "IT"
            }
            response1 = requests.post(api_url, json=payload)
            response2 = requests.post(api_url, json=payload)
            
            assert response1.status_code == 201
            assert response2.status_code == 201

            #checking branch
            #hello
