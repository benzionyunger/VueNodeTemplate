import json
import os


class Config:
    def __init__(self , server_name):
        with open("setup/prod/"+server_name+"-config.json", 'r') as f:
            data = json.load(f)
        self.domain = data.get("domain")
        self.admin_email = data.get("admin_email")
        


api_config = Config('api')
# admin_config = Config('portal')


def get_certificate():
    print(os.system("ls -la"))
    docker_file = "docker-compose-setup-prod.yml"

    # API setup--------------------

    os.system("docker-compose -f {docker_file} up -d --build".format(docker_file=docker_file))
    # generate a certificate
    os.system('''docker-compose -f {docker_file} run --rm letsencrypt letsencrypt certonly --webroot --email {admin_email} --agree-tos -w /var/www/letsencrypt -d {domain}'''
              .format(docker_file=docker_file, admin_email=api_config.admin_email, domain=api_config.domain)
              )
    # down docker-compose-setup
    os.system("docker-compose -f {docker_file} stop".format(docker_file=docker_file))


    # # Web Portal setup--------------------

    # os.system("docker-compose -f {docker_file} up -d --build".format(docker_file=docker_file))
    # # generate a certificate
    # os.system('''docker-compose -f {docker_file} run --rm letsencrypt letsencrypt certonly --webroot --email {admin_email} --agree-tos -w /var/www/letsencrypt -d {domain}'''
    #           .format(docker_file=docker_file, admin_email=admin_config.admin_email, domain=admin_config.domain)
    #           )
    # # down docker-compose-setup
    # os.system("docker-compose -f {docker_file} stop".format(docker_file=docker_file))


def run_docker_production():
    docker_file = "docker-compose-prod.yml"
    os.system("docker-compose -f {docker_file} up -d".format(docker_file=docker_file))

if __name__ == '__main__':
    # go to root location
    # os.chdir("..")
    get_certificate()
    run_docker_production()