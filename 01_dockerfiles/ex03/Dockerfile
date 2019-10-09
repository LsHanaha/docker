FROM ubuntu

RUN apt-get update && apt-get upgrade -y
RUN apt install wget openssh-server ca-certificates postfix -y
RUN wget https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh && \
	chmod 777 ./script.deb.sh && \
	./script.deb.sh
RUN apt install gitlab-ce tzdata -y

EXPOSE 80 443 22

ENTRYPOINT (/opt/gitlab/embedded/bin/runsvdir-start &) && gitlab-ctl reconfigure && tail -f /dev/null
