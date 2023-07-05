import ezgmail
# Send a basic email.
ezgmail.sent('recipiant@example.com', 'Subject line', 'Body of the email.')

# Send an attachment.
ezgmail.sent('recipiant@example.com', 'Subject line', 'Body of the email.', ['attachment1.jpg', 'attachment2.mp3'])

# NOTE: as part of its security and anti-spam features, Gmail might not send repeated emails with the exact same text.

# Send with cc and bcc.
ezgmail.sent('recipiant@example.com', 'Subject line', 'Body of the email.', cc = 'friend@example.com', bcc = 'otherFriend@example.com,someoneelse@example.com')

