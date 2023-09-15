import requests
import json
import urllib.parse


following_users = []


def get_following(next_page):
    variables = {
        "id": "178370968",
        "include_reel": True,
        "fetch_mutual": True,
        "first": 100
    }

    if next_page:
        variables.after = next_page

    encoded_data = urllib.parse.quote(json.dumps(variables))

    url = f'https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={encoded_data}'

    headers = {
        'cookie': 'ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; mid=Y77zKwALAAGnTO9OePXhkK5-_IKg; ig_did=E3EE5711-FC2C-4306-8C0E-D5865F370DFD; datr=SmfBY5i8U6g0BVwtGNBOvdBz; csrftoken=p5cONvUeHdaheatf7oeUayhYUP4lrRHI; ds_user_id=178370968; dpr=1.25; shbid="19056\054178370968\0541725992440:01f77cbf6eb21abf629867f3e4df848d2b17de7d4291c22e2d5d6d5cd78be245929d49ab"; shbts="1694456440\054178370968\0541725992440:01f7a55c858429ed546b27fcdc9cfd9a78277b9531e7e5a23b90b58ba1caaf9911125eec"; sessionid=178370968%3A2crldhavVlDHfL%3A12%3AAYfEGjOtLSFV5KIxfDXzNOXKrJajEg156iF0QZFOgXM; fbsr_124024574287414=u2nmfrM5itYA3nBO7-GFg3Qni58vJRRg8Wuvl2nhbus.eyJ1c2VyX2lkIjoiMTAwMDAxMDA4MTEzODQ4IiwiY29kZSI6IkFRQzJpZ2lOa0tQQ2ROUXRxazFKdkJvNlF3T19taGE2WGNlNkpBSVp6VXF3R3hQYVNMOF9DSWNzcVUyRExldkU3LWphSTZzbHAwczdSNVE5TThxVjdhZTRBMkpfSXlsMXVmdXhQY3kzSnZCSF9PZ041dHNvcUpkdWZxemdlbFFmTUo0SnVvdkZsZy1salZDMTYtdVVwS1pXN0RmMXVzVkNZeWJuZ2E3V05ZTkVvNGFzZ1FfanAtb0IyVkNTd1JJWHhXOE50azBpYmI5bnNBRWxHNmlvTDd5Mjc1c2NxY2x1bmRlT0M3bTdXTmdGX1o0OG0tM0VOMm5BZW1kckxzeVk5bGdtRHJka3VObU9QUm5JcWFIQ2ZxWHVFeWNWVWRTVzdiV1hoc1VQQW0wZWVpRmluRElNUW91LTJ5d2FrajhqSmwtSFlYMV9IUUF6ek9NN3JWZmFpRkVCRkhMT2Y3UnN0OEx2TEhnNEVvZ3l5USIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQk8zeDNPUm92T1pCVlRnWGVLajVaQjFVNFZpYk44VG11SmhTNWJaQUU2bjBIWkFIUlNxNTZOY3hRSzIzN0JyTWZ2ODFxQnJzOGJJTVpBU3RweDdpcmVOQlpBVURPOHZvNUVvUEFyTHozTE50bHRWTldpWkJVSDhVcVZNbVFLUGRkb0ZscWdBNVJSMFJlRGlCWkJzRGZYeGNzc1NVWGFHczh1RUJORzhsNGxTVllVWkMwNElwMm8yc09BUDRnWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY5NDU3MjkyNX0; rur="NCG\054178370968\0541726109296:01f7fefbe6d94aa153e1e3c7ef4ea0fbd3fc16e4405cc5358869b9f0e7cdc71e5049310a"'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data["user"]["edge_followed_by"]["page_info"])
        for user in data.user.edge_followed_by.edges:
            following_users.append(user.node.username)

        page_info = data.data.user.edge_followed_by.page_info

        if page_info.has_next_page is True:
            get_following(page_info.end_cursor)
    else:
        print("ERROR: get following users")


if __name__ == '__main__':
    get_following("")

    print(following_users)
