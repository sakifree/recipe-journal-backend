## *Recipe Journal*
***
* **Description:** An application that allows users to track their favorite recipes. They will be able to read, create, update, and delete an entry.
* **Technologies/Methods Used:** Python, Django, DjangoRestFramework, PostgreSQL, Render

### *Models*
***
![Recipe Model](https://i.imgur.com/zKO0eo1.png)


### *Routes*
***
| Endpoint | Method | Description |
| -------- | ------ | ----------- |
| /recipe | GET | grabs every recipe within the database |
| /recipe/:id | GET | reads a specific recipe entry |
| /recipe | POST | creates a new recipe  |
| /recipe/:id | PUT | updates a specific recipe based on the ID |
| /recipe/:id | DELETE | deletes a recipe entry |

#### *Extras*
***
* Hoping to add authentification
* Want users to be able to search for certain keywords within recipes