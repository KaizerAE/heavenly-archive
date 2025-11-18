#!/usr/bin/env python3
"""
Heavenly Archive - Main Application Entry Point

A beautiful event logging and achievement tracking system
inspired by Heaven Official's Blessing (天官赐福).

Author: KaizerAE
License: MIT
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
from pathlib import Path

# Application metadata
APP_NAME = "Heavenly Archive"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = (
    "A beautiful event logging and achievement tracking system "
    "inspired by Heaven Official's Blessing"
)

# Initialize FastAPI application
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Root endpoint - Returns welcome message
    """
    return """
    <html>
        <head>
            <title>Heavenly Archive</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    text-align: center;
                    padding: 40px;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 20px;
                    backdrop-filter: blur(10px);
                    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                }
                h1 {
                    font-size: 3em;
                    margin-bottom: 20px;
                }
                p {
                    font-size: 1.2em;
                    margin: 10px 0;
                }
                .links {
                    margin-top: 30px;
                }
                a {
                    color: #FFD700;
                    text-decoration: none;
                    margin: 0 15px;
                    font-size: 1.1em;
                    transition: color 0.3s;
                }
                a:hover {
                    color: #FFA500;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🌸 Heavenly Archive</h1>
                <p>天官赐福档案馆</p>
                <p>Record your journey with celestial elegance ✨</p>
                <div class="links">
                    <a href="/api/docs">📖 API Documentation</a>
                    <a href="/api/redoc">📚 ReDoc</a>
                    <a href="https://github.com/KaizerAE/heavenly-archive">💻 GitHub</a>
                </div>
                <p style="margin-top: 40px; font-size: 0.9em; opacity: 0.8;">
                    Version {version} | Built with ❤️ and inspired by 天官赐福
                </p>
            </div>
        </body>
    </html>
    """.format(version=APP_VERSION)


# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring
    """
    return {
        "status": "healthy",
        "app": APP_NAME,
        "version": APP_VERSION,
        "message": "May the heavens bless your journey 🌸"
    }


# Application startup event
@app.on_event("startup")
async def startup_event():
    """
    Actions to perform on application startup
    """
    print("\n" + "=" * 60)
    print(f"🌸 {APP_NAME} v{APP_VERSION}")
    print("天官赐福档案馆 - Heavenly Archive")
    print("=" * 60)
    print("✨ Application starting...")
    print("📚 API Documentation: http://localhost:8000/api/docs")
    print("🌐 Application: http://localhost:8000")
    print("=" * 60 + "\n")


# Application shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """
    Actions to perform on application shutdown
    """
    print("\n" + "=" * 60)
    print("🌸 Heavenly Archive shutting down...")
    print("May your records be preserved eternally ✨")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    # Run the application
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload during development
        log_level="info",
    )
