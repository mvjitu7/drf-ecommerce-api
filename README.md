
# DRF E-commerce API

This is a RESTful API built using Django Rest Framework for an e-commerce platform. The API allows for managing users, products, and categories.

## Features

- **User Model**: Uses Django's built-in `auth.User` for user authentication.
- **Product Model**: Create, retrieve, update, and delete products.
- **Category Model**: Products are categorized under various categories.
- Full CRUD functionality for products and categories.
- RESTful API endpoints using Django Rest Framework.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mvjitu7/drf-ecommerce-api.git
   cd drf-ecommerce-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- Django's built-in authentication is used for user management.

### Product
- `GET /api/products/` - List all products
- `POST /api/products/` - Create a new product
- `GET /api/products/<id>/` - Retrieve a product by ID
- `PUT /api/products/<id>/` - Update a product by ID
- `DELETE /api/products/<id>/` - Delete a product by ID

### Category
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create a new category
- `GET /api/categories/<id>/` - Retrieve a category by ID
- `PUT /api/categories/<id>/` - Update a category by ID
- `DELETE /api/categories/<id>/` - Delete a category by ID

## Models

- **Product**: Represents a product in the e-commerce app with fields like `name`, `description`, `price`, and a foreign key to `Category`.
- **Category**: Represents product categories, having fields like `name`.

## Running Tests

You can run the tests using Django's test framework:

```bash
python manage.py test
```

## Contributing

Feel free to fork this repository and create a pull request if you want to contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
