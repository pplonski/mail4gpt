# Manage your email in ChatGPT ✉️🦜

Wouldn't it be fantastic if you could access your email in ChatGPT?

It is possible! 

This project introduces a novel integration of email management capabilities into ChatGPT via a custom REST API server. It is specifically designed to augment the functionality of custom GPTs, enabling them to handle email tasks efficiently within the ChatGPT environment.

This server makes access to **only one** email address. It should be configured in `.env` file. See details below. This server gives access to email reading/sending by auth token that is created when server is starting. 

[Here](https://api.mail4gpt.com/schema/swagger-ui/) is Swagger UI with endpoints docs.

Below is an example chat with email enabled. The chat history is available at https://chat.openai.com/share/8542aae6-74d7-47d3-bf2c-8f0c022985c3

![](/media/summary.png)


## Read email 

Reading email in ChatGPT.

![](./media/read-email.gif)

## Send email

Send response in ChatGPT.

![](./media/send-email.gif)

## Configure

Please check `.env-example` to check which variables to set. You can provide **only one** email address.

OpenAPI schema is available at address: https://api.mail4gpt.com/schema/

OpenAPI schema in Swagger UI is available at address: https://api.mail4gpt.com/schema/swagger-ui/.

![](/media/configure.gif)

## Deployment

The server is deployed with docker-compose. All configuration files are attached. If you need help with deployment please let us know!

## 👩‍💼🐦 Connect with Us on Twitter & Linkedin

Stay up-to-date with our latest projects by following us on Twitter ([MLJAR Twitter](https://twitter.com/MLJAROfficial)) and LinkedIn ([Aleksandra LinkedIn](https://www.linkedin.com/in/aleksandra-p%C5%82o%C5%84ska-42047432/) & [Piotr LinkedIn](https://www.linkedin.com/in/piotr-plonski-mljar/)). We look forward to connecting with you and hearing your thoughts, ideas, and experiences with mail4gpt. Let's explore the future of AI together!
