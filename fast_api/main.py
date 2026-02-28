# -*- coding: utf-8 -*-
from fastapi import FastAPI, status
from fast_api.core.odoo_env import get_env


app = FastAPI(
    title="Avenue Core API",
    description="Backend services for Avenue Core.",
    version="1.0.0"
)


@app.get("/", tags=["General"], status_code=status.HTTP_200_OK)
async def read_root():
    """
    Root endpoint to verify the API is online.
    """
    with get_env() as env:
        print(env['res.partner'].search([]))
    return {
        "status": "online",
        "version": "1.0.0",
        "message": "Welcome to the Avenue Core Management API"
    }
