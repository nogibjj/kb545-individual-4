# kb545-individual-4

The following is a simple Flask App, that is pushed to DockerHub to be containerized, and is being hosted by Azure Web App. This results in an auto-scaling Flask app, completely hosted.

### Flask App

This project utilized ```Flask```, which is a Python package that easily containes HTML code, to allow easy hosting of web applications. The actual utilization of Flask is incredibly easy, and was used to hold the application as a whole. The app itself was used to simply learn how to make a proper transition with values, with the sole purpose of being used as boilderplate code for a much larger project (which can be found here https://github.com/nogibjj/Steam_Review__Analyzer )

The app can easily be run by either running the command ```python app.py```, or by running the application with Flask itself, through ```flask run```

### Docker

This project holds 2 Dockerfiles, one in ```.devcontainer``` and one in the root directory. The file in ```.devcontainer``` contains the Dockerfile that is used to activated GitHub Codespaces. This is necessary, and a standard for any project by this account. The second Dockerfile has a specific purpose, which is to create a DockerImage.

The reason that a DockerImage is necessasry, is that it can then be used to setup a container on DockerHub. However, there are a few steps necessary to get this. The following below are the steps necessary:

1. ```docker login --username=``` This command will link your DockerHub account to this repository. With this link established, DockerHub is easily able to communicate with the code in your local.
2. ```docker build app-name .``` This command will actually make the DockerImage locally, and will take a little bit to run. Once done, you will have a local DockerImage. This can be used to run the application with docker with the command ```docker run -p 5000:5000 app-name```. This step should only be done for testing purposes
3. ```docker push username/repo``` This command will finally send the DockerImage recently created to DockerHub. If successful, the container will offically be setup. You would see this below if successful

![image](https://github.com/nogibjj/kb545-individual-4/assets/55768636/7eef19f5-fb0c-42cf-a2a8-376d6fd5fdce)

### Azure Web App

With the DockerImage, and the container created, the next step performed was to upload the container information to Azure Web App. The purpose of setting up with Azure is because it has the tools to take the container, and link it with a public endpoint. In laymans terms, this takes the Flask app, and makes it easily accessible to anyone using the internet as normal. Once uploading it to the Azure Web App, all the user needs to do is set the ```WEBSITES_PORT=5000``` in the configurations menu, and then start the web app. The result would be using the public link anywhere. The following below is the public endpoint associated with this app.

(Note, if it is not working, it is either because the Web App shut down for a timer, or the Web App ran out of money needed to continue running)

Link: kian-flask-poc.azurewebsites.net

Video Link: https://youtu.be/sotbr6Wmn80

