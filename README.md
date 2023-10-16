# Data Processing Application with Docker

This repository contains a simple data processing application that utilizes Docker for containerization. The application processes data using Python and stores it in a SQLite database.

## Usage

### Prerequisites

Make sure you have Docker installed on your system. If you haven't already, you can download and install Docker from [here](https://www.docker.com/get-started).

### Clone the repo

Clone this repository, run the following command:

```bash
git clone https://github.com/Sefdine/Docker_initialization.git
```

### Build an image based on the Dockerfile

Open the terminal and go in the folder where you have your project. Run this command :

```
docker build -t data-processing-app .
```

