# Ishtar Naturals Website - Deployment Guide

## Quick Start Guide

### For GitHub Repository Setup

1. **Create GitHub Repository**:
   - Go to GitHub.com and sign in
   - Click "New Repository"
   - Name: `ishtar-naturals-website`
   - Make it Public
   - Don't initialize with README (we have our own)

2. **Upload Code to GitHub**:
   ```bash
   # Navigate to project directory
   cd ishtar-naturals-website
   
   # Initialize git repository
   git init
   
   # Add all files
   git add .
   
   # Commit files
   git commit -m "Initial commit: Ishtar Naturals website"
   
   # Add remote repository (replace with your GitHub URL)
   git remote add origin https://github.com/yourusername/ishtar-naturals-website.git
   
   # Push to GitHub
   git push -u origin main
   ```

### For Local Development

1. **Clone and Setup**:
   ```bash
   git clone https://github.com/yourusername/ishtar-naturals-website.git
   cd ishtar-naturals-website
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

2. **Access the Website**:
   - Website: http://localhost:8000
   - Admin: http://localhost:8000/admin

### For Production Deployment

#### Option 1: Heroku (Recommended for beginners)

1. **Install Heroku CLI** from https://devcenter.heroku.com/articles/heroku-cli

2. **Create Heroku App**:
   ```bash
   heroku create your-app-name
   ```

3. **Add Buildpack**:
   ```bash
   heroku buildpacks:set heroku/python
   ```

4. **Deploy**:
   ```bash
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

#### Option 2: VPS/Server Deployment

1. **Server Requirements**:
   - Ubuntu 20.04+ or similar
   - Python 3.8+
   - Nginx or Apache
   - SSL certificate (Let's Encrypt recommended)

2. **Installation Steps**:
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python and dependencies
   sudo apt install python3 python3-pip python3-venv nginx -y
   
   # Clone repository
   git clone https://github.com/yourusername/ishtar-naturals-website.git
   cd ishtar-naturals-website
   
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   pip install gunicorn
   
   # Setup database
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py collectstatic
   ```

3. **Configure Gunicorn**:
   ```bash
   # Test Gunicorn
   gunicorn ishtar_naturals.wsgi:application --bind 0.0.0.0:8000
   ```

4. **Configure Nginx**:
   Create `/etc/nginx/sites-available/ishtar-naturals`:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location = /favicon.ico { access_log off; log_not_found off; }
       location /static/ {
           root /path/to/ishtar-naturals-website;
       }
       
       location / {
           include proxy_params;
           proxy_pass http://unix:/path/to/ishtar-naturals-website/ishtar_naturals.sock;
       }
   }
   ```

5. **Enable Site**:
   ```bash
   sudo ln -s /etc/nginx/sites-available/ishtar-naturals /etc/nginx/sites-enabled
   sudo nginx -t
   sudo systemctl restart nginx
   ```

### Using ATOM Editor

1. **Install ATOM**: Download from https://atom.io

2. **Recommended Packages**:
   - python-tools
   - django-templates
   - file-icons
   - minimap
   - atom-beautify

3. **Open Project**:
   - File → Open Folder
   - Select the `ishtar-naturals-website` folder

4. **Editing Files**:
   - Templates: `templates/` folder
   - Styles: `static/css/style.css`
   - JavaScript: `static/js/main.js`
   - Models: `products/models.py`, `pages/models.py`
   - Views: `products/views.py`, `pages/views.py`

### Important Files to Know

- **Settings**: `ishtar_naturals/settings.py` - Main configuration
- **URLs**: `ishtar_naturals/urls.py` - Main URL routing
- **Models**: Define database structure
- **Views**: Handle business logic
- **Templates**: HTML files with Django template language
- **Static Files**: CSS, JavaScript, images

### Admin Credentials

Default superuser created during setup:
- Username: admin
- Email: admin@ishtarnaturals.com
- Password: admin123

**⚠️ IMPORTANT**: Change these credentials in production!

### Maintenance Tasks

1. **Update Content**:
   - Use Django admin interface
   - Edit templates for layout changes
   - Modify CSS for styling changes

2. **Backup Database**:
   ```bash
   python manage.py dumpdata > backup.json
   ```

3. **Restore Database**:
   ```bash
   python manage.py loaddata backup.json
   ```

4. **Update Code**:
   ```bash
   git pull origin main
   python manage.py migrate
   python manage.py collectstatic
   sudo systemctl restart gunicorn
   ```

### Troubleshooting

1. **Static Files Not Loading**:
   ```bash
   python manage.py collectstatic --clear
   ```

2. **Database Issues**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Permission Errors**:
   ```bash
   sudo chown -R www-data:www-data /path/to/project
   ```

### Support

For technical support:
- Check Django documentation: https://docs.djangoproject.com/
- Review server logs: `sudo tail -f /var/log/nginx/error.log`
- Check application logs in terminal

---

**Happy Deploying! 🚀**

