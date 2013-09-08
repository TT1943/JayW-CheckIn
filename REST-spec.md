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
