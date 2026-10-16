# We are going to base our container on Ubuntu
FROM python:3.14


EXPOSE 5000

# We want to do all of our work in
# a directory called /conway
WORKDIR /app

# Even if you use the -y flag with apt, it will sometimes
# stop to ask the user to intervene. Setting the
# environment variable DEBIAN_FRONTEND to
# noninteractive tells apt to never do this, which ensures
# that the build is fully automated
ENV DEBIAN_FRONTEND=noninteractive

# Run a software update
RUN apt update && apt dist-upgrade -y

# Install the package we need to perform the build
# (build-essential gives us both GCC and make)
RUN apt install -y build-essential

RUN pip install flask
# Copy the files over
COPY . .
# Perform the build!

# When the user runs the container, run the conway executable:
CMD ["python3", "hello.py"]
