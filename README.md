# Chatbot
A LINE chatbot that promotes myself.

### Build on Heroku
The setting of Heroku and LINE interface is clear in the document of LINE website. This part is mainly focus on how to modify a sample chatbot on Heroku.
1. Follow the guideline https://developers.line.biz/en/docs/messaging-api/building-sample-bot-with-heroku/#deploy-the-kitchensink-sample-bot-app to setup a simple chatbot that only repeat what you've say. 
2. Create a repository that includes the following files:
    - Procfile: A file with the command to run your server.
    - The source codes of your server.
    - requirements.txt: the needed package for your server.
3. `heroku login -i` to login from Heroku CLI
4. Type `heroku git:remote -a chatbot-secretary` in your local repo directory to allow you to push the files to Heroku side.
5. Set the environment variables for Heroku:
    ```
    heroku config:set CHANNEL_ACCESS_TOKEN=<Your token from LINE interface>
    heroku config:set CHANNEL_SECRET=<Your secret from LINE interface>
    ```
    Notice that the name of the variables might be different, depending on the your program.
6. After finishing the steps above, we can just:
    ```
    git add <files>
    git commit -m "messages"
    git push <heroku / origin>
    ```
    The server should run without error!
 ---
 
### Features
