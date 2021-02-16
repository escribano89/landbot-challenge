# Landbot Challenge

The landbot challenge description could be found [here](https://github.com/hello-umi/backend-challenge).

## Requirements

The app is dockerized: [Docker](https://www.docker.com/)

## Getting started
```bash
docker-compose up
```

This command will build the environment, running the migrations and the related services. The server will be started at http://127.0.0.1:8000.
In order to access to the container you execute the below command after the container is prepared:

```bash
docker-compose exec web sh
```

 ## Common tasks
 
 Once you have accessed to the container:
 
 Test execution 
```bash
python manage.py tests
```
 Flake8 checking
```bash
flake8
```

## Project details

The chat created using Landbot can be found here: https://chats.landbot.io/v3/H-828120-H1FT7FXKH6JDFW2Q/index.html

In order to give the desired functionality to the chatbot, we have implemented an API using Django, DRF, and Celery for the async tasks. (Further information about the API [here](https://github.com/escribano89/landbot-challenge/blob/master/docs/api.md)). All the notifications (email, slack) have been considered as async tasks, so they are managed by celery without blocking the main execution. To apply this decoupling we have used Django Signals to trigger the notification after some event (eg: user signup or assistance request). Celery takes care of these tasks using Redis as a broker. A Notification table has been included to prepare and build the notifications and check their current status.

The notifications have been developed to allow the addition of new topics and channels in an easy way, just including the new one in our mapping and implementing the concrete notification (covering it with the corresponding test).

The functionality has been covered with structured tests. We set up flake8 and Github actions to keep the code clean and green in every Pull Request. We have left some specific settings in the Django settings file, just to ease the testing process, but it must not be included in a realistic repository.

## Last considerations

- Review and expand the test suite.
- Consider the use of API versioning.
- We included a library to handle the phone validation. This could be replaced in case it doesn't fit correctly.
- We send all the notifications in the background, without applying that required "minute". So in case that is 100% necessary, we should implement it.
- In case of having code scalability issues, consider decoupling the business code from the infrastructure.
- Improve the API returning HTTP codes to be more concise (eg: 422 instead of 400 or 409 instead of 400)
- Now the chatbot only supports one iteration. If a user is already registered it returns a 400 bad request response. We could adapt it to the business requirements.

## Screenshots

![Slack](https://github.com/escribano89/landbot-challenge/blob/master/img/slack.PNG)
![Bot](https://github.com/escribano89/landbot-challenge/blob/master/img/final_bot.PNG)
![Signup](https://github.com/escribano89/landbot-challenge/blob/master/img/welcome.PNG)

