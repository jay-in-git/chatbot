# Chatbot
A LINE chatbot that promotes myself.

QRcode:

![](./qrcode.png)

Notice that the chatbot might need time to be waken because Heroku will sleep automatically.(I didn't force Heroku to wake up because the there's limited time per month)
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
### Test on local
1. `ngrox http <port num>`
2. Copy the https url to LINE webhook url. Remember to add '/callback'.
3. `python app.py --port <port num>` port number should be the same as the one in 1.
 
 ---
### Features
使用 Message, Template, Flex Message 等模板，讓使用這可以透過按鍵互動來取得資料，不用花時間打字。

使用方式：
- 加入機器人 jay 為好友，會跳出選單，可以取得想知道的資訊。若無選單可打 profile 取得，大小寫不拘。
- 點擊每個資訊按鈕後會傳送文字訊息給 jay，若想直接打字跟 jay 取資訊也可以，要注意大小寫。
- 用 jay 來了解 jay 吧！
        
Code 經過初步的 refactor，未來若想添加新的介面會更加方便！
