## keybase-notification-api
Accepts POSTs with a `message` and `username` parameter and sends chat messages. It's designed to use Keybase as an encrypted self-notification system (like Pushover, but with end-to-end encryption), although it works to message users other than yourself too.

# Usage
`docker run --name "keybase-api" -e "KEYBASE_USERNAME=<username>" -e "KEYBASE_PAPERKEY=<key> -p "4433:4433" bencouture/keybase-notification-api`

Run the contauner with the KEYBASE_USERNAME and KEYBASE_PAPERKEY environment variables. These are used to provision the container as a one-shot device using the `keybase oneshot` command. This doesn't modify your chain like it would if you did a proper `keybase login`. Documentation on this feature is very sparse, I couldn't find a proper wiki or explanation of how this feature works.

You can generate your paper key through the web UI, or with the `keybase paperkey` command.

The API itself runs on port 4433, and accepts either a form or JSON payload. `message` is required, `username` is optional and defaults to the `KEYBASE_USERNAME` environment variable, which means the default is to message yourself.
