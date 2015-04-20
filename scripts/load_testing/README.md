
Install locust (a "modern" load testing app)

    brew install libevent
    workon p97 # activate virtualenv
    pip install locustio

Run the locust server

    cd scripts/load_testing
    vi locustfile.py  # edit username and password
    locust --host=http://ofr.marineplanner.io

And visit the web interface at `127.0.0.1:8089` to start testing