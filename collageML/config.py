#  IN THE NAME OF ALLAH
#
#  You should run this file to allow https://quera.org to connect to your jupyter lab.
#  For security purposes, a random `token` is set specially for you in this file. This is YOUR token. Keep it secure.

###############################################################
#       IMPORTANT:                                            #
#  Do not share this file or your token with other people.    #
###############################################################

import os


def main():
    token = "3741ddd0-68b0-40f0-b412-289a7b8f1587"
    url = "https://quera.org"
    config = """
c.NotebookApp.tornado_settings = {{
    'headers': {{
        'Content-Security-Policy': "frame-ancestors {0} 'self' ",
        'Access-Control-Allow-Origin': "{0}",
        'X-Content-Type-Options': 'allow-from {0}',
        'X-Frame-Options': 'allow-from {0}',
        'access-control-allow-credentials': True,
        'Access-Control-Allow-Methods': 'GET, PUT, POST, PATCH, DELETE, OPTIONS'
    }}
}}
c.NotebookApp.allow_origin = '{0}'
c.NotebookApp.token = '{1}'
c.NotebookApp.allow_credentials = True
    """.format(
        url, token
    )

    jupyter_dir = os.path.join(os.path.expanduser("~"), ".jupyter")
    if not os.path.exists(jupyter_dir):
        # Create ~/.jupyter directory if it doesn't exist
        os.makedirs(jupyter_dir)

    with open(os.path.join(jupyter_dir, "jupyter_notebook_config.py"), "w+") as fp:
        # Append config to ~/.jupyter/jupyter_notebook_config.py
        fp.write(config)


if __name__ == "__main__":
    main()
