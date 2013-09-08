GET /api/events
--
get list of all events.
return

    {
      "count" : "int32",
      "events" : [
        {
          "name" : "String" 
        }
      ]
    }

GET /api/event/:id/users
--
show list of people info
return

    {
      "count" : "int32"
      "users" : [
        {
          "contact" : {
            "name" : "String",
            "email" : "String",
            "phone" : "String",
            "wechat" : "String",
            "create_date" : "DateTime",
            "updated" : "DateTime"
          },
          "checked" : "boolean"
        }
      ]
    }

POST /api/event/:id/user/:user_id/checkin
--
mark people checked in

POST /api/event/:id/user/:user_id/uncheckin
--
mark people unchecked in

POST /api/users
--
Accepting content:

    {
      "name" : "String",
      "email" : "String",
      "phone" : "String",
      "wechat" : "String"
    }
    
return 302 and redirect to /api/user/:id where :id is the id of the new user
if email exists, return 409

POST /api/user/:id
--
accepting fields of

    {
      "name" : "String",
      "email" : "String",
      "phone" : "String",
      "wechat" : "String"
    }
    
return 204
