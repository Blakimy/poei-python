"""A simple example of a hug API call with versioning"""
import hug


@hug.get('/echo', versions=1)
def echo(text):
    return text


@hug.get('/echo', versions=range(2, 5))
def echo(text):
    return 'Echo: {text}'.format(**locals())


@hug.get('/unversioned')
def hello():
    return 'Hello world!'


{"404": "The API call you tried to make was not defined. Here's a definition of the API to help you get going :)",
  "documentation": {
    "overview": "A basic (single function) API written using Hug",
    "handlers": {
      "/happy_birthday": {
        "GET": {
          "usage": "Says happy birthday to a user",
          "examples": [
            "http://localhost:8000/happy_birthday?name=HUG&age=1"
          ],
          "outputs": {
            "format": "JSON (Javascript Serialized Object Notation)",
            "content_type": "application/json"
          },
          "inputs": {
            "name": {
              "type": "Basic text / string value"
            },
            "age": {
              "type": "A Whole number"
            }
          }
        }
      }
    }
  }
}

"""A basic (single function) API written using Hug"""
import hug


@hug.get('/happy_birthday', examples="name=HUG&age=1")
def happy_birthday(name: hug.types.text, age: hug.types.number):
    """Says happy birthday to a user"""
    return "Happy {0} Birthday {1}!".format(name, age)

"""An example of writing an API to scrape hacker news once, and then enabling usage everywhere"""
import hug
import requests


@hug.local()
@hug.cli()
@hug.get()
def top_post(section: hug.types.one_of(('news', 'newest', 'show'))='news'):
    """Returns the top post from the provided section"""
    content = requests.get('https://news.ycombinator.com/{0}'.format(section)).content
    text = content.decode('utf-8')
    return text.split('<tr class=\'athing\'>')[1].split("<a href")[1].split(">")[1].split("<")[0]
view rawwrite_once.py hosted with ❤ by GitHub