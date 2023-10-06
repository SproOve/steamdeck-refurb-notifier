# steamdeck-refurb-notifier
Check periodically, if my desired refurbished Steamdeck is available and notify.

## How does it work?
The script is running on a user set up period and notifies the user, when the desired steamdeck is available.

## Prerequisites
### Python v3

### pip packages
    pip install yagmail

### Further steps
- Edit [config_example.js] to your liking
- Rename [config_example.js] -> [config.js]

## Configuration 
| Syntax | Description |
| --- | --- | 
| ```pollInterval```: (*number*) | interval of polling in seconds, default is 300 = 5 minutes
|```notify64```: (*boolean*) | if set to true, you'll be notified, when the 64GB version is available
|```notify256```: (*boolean*) | if set to true, you'll be notified, when the 256GB version is available
|```notify512```: (*boolean*) | if set to true, you'll be notified, when the 512GB version is available
| ```mailAcc```: (*string*) | your Mailadress
| ```mailPW```: (*string*) | your Mailpassword


## Good to know
- I highly recommend using a separate emailaccount and not your mainaccount due to security reasons, even if you're running this locally
- When using 2FA, you probably need to generate an app-password and use it instead of your regular password
- right now its setup for an microsoft365 server, for gmail just remove everything after "yagmail.SMTP(mailAcc, mailPW...", this part will be generic in the future but right now it's just not :D 