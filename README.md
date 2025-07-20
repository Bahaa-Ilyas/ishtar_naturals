# Ishtar Naturals Website

A professional Django-based website for Ishtar Naturals, featuring premium bee-based skincare products enhanced with nanotechnology. This website showcases the company's innovative lip balm and deodorant products with a beautiful yellow-brown color scheme inspired by natural honey and bee products.

## 🌟 Features

### ✨ Enhanced User Interface
- **Yellow-Brown Color Scheme**: Inspired by the uploaded lip balm design, featuring warm honey and amber tones
- **Dropdown Navigation**: Multi-level navigation with icons for intuitive browsing
- **Responsive Design**: Mobile-first approach ensuring perfect display on all devices
- **Professional Styling**: Modern design with honeycomb patterns and bee-inspired elements

### 🔐 User Authentication System
- **User Registration**: Complete signup process with form validation
- **Login/Logout**: Secure authentication with session management
- **User Profiles**: Personal account management and profile editing
- **Password Management**: Password change and reset functionality
- **Remember Me**: Optional persistent login sessions

### 📱 Navigation Structure
- **Home**: Hero section with company overview and product showcase
- **Products**: 
  - All Products overview
  - Lip Balm category
  - Deodorant category  
  - Product Bundles
- **About**:
  - Company story and mission
  - Team profiles (Dr. Bahaa Ilyas, Awas Faedi, Roza Qaidi)
  - Company history and values
- **Science**:
  - Propolis research and benefits
  - Nanotechnology applications
  - Scientific backing and studies
- **Contact**:
  - Contact forms
  - Company information
  - Customer support

### 🛍️ Product Management
- **Product Catalog**: Comprehensive product listings with images
- **Category Filtering**: Easy browsing by product type
- **Product Details**: Detailed descriptions, pricing, and specifications
- **Featured Products**: Highlighted bestsellers and new arrivals

### 🎨 Design Elements
- **Custom Icons**: FontAwesome icons throughout the interface
- **Color Palette**: 
  - Primary: #D4A574 (Warm honey)
  - Secondary: #8B4513 (Rich brown)
  - Accent: #F4E4BC (Light cream)
  - Background: #FFF8E7 (Soft ivory)
- **Typography**: Professional font hierarchy with excellent readability
- **Visual Effects**: Smooth transitions and hover effects

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ishtar-naturals-website.git
   cd ishtar-naturals-website
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Visit the website**
   Open your browser and go to `http://localhost:8000`

## 📁 Project Structure

```
ishtar_naturals/
├── ishtar_naturals/          # Main project settings
│   ├── settings.py           # Django configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
├── pages/                   # Static pages app
│   ├── views.py             # Page views
│   ├── urls.py              # Page URL patterns
│   └── models.py            # Page models
├── products/                # Products management app
│   ├── models.py            # Product models
│   ├── views.py             # Product views
│   └── admin.py             # Admin configuration
├── accounts/                # User authentication app
│   ├── views.py             # Authentication views
│   ├── forms.py             # User forms
│   └── urls.py              # Auth URL patterns
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── pages/               # Page templates
│   ├── products/            # Product templates
│   └── accounts/            # Authentication templates
├── static/                  # Static files
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files
│   └── images/              # Image assets
├── media/                   # User uploaded files
├── requirements.txt         # Python dependencies
├── Procfile                 # Heroku deployment
├── runtime.txt              # Python version
└── manage.py               # Django management script
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com
DATABASE_URL=sqlite:///db.sqlite3
```

### Database Configuration
- **SQLite** (default for development)
- **PostgreSQL** (recommended for production)
- **MySQL** (alternative option)

## 🚀 Deployment

### Heroku Deployment
1. **Install Heroku CLI**
2. **Create Heroku app**: `heroku create your-app-name`
3. **Set environment variables**: `heroku config:set SECRET_KEY=your-secret-key`
4. **Deploy**: `git push heroku main`

### GitHub Pages
1. **Generate static files**: `python manage.py collectstatic`
2. **Configure GitHub Pages** in repository settings

## 🛠️ Development

### Adding New Features
1. **Create new app**: `python manage.py startapp appname`
2. **Add to INSTALLED_APPS** in settings.py
3. **Create models** and run migrations
4. **Implement views** and URL patterns
5. **Create templates** with consistent styling

### Customizing Design
- **Edit CSS files** in `static/css/`
- **Update color variables** in the CSS root
- **Modify templates** in `templates/`
- **Add new images** to `static/images/`

## 📊 Key Features Implemented

### 1. Enhanced Navigation System
- Multi-level dropdowns for Products and About sections
- Icon integration using FontAwesome
- Hover effects with smooth transitions
- Mobile-responsive collapsible menu

### 2. User Authentication & Management
- Registration system with email verification
- Login/logout functionality with session management
- User profile management with editable information
- Password change and reset capabilities

### 3. Product Catalog System
- Dynamic product listings with database integration
- Category-based filtering (Lip Balm, Deodorant, Bundles)
- Product detail pages with comprehensive information
- Image management for product photos

### 4. Visual Design & Branding
- Yellow-brown color palette inspired by the lip balm design
- Honeycomb patterns and bee-inspired visual elements
- Professional typography with clear hierarchy
- Responsive grid system for all screen sizes

## 🔒 Security Features
- CSRF protection on all forms
- SQL injection prevention through Django ORM
- XSS protection with template escaping
- Secure headers configuration
- User input validation and sanitization


## 🙏 Acknowledgments

- **Team Members**: Dr. Bahaa Ilyas, Awas Faedi, Roza Qaidi
- **Design Inspiration**: Natural bee products and honey aesthetics
- **Technology Stack**: Django, Bootstrap, FontAwesome

---

**Made with ❤️ for Ishtar Naturals - Where Nature Meets Science**

