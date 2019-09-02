import argparse
import os

OLD_DOMAIN_TEMPLATE = "{your_domain}"


def read_file(path):
    with open(path, "r") as old_file:
        str_file = old_file.read()
    return str_file


def update_new_domain(str_old_file, old_domain, new_domain):
    new_file = str_old_file.replace(old_domain, new_domain)
    return new_file


def create_new_file(path, str_new_file):
    with open(path,'w') as file_path:
        file_path.write(str_new_file)
    # new_file = open(path, "w+")
    # new_file.write(str_new_file)


def main(path):
    parser = argparse.ArgumentParser("get arg for get new domain")
    parser.add_argument("-d", dest="new_domain")
    args = parser.parse_args()
    new_domain = args.new_domain
    # frontend_url = args.new_domain
    # new_domain = _parse_domain(frontend_url)
    old_file = read_file(path)

    str_new_file = update_new_domain(old_file, OLD_DOMAIN_TEMPLATE, new_domain)
    create_new_file(path, str_new_file)


# def _parse_domain(frontend_url):
#     return urlparse(frontend_url).netloc


if __name__ == '__main__':
    os.system("pwd")
    main("nginx/nginx.conf")
    main("setup/prod/api-config.json")
    main("docker-compose-prod.yml")
    main("setup/prod/nginx/nginx_template.conf")
