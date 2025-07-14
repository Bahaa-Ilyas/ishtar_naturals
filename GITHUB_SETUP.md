# GitHub Setup and Deployment Guide

This comprehensive guide will walk you through setting up your Ishtar Naturals website on GitHub and deploying it for public access.

## 📋 Prerequisites

Before starting, ensure you have:
- A GitHub account (create one at https://github.com)
- Git installed on your computer
- The Ishtar Naturals website files (this project)
- Basic familiarity with command line/terminal

## 🚀 Step 1: Create GitHub Repository

### Option A: Using GitHub Website
1. **Sign in to GitHub** at https://github.com
2. **Click the "+" icon** in the top right corner
3. **Select "New repository"**
4. **Repository settings**:
   - Repository name: `ishtar-naturals-website`
   - Description: `Professional website for Ishtar Naturals bee-based skincare products`
   - Visibility: **Public** (required for GitHub Pages)
   - **Do NOT** initialize with README, .gitignore, or license (we have our own)
5. **Click "Create repository"**

### Option B: Using GitHub CLI (Advanced)
```bash
# Install GitHub CLI first: https://cli.github.com/
gh repo create ishtar-naturals-website --public --description "Professional website for Ishtar Naturals bee-based skincare products"
```

## 📁 Step 2: Prepare Your Local Repository

### Initialize Git Repository
```bash
# Navigate to your project directory
cd ishtar_naturals

# Initialize git repository
git init

# Add all files to staging
git add .

# Create initial commit
git commit -m "Initial commit: Ishtar Naturals website with authentication and enhanced UI"
```

### Connect to GitHub Repository
```bash
# Add GitHub repository as remote origin
git remote add origin https://github.com/YOUR_USERNAME/ishtar-naturals-website.git

# Verify remote connection
git remote -v

# Push to GitHub
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username**

## 🔧 Step 3: Configure Repository Settings

### Repository Settings
1. **Go to your repository** on GitHub
2. **Click "Settings" tab**
3. **Configure the following**:

#### General Settings
- **Repository name**: ishtar-naturals-website
- **Description**: Professional website for Ishtar Naturals bee-based skincare products
- **Website**: (will be filled after deployment)
- **Topics**: Add relevant tags like `django`, `skincare`, `ecommerce`, `bee-products`

#### Security Settings
- **Enable "Vulnerability alerts"**
- **Enable "Dependency graph"**
- **Configure "Code security and analysis"**

## 🌐 Step 4: Deployment Options

### Option A: Heroku Deployment (Recommended)

#### Prerequisites
- Heroku account (free at https://heroku.com)
- Heroku CLI installed

#### Deployment Steps
```bash
# Install Heroku CLI (if not already installed)
# Visit: https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create Heroku app
heroku create ishtar-naturals-app

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="ishtar-naturals-app.herokuapp.com"

# Deploy to Heroku
git push heroku main

# Run database migrations
heroku run python manage.py migrate

# Create superuser (optional)
heroku run python manage.py createsuperuser

# Open your deployed website
heroku open
```

#### Custom Domain (Optional)
```bash
# Add custom domain
heroku domains:add www.ishtarnaturals.com

# Configure DNS settings with your domain provider
# Point CNAME record to: ishtar-naturals-app.herokuapp.com
```

### Option B: GitHub Pages (Static Version)

#### Convert to Static Site
```bash
# Install Django static site generator
pip install django-distill

# Generate static files
python manage.py collectstatic --noinput
python manage.py distill-local --force

# Create gh-pages branch
git checkout -b gh-pages

# Copy static files to root
cp -r staticfiles/* .
cp -r dist/* .

# Commit and push
git add .
git commit -m "Deploy static site to GitHub Pages"
git push origin gh-pages
```

#### Enable GitHub Pages
1. **Go to repository Settings**
2. **Scroll to "Pages" section**
3. **Source**: Deploy from a branch
4. **Branch**: gh-pages
5. **Folder**: / (root)
6. **Click "Save"**

Your site will be available at: `https://YOUR_USERNAME.github.io/ishtar-naturals-website`

### Option C: VPS/Cloud Server Deployment

#### Server Requirements
- Ubuntu 20.04+ or similar Linux distribution
- Python 3.11+
- Nginx web server
- PostgreSQL database (recommended)

#### Deployment Script
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3-pip python3-venv nginx postgresql postgresql-contrib -y

# Clone repository
git clone https://github.com/YOUR_USERNAME/ishtar-naturals-website.git
cd ishtar-naturals-website

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
pip install gunicorn psycopg2-binary

# Set up PostgreSQL database
sudo -u postgres createdb ishtar_naturals
sudo -u postgres createuser ishtar_user
sudo -u postgres psql -c "ALTER USER ishtar_user PASSWORD 'secure_password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ishtar_naturals TO ishtar_user;"

# Configure environment variables
cp .env.example .env
# Edit .env file with your settings

# Run migrations
python manage.py migrate
python manage.py collectstatic --noinput

# Create systemd service
sudo nano /etc/systemd/system/ishtar-naturals.service
```

#### Systemd Service Configuration
```ini
[Unit]
Description=Ishtar Naturals Django Application
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/ishtar-naturals-website
Environment="PATH=/path/to/ishtar-naturals-website/venv/bin"
ExecStart=/path/to/ishtar-naturals-website/venv/bin/gunicorn --workers 3 --bind unix:/path/to/ishtar-naturals-website/ishtar_naturals.sock ishtar_naturals.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```

#### Nginx Configuration
```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/ishtar-naturals-website;
    }
    location /media/ {
        root /path/to/ishtar-naturals-website;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/ishtar-naturals-website/ishtar_naturals.sock;
    }
}
```

## 🔄 Step 5: Continuous Deployment

### GitHub Actions Workflow
Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Heroku

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy to Heroku
      uses: akhileshns/heroku-deploy@v3.12.12
      with:
        heroku_api_key: ${{secrets.HEROKU_API_KEY}}
        heroku_app_name: "ishtar-naturals-app"
        heroku_email: "your-email@example.com"
```

### Set up Secrets
1. **Go to repository Settings**
2. **Click "Secrets and variables" > "Actions"**
3. **Add repository secrets**:
   - `HEROKU_API_KEY`: Your Heroku API key
   - `SECRET_KEY`: Django secret key
   - `DATABASE_URL`: Production database URL

## 📊 Step 6: Monitoring and Analytics

### GitHub Repository Insights
- **Traffic**: Monitor repository visits and clones
- **Issues**: Track bug reports and feature requests
- **Pull Requests**: Manage code contributions
- **Security**: Monitor vulnerability alerts

### Website Analytics
```html
<!-- Add to base.html template -->
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_TRACKING_ID');
</script>
```

### Performance Monitoring
- **Heroku Metrics**: Monitor app performance
- **Error Tracking**: Use Sentry for error monitoring
- **Uptime Monitoring**: Use services like UptimeRobot

## 🔒 Step 7: Security Best Practices

### Repository Security
- **Enable two-factor authentication** on GitHub
- **Use branch protection rules** for main branch
- **Require pull request reviews** for changes
- **Enable security alerts** for dependencies

### Application Security
- **Keep dependencies updated** regularly
- **Use environment variables** for sensitive data
- **Enable HTTPS** in production
- **Regular security audits** of code

### Environment Variables Security
```bash
# Never commit these to repository
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
EMAIL_HOST_PASSWORD=your-email-password
STRIPE_SECRET_KEY=your-stripe-key
```

## 🚀 Step 8: Domain Configuration

### Custom Domain Setup
1. **Purchase domain** from registrar (GoDaddy, Namecheap, etc.)
2. **Configure DNS settings**:
   - A record: @ → Heroku IP addresses
   - CNAME record: www → your-app.herokuapp.com
3. **Add domain to Heroku**:
   ```bash
   heroku domains:add www.ishtarnaturals.com
   heroku domains:add ishtarnaturals.com
   ```
4. **Enable SSL certificate**:
   ```bash
   heroku certs:auto:enable
   ```

### SSL Certificate
- **Heroku**: Automatic SSL with custom domains
- **Let's Encrypt**: Free SSL certificates
- **Cloudflare**: CDN with SSL included

## 📈 Step 9: SEO and Marketing

### Search Engine Optimization
- **Submit sitemap** to Google Search Console
- **Verify domain** with search engines
- **Set up Google My Business** listing
- **Configure social media** meta tags

### Social Media Integration
```html
<!-- Open Graph tags for social sharing -->
<meta property="og:title" content="Ishtar Naturals - Premium Bee-Based Skincare">
<meta property="og:description" content="Revolutionary bee-based skincare products enhanced with nanotechnology">
<meta property="og:image" content="https://your-domain.com/static/images/og-image.jpg">
<meta property="og:url" content="https://your-domain.com">
```

## 🛠️ Step 10: Maintenance and Updates

### Regular Maintenance Tasks
- **Update dependencies** monthly
- **Monitor security alerts** weekly
- **Backup database** regularly
- **Review analytics** monthly
- **Update content** as needed

### Version Control Best Practices
```bash
# Create feature branches
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature: description"

# Push to GitHub
git push origin feature/new-feature

# Create pull request on GitHub
# Merge after review
```

### Deployment Checklist
- [ ] Code tested locally
- [ ] Dependencies updated
- [ ] Environment variables configured
- [ ] Database migrations ready
- [ ] Static files collected
- [ ] SSL certificate active
- [ ] Domain configured
- [ ] Analytics tracking active
- [ ] Error monitoring enabled
- [ ] Backup strategy in place

## 📞 Support and Troubleshooting

### Common Issues

#### Deployment Fails
```bash
# Check Heroku logs
heroku logs --tail

# Common fixes
heroku config:set DISABLE_COLLECTSTATIC=1
heroku run python manage.py migrate
```

#### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check WhiteNoise configuration
# Verify STATIC_ROOT setting
```

#### Database Connection Issues
```bash
# Check database URL
heroku config:get DATABASE_URL

# Run migrations
heroku run python manage.py migrate
```

### Getting Help
- **GitHub Issues**: Create issues for bugs
- **Heroku Support**: Use Heroku help center
- **Django Documentation**: https://docs.djangoproject.com
- **Community Forums**: Stack Overflow, Reddit

### Contact Information
- **Repository**: https://github.com/YOUR_USERNAME/ishtar-naturals-website
- **Website**: https://your-domain.com
- **Email**: support@ishtarnaturals.com

---

## 🎉 Congratulations!

You have successfully set up your Ishtar Naturals website on GitHub and deployed it to the web. Your professional bee-based skincare website is now live and ready to serve customers worldwide.

### Next Steps
1. **Test all functionality** on the live site
2. **Set up monitoring** and analytics
3. **Configure backup** strategies
4. **Plan content updates** and marketing
5. **Monitor performance** and user feedback

**Your website is now live and ready to showcase the power of nature enhanced by science!**

