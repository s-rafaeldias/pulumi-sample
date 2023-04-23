FROM alpine:latest

ENV SERVICE_NAME "{{ name }}"
ENV SERVICE_TYPE "{{ service_type }}"

# START Pre install commands
{% for k in dockerfile.pre_install_commands %}
{{ k }}
{% endfor %}
# END Pre install commands

RUN "/bin/bash"
