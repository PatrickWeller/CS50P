# watch.py for watching on youtube

# It turns out that (most) YouTube videos can be embedded in other websites.
# For instance, if you visit https://youtu.be/xvFZjo5PgG0 on a laptop or desktop,
# click Share, and then click Embed, you’ll see HTML
# (the language in which web pages are written) like the below,
# which you could then copy into your own website’s source code,
# wherein iframe is an HTML “element,” and src is one of several HTML “attributes” therein,
# the value of which, between quotes, is https://www.youtube.com/embed/xvFZjo5PgG0.

# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"
# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
# clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Because some HTML attributes are optional, you could instead minimally embed just the below.
# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

# Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages
# (e.g., https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter,
# shareable youtu.be URLs (e.g., https://youtu.be/xvFZjo5PgG0)
# where they can be watched on YouTube itself.

# In watch.py, implement a function called parse that expects a str of HTML as input,
# extracts any YouTube URL that’s the value of a src attribute of an iframe element therein,
# and returns its shorter, shareable youtu.be equivalent as a str.
# Expect that any such URL will be in one of the formats below.
# Assume that the value of src will be surrounded by double quotes.
# And assume that the input will contain no more than one such URL.
# If the input does not contain any such URL at all, return None.

# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0

import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"^<iframe.*src=\"(?:(?:https?://(?:www\.)?youtube.com/embed/))(.+)\".*</iframe>$", s):
        url_end =  match.group(1)
        url = "https://youtu.be/" + url_end
        return url
    else:
        return None




if __name__ == "__main__":
    main()
