Providing context for chat conversations.
===
Current state: `works` (but prepare to get your hands dirty)

piraBot can give contextual clues in a jabber chat. It can be set to listen to a chat room on jabber and when an issue is mentioned will query the issue tracker to fetch contextual information and post that back to the chat.

#Example:

>(11:28:18 PM) jerrylindahl: piraBot: MFOL-17643  
>(11:28:20 PM) piraBot: MFOL-17643 Summary: PHP upgrade - Unit + acceptance test support on test slaves for both 5.3 and 5.5

### Requirements
* python3
* sleekxmpp
* jira


### Suggested
* py.test (for unit tests)
* Linux/BSD (only tested on linux)

Run tests with py.test from project root.

Configure by copying pira.example.cfg to pira.cfg.

### Configuring
Copy `pira.example.cfg` to `pira.config` and update the settings.

### Running

```python3 -m src.main
```
