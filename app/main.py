import uvicorn
from server.server import create_server


def main():
    server = create_server()
    uvicorn.run(server)


if __name__ == "__main__":
    main()
