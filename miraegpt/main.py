from miraegpt.backend.serve import app

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)