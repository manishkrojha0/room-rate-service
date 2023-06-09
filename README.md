# Room Rate Management

Room Rate Management is a web application built with Django that allows users to manage and filter room rates based on various criteria.

## Features

- Add, edit, and delete room rates
- Apply discounts to room rates
- Filter room rates based on room ID, date, and discount

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/room-rate-management.git
2. Navigate to the project directory: ```cd RoomRateManagementProject```
3. Create a virtual environment:```python -m venv env```
4. Activate the virtual environment:
 - For Windows: ```env\Scripts\activate```
 - For macOS and Linux:```source env/bin/activate```
5. Install required dependencies ```pip install -r requirements.txt```
6. Run database migrations: ```python manage.py migrate```
7. Start the development server: ```python manage.py runserver```
8. Open your web browser and visit http://localhost:8000/core to access the application.

# Usage of this project
 -  Add a Room Rate:
        1. Click on the "Add Room Rate" button.
        2. Fill in the required details for the room rate, including the room ID, rate, and any applicable discounts.
        3. Click "Save" to add the room rate.

 - Edit a Room Rate:
         1. Locate the room rate you want to edit in the list.
         2. Click on the "Edit" button next to the room rate.
         3. Update the details as needed.
         4. Click "Save" to update the room rate.

 - Delete a Room Rate:
        1. Locate the room rate you want to delete in the list.
        2. Click on the "Delete" button next to the room rate.
        3. Confirm the deletion when prompted.

 - Filter Room Rates:
   1. Fill in the desired filters in the filter form on the "Filter Room Rates" page.
   2. Click "Filter" to view the filtered room rates based on the selected criteria.

