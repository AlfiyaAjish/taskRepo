from user_contact.main import  app
import uvicorn
app=app()

def main():
    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# If this script is executed directly, call the main function
if __name__ == "__main__":
    main()
