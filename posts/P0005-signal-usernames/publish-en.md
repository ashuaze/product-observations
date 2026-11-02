### 1/6

1/6
Signal's username is not your login, public handle or chat identity.

It is an address for one moment: starting a conversation without handing over your phone number.

That narrow role suggests a useful design principle: one identifier need not do every job.

### 2/6

2/6
In Signal's standard flow, a phone number registers the account. An exact username starts a message request. After acceptance, the chat shows a profile name, not that username.

Registration, discovery and presentation are separate layers.

https://support.signal.org/hc/en-us/articles/6712070553754-Phone-Number-Privacy-and-Usernames

### 3/6

3/6
By default, people who do not have your number cannot see it, but anyone who knows it can still find you.

To require username contact, set "Who can find me by my number" to Nobody.

Privacy and reachability move in opposite directions.

https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive

### 4/6

4/6
Signal has no searchable username directory. Usernames can change or disappear, and their QR code or link can be reset. Existing chats remain.

That makes a username closer to a revocable introduction than a permanent public identity. It is not proof of identity.

### 5/6

5/6
A current exception matters: Android beta 8.28+ tests phone-numberless registration through a paid Signal Login and cryptographic recovery keys.

That is a separate account-creation experiment, not a new property of usernames.

https://support.signal.org/hc/en-us/articles/11197884108826-Phone-Numberless-Registration-for-Android-beta

### 6/6

6/6
For builders, separate four questions:

- What proves account ownership?
- How can someone find me?
- What do they see after we connect?
- How do they verify it is me?

Combine those roles only when the convenience is worth the disclosure and lock-in.
