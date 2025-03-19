from fastapi import FastAPI
from user_contact.scripts.core.handlers import user_handlers
import uvicorn
app = FastAPI()

# Include the user handler endpoints
app.include_router(user_handlers.user_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Contact Service"}
def main():
    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)

# If this script is executed directly, call the main function
if __name__ == "__main__":
    main()
