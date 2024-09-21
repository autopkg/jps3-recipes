# Notes

## Current App Downloads

Examples of where download URLs redirect to:

### Gigapixel

- https://topazlabs.com/d/gigapixel/latest/mac/full
    - `HTTP 301` → https://downloads.topazlabs.com/deploy/TopazGigapixelAI/7.4.3/TopazGigapixelAI-7.4.3.pkg
- **pkg**

# Photo

- https://topazlabs.com/d/photo/latest/mac/full
    - `HTTP 301` → https://downloads.topazlabs.com/deploy/TopazPhotoAI/3.2.1/TopazPhotoAI-3.2.1.pkg
- **pkg**

# Video

- https://topazlabs.com/d/tvai/latest/mac/full
    - `HTTP 301` → https://downloads.topazlabs.com/deploy/TopazVideoAI/5.3.2/TopazVideoAI-5.3.2.dmg
- **dmg**


## Discoveries via Proxyman

### APIs

- Docs
    - [Topaz Web API](https://api.topaz-labs.net/)
        - [Swagger(?)](https://api.topaz-labs.net/docs)
            - https://api.topaz-labs.net/openapi.json
            - https://github.com/TopazLabs/topaz-web-api/blob/main/README.md#topaz-web-api _(not public? no longer extant? :shrug:)_
        - https://api.topaz-labs.net/redoc


- - - 

# Scratch

	https://api.topaz-labs.net/v2/app_state/unauthed?app_build_type=RELEASE&app_cname=GIGAPIXEL&app_version=7.4.1&arch=arm64&cpu_supports_avx=true&email_mac=9939e10df61bd712ddb34888970c61d969a499f4108d8c2b9e932ae70b21e081&license_expiration_datetime=2023-01-16T00:00:00&os_type=osx&os_version=15.0&user_email=someemail@company.tld

	HMAC-SHA256 key:'«key_grepped_from_strings»' input:'someemail@company.tld' result:'9939e10df61bd712ddb34888970c61d969a499f4108d8c2b9e932ae70b21e081'


```shell
#!/bin/zsh

function get_hmac () {
	echo -n $1 \
	| openssl dgst -r                                   \
        -sha256                                         \
        -hmac "${HMAC_KEY:-«key_grepped_from_strings»}" \
	| cut -d ' ' -f1
}

curl           \
	--silent   \
	--location \
	--url       "https://api.topaz-labs.net/v2/app_state/unauthed"  \
	--header    "x-api-key: ${x_api_key}"                           \
    --url-query "app_build_type=RELEASE"                            \
    --url-query "app_cname=GIGAPIXEL"                               \
    --url-query "app_version=7.4.1"                                 \
    --url-query "arch=arm64"                                        \
    --url-query "cpu_supports_avx=true"                             \
    --url-query "email_mac=$(get_hmac "$user_email")"               \
    --url-query "license_expiration_datetime=2023-01-16T00:00:00"   \
    --url-query "os_type=osx"                                       \
    --url-query "os_version=15.0"                                   \
    --url-query "user_email=${user_email}" \
    -o /dev/null \
    --write-out '%{json}'
```