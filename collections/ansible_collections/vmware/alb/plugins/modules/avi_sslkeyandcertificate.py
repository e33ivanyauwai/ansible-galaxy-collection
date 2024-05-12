#!/usr/bin/python
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_sslkeyandcertificate
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of SSLKeyAndCertificate Avi RESTful Object
description:
    - This module is used to configure SSLKeyAndCertificate object
    - more examples at U(https://github.com/avinetworks/devops)
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        choices: ["add", "replace", "delete", "remove"]
        type: str
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
    ca_certs:
        description:
            - Ca certificates in certificate chain.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    certificate:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: dict
    certificate_base64:
        description:
            - States if the certificate is base64 encoded.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    certificate_management_profile_ref:
        description:
            - It is a reference to an object of type certificatemanagementprofile.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    created_by:
        description:
            - Creator name.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    dynamic_params:
        description:
            - Dynamic parameters needed for certificate management profile.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    enable_ocsp_stapling:
        description:
            - Enables ocsp stapling.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enckey_base64:
        description:
            - Encrypted private key corresponding to the private key (e.g.
            - Those generated by an hsm such as thales nshield).
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    enckey_name:
        description:
            - Name of the encrypted private key (e.g.
            - Those generated by an hsm such as thales nshield).
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    format:
        description:
            - Format of the key/certificate file.
            - Enum options - SSL_PEM, SSL_PKCS12.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as SSL_PEM.
        type: str
    hardwaresecuritymodulegroup_ref:
        description:
            - It is a reference to an object of type hardwaresecuritymodulegroup.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    import_key_to_hsm:
        description:
            - Flag to enable private key import to hsm while importing the certificate.
            - Field introduced in 22.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    is_federated:
        description:
            - It specifies whether the object has to be replicated to the gslb followers.
            - Field introduced in 22.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    key:
        description:
            - Private key.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    key_base64:
        description:
            - States if the private key is base64 encoded.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    key_params:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    key_passphrase:
        description:
            - Passphrase used to encrypt the private key.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: list
        elements: dict
    name:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    ocsp_config:
        description:
            - Configuration related to ocsp.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    ocsp_error_status:
        description:
            - Error reported during ocsp status query.
            - Enum options - OCSP_ERR_CERTSTATUS_GOOD, OCSP_ERR_CERTSTATUS_REVOKED, OCSP_ERR_CERTSTATUS_UNKNOWN, OCSP_ERR_CERTSTATUS_SERVERFAIL_ERR,
            - OCSP_ERR_CERTSTATUS_JOBDB, OCSP_ERR_CERTSTATUS_DISABLED, OCSP_ERR_CERTSTATUS_GETCERT, OCSP_ERR_CERTSTATUS_NONVSCERT,
            - OCSP_ERR_CERTSTATUS_SELFSIGNED, OCSP_ERR_CERTSTATUS_CERTFINISH, OCSP_ERR_CERTSTATUS_CACERT, OCSP_ERR_CERTSTATUS_REQUEST,
            - OCSP_ERR_CERTSTATUS_ISSUER_REVOKED, OCSP_ERR_CERTSTATUS_PARSE_CERT, OCSP_ERR_CERTSTATUS_HTTP_REQ, OCSP_ERR_CERTSTATUS_URL_LIST,
            - OCSP_ERR_CERTSTATUS_HTTP_SEND, OCSP_ERR_CERTSTATUS_HTTP_RECV, OCSP_ERR_CERTSTATUS_HTTP_RESP.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- ocsp_err_certstatus_disabled), basic edition(allowed values-
            - ocsp_err_certstatus_disabled), enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as OCSP_ERR_CERTSTATUS_DISABLED.
        type: str
    ocsp_responder_url_list_from_certs:
        description:
            - This is an internal field to store the ocsp responder urls contained in the certificate.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: str
    ocsp_response_info:
        description:
            - Information related to ocsp response.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    status:
        description:
            - Enum options - SSL_CERTIFICATE_FINISHED, SSL_CERTIFICATE_PENDING.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as SSL_CERTIFICATE_FINISHED.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    type:
        description:
            - Enum options - SSL_CERTIFICATE_TYPE_VIRTUALSERVICE, SSL_CERTIFICATE_TYPE_SYSTEM, SSL_CERTIFICATE_TYPE_CA.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"

- name: Create a SSL Key and Certificate
  vmware.alb.avi_sslkeyandcertificate:
    avi_credentials: "{{ avi_credentials }}"
    key: |
        -----BEGIN PRIVATE KEY-----
        ....
        -----END PRIVATE KEY-----
    certificate:
        self_signed: true
        certificate: |
          -----BEGIN CERTIFICATE-----
          ....
          -----END CERTIFICATE-----
    type: SSL_CERTIFICATE_TYPE_VIRTUALSERVICE
    name: MyTestCert
"""

RETURN = '''
obj:
    description: SSLKeyAndCertificate (api/sslkeyandcertificate) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, avi_ansible_api)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        ca_certs=dict(type='list', elements='dict',),
        certificate=dict(type='dict', required=True),
        certificate_base64=dict(type='bool',),
        certificate_management_profile_ref=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        created_by=dict(type='str',),
        dynamic_params=dict(type='list', elements='dict',),
        enable_ocsp_stapling=dict(type='bool',),
        enckey_base64=dict(type='str',),
        enckey_name=dict(type='str',),
        format=dict(type='str',),
        hardwaresecuritymodulegroup_ref=dict(type='str',),
        import_key_to_hsm=dict(type='bool',),
        is_federated=dict(type='bool',),
        key=dict(type='str', no_log=True,),
        key_base64=dict(type='bool',),
        key_params=dict(type='dict',),
        key_passphrase=dict(type='str', no_log=True,),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        ocsp_config=dict(type='dict',),
        ocsp_error_status=dict(type='str',),
        ocsp_responder_url_list_from_certs=dict(type='list', elements='str',),
        ocsp_response_info=dict(type='dict',),
        status=dict(type='str',),
        tenant_ref=dict(type='str',),
        type=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'sslkeyandcertificate',
                           ['key', 'key_passphrase'])


if __name__ == '__main__':
    main()