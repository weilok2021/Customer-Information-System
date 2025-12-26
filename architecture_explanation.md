# Customer Information System - File Architecture

## Project Structure Overview

### app/
- **main.py**: Application entry point that initializes the FastAPI application and defines the root routes.

### app/common/
- **db.py**: Database initialization and connection management utilities.
- **logger.py**: Centralized logging configuration for consistent application logging.
- **exceptions.py**: Custom exception definitions for handling specific error cases.
- **utils.py**: Shared utility functions used across different modules.

### app/config/
- **settings.py**: Environment configuration settings and application constants.

### app/models/
- **customer_model.py**: Defines the Customer ORM and Pydantic schema models for data validation and serialization.

### app/data/
- **customer_repository.py**: Handles data access operations, acting as an abstraction layer between API and data storage.

### app/service/
- **customer_service.py**: Contains the business logic for processing customer data and operations.

### app/web/
- **customer_routes.py**: Defines the API endpoints for customer-related operations following REST principles.

### app/fake/
- **__init__.py**: Contains fake data generators for testing and development purposes.

### app/templates/
- **base.html**: Base HTML template providing the common layout structure for all pages.
- **customer_list.html**: Template for displaying a list of customers with pagination and search functionality.
- **customer_detail.html**: Template for showing detailed information about a specific customer.

### app/static/
#### app/static/css/
- **styles.css**: Main stylesheet containing CSS rules for the application's visual presentation.

#### app/static/js/
- **main.js**: JavaScript file containing client-side logic and interactive functionality.

### app/tests/
- **test_customer.py**: Unit and integration tests for the customer module functionality.