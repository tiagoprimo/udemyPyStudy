from twilio.rest import Client

# put your own credentials here
account_sid = "AC080c59fdee92cb44e58b84d9a17de735"
auth_token = "1f1d4ea29ae882cca536e0ef1b7ca294"

client = Client(account_sid, auth_token)

client.messages.create(
    to="+55(19)992441046",
    from_="+553139561413",
    body="This is the ship that made the Kessel Run in fourteen parsecs?")