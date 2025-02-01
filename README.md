# FAQ Management System

A Django-based FAQ Management System with multi-language support, WYSIWYG editor integration, and REST API for managing FAQs.

---

## **Features**
- **Multi-language Support**: FAQs can be translated into multiple languages (e.g., Hindi, Telugu).
- **WYSIWYG Editor**: Rich text formatting for FAQ answers using django-ckeditor.
- **REST API**: CRUD operations for FAQs with language-specific responses.
- **Caching**: Redis-based caching for improved performance.
- **Admin Panel**: User-friendly interface for managing FAQs.
- **Unit Tests**: Comprehensive test coverage for models and API endpoints.
- **Docker Support**: Easy deployment using Docker and Docker Compose.

---


## **Prerequisites**
- Python 3.9 or higher
- Docker (optional, for containerized deployment)
- Redis (for caching)


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/faq_project.git
2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
3. Run migrations:
   ```bash
   python manage.py migrate
4. Start the server:
   ```bash
   python manage.py runserver

---

## API Usage
### **Endpoints**

*   **Fetch FAQs**: GET /api/faqs/
    
*   **Create FAQ**: POST /api/faqs/
    
*   **Update FAQ**: PUT /api/faqs//
    
*   **Delete FAQ**: DELETE /api/faqs//

- Fetch FAQs in English:
   ```bash
   python manage.py runserver

- Fetch FAQs in Hindi:

   ```bash
   curl http://localhost:8000/api/faqs/?lang=hi

- Fetch FAQs in Bengali:

   ```bash
   curl http://localhost:8000/api/faqs/?lang=bn

## Admin Panel


1.     ```bash
       python manage.py createsuperuser
    
2.  Access the admin panel at http://localhost:8000/admin/.
    
3.  Log in with your superuser credentials and manage FAQs.
   

## Deployment with Docker
1. Build and run the Docker container:

   ```bash
   docker-compose up --build
2. Access the app at http://localhost:8000.

## Testing

1. Run unit tests using pytest:    
   ```bash
   pytest

## Contributing
1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature
3. Commit your changes:

   ```bash
   git commit -m "feat: Add your feature"
4. Push to the branch:

   ```bash
   git push origin feature/your-feature
5. Open a pull request.


