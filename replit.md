# Overview

This is a FastAPI-based web application designed for image annotation and management. The system provides REST API endpoints for managing annotations, handling image uploads, exporting data in multiple formats, and integrating with AI services. The application follows a modular architecture with organized route handlers and supports cross-origin requests for web frontend integration.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Backend Framework
- **FastAPI**: Modern Python web framework chosen for its automatic API documentation, type hints support, and high performance
- **Modular Route Organization**: Routes are separated into logical modules (annotations, images, export, ai) for maintainability
- **CORS Middleware**: Configured to allow all origins, methods, and headers for flexible frontend integration

## API Design Patterns
- **RESTful Architecture**: Standard HTTP methods (GET, POST, PUT, DELETE) for resource manipulation
- **Pydantic Models**: Type validation and serialization for AI service requests and responses
- **Consistent Response Format**: Standardized JSON responses with message and data fields
- **Resource-Based URLs**: Clear endpoint structure with prefixed routes (/api/annotations, /api/images, etc.)

## Core Features
- **Image Management**: Upload, retrieve, and delete images with file handling capabilities
- **Annotation System**: Full CRUD operations for managing image annotations
- **Data Export**: Multiple export formats (JSON, CSV, XML) for data portability
- **AI Integration**: Ready-to-implement AI service endpoints with configurable token limits

## Application Structure
- **Health Monitoring**: Built-in health check endpoint for service monitoring
- **Automatic Documentation**: FastAPI's built-in Swagger UI and ReDoc documentation
- **Error Handling**: Structured error responses through FastAPI's exception handling

# External Dependencies

## Core Dependencies
- **FastAPI**: Web framework for building the REST API
- **Uvicorn**: ASGI server for running the FastAPI application
- **Pydantic**: Data validation and settings management
- **SQLAlchemy**: ORM for database operations and management
- **psycopg2-binary**: PostgreSQL database adapter for Python

## Potential Integrations
- **AI Services**: Architecture supports integration with OpenAI GPT models, Claude, or other LLM providers
- **File Storage**: Current implementation handles file uploads, ready for cloud storage integration
- **Database**: Supabase PostgreSQL integration via SQLAlchemy ORM for persistent storage of annotations and metadata
- **Frontend Applications**: CORS configuration allows integration with web frontends, mobile apps, or other client applications

## Development Tools
- **Python 3.7+**: Runtime environment
- **Type Hints**: Full type annotation support for better code maintainability