# APIs
Experiments with creating APIs

I'm learning how to build and serve APIs with Python. These scripts start
simple and get increasingly more complex. Host it locally by e.g. running
`python 02_serve-data.py`, then pointing your browser to 
`localhost:5002/people` - or use your command line via e.g.
`curl localhost:5002/people` to see the results.

### Details

You could build an API with vanilla Flask, see e.g. [here](https://mechlab-engineering.de/2017/11/deploy-your-machine-learning-model-as-rest-api-in-less-than-1-hour-with-scikit-learn-and-docker/). But the `flask_restful` package makes it easier.

### Misc

- Run `curl` with the `-v` argument to get a verbose output, including
HTTP status codes (200, 404, etc).
