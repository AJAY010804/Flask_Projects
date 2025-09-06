# Flask Projects

## Overview
This is a Flask web application project that was imported from GitHub and set up to run in the Replit environment. The project provides a basic Flask application structure with API endpoints and a modern web interface.

## Project Architecture
- **Language**: Python 3.11
- **Framework**: Flask 3.0.0
- **Server**: Development server running on 0.0.0.0:5000
- **Deployment**: Configured for Replit's autoscale deployment

## Project Structure
```
.
├── app.py              # Main Flask application with routes
├── requirements.txt    # Python dependencies
├── .replit            # Replit configuration
├── .gitignore         # Git ignore file (Python-focused)
└── replit.md          # Project documentation
```

## Features
- **Home Route (/)**: Beautiful welcome page with project information
- **API Endpoints**:
  - `/api/test` - API status and version information
  - `/api/data` - Sample project data
  - `/health` - Health check endpoint
- **Replit Integration**: Properly configured for Replit's proxy environment
- **Modern UI**: Responsive design with gradient backgrounds and animations

## Recent Changes (September 6, 2025)
- Set up complete Flask application from minimal GitHub import
- Installed Python 3.11 and Flask dependencies
- Configured server to run on 0.0.0.0:5000 for Replit compatibility
- Created workflow for automatic server startup
- Implemented deployment configuration for production
- Added comprehensive API endpoints and modern web interface

## Development
The application runs automatically in Replit with the configured workflow. The server is set to debug mode for development convenience.

## Configuration
- **Host**: 0.0.0.0 (required for Replit proxy)
- **Port**: 5000 (Replit's designated frontend port)
- **Debug Mode**: Enabled for development
- **Deployment**: Autoscale configuration for production