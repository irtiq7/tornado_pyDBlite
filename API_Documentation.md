**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

# /api/delete\_record/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "id": {
            "type": "number"
        }
    },
    "type": "object"
}
```


**Input Example**
```json
{
    "id": 0
}
```


**Output Schema**
```json
null
```





<br>
<br>

# /api/getting\_data/?

    Content-Type: application/json



<br>
<br>

# /api/greeting/\(?P\<fname\>\[a\-zA\-Z0\-9\_\\\-\]\+\)/\(?P\<lname\>\[a\-zA\-Z0\-9\_\\\-\]\+\)/?$

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "type": "string"
}
```


**Output Example**
```json
"Greetings, Named Person!"
```


**Notes**

Greets you.



<br>
<br>

# /api/post\_data/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "body": {
            "type": "string"
        },
        "guid": {
            "type": "string"
        }
    },
    "type": "object"
}
```


**Input Example**
```json
{
    "body": "Very Important Post-It Note",
    "guid": "information"
}
```


**Output Schema**
```json
null
```




