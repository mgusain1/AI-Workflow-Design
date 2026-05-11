AI Workflow Engine

A backend system for running AI-powered processing pipelines asynchronously.

This project simulates a simplified production-style AI workflow engine capable of:

accepting AI tasks through APIs
processing tasks through pipelines
tracking execution status
storing results
exposing task monitoring endpoints

The goal of this project is to understand how real-world AI backend systems orchestrate workflows such as summarization, classification, and information extraction.

Features
FastAPI-based backend APIs
SQLite database integration using SQLAlchemy
Task creation and tracking
Pipeline execution system
Result storage
Modular backend architecture
Swagger/OpenAPI documentation
Extensible workflow design
Current Supported Workflow
Summarization Pipeline

Accepts text input and processes it through a summarization workflow.

Task lifecycle:

pending → running → completed
