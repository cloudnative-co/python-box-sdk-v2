Maps = {
    "Comments.create": """{
        "item": {{
            "id": {item_id},
            "type": {item_type}
        }},
        "message": {message},
        "tagged_message": {tagged_message}
    }""",
    "Comments.update": """{
        "message": {message}
    }""",
    "Collaborations.create": """{{
        "accessible_by": {{
            "id": {accessible_by_id},
            "login": {accessible_by_login},
            "type": {accessible_by_type}
        }},
        "can_view_path": {can_view_path},
        "item": {{
            "id": {item_id},
            "type": {item_type}
        }},
        "role": {role}
    }}""",
    "Collaborations.update": """{{
        "can_view_path": {can_view_path},
        "expires_at": {expires_at},
        "role": {role},
        "status": {status}
    }}""",
    "Files.copy": """{{
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }},
        "version": {version}
    }}""",
    "Files.update": """{{
        "description": {description},
        "lock": {{
            "access": {lock_access},
            "expires_at": {lock_expires_at},
            "is_download_prevented": {lock_is_download_prevented}
        }},
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }},
        "permissions": {{
            "can_download": {permissions_can_download}
        }},
        "shared_link": {{
            "access": {shared_link_access},
            "password": {shared_link_password},
            "permissions":{{
                "can_download":{shared_link_permissions_can_download}
            }},
            "unshared_at": {shared_link_unshared_at}
        }},
        "tags": {tags}
    }}""",
    "Files.preflight": """{{
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }},
        "size": {size}
    }}""",
    "Files.upload": """{{
        "attributes": {{
            "content_created_at": {content_created_at},
            "content_modified_at": {content_modified_at},
            "name": {name},
            "parent": {{
                "id": {parent_id}
            }}
        }}
    }}""",
    "Files.restore": """{{
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }}
    }}""",
    "Folders.create": """{{
        "folder_upload_email": {{
            "access": {folder_upload_email_access}
        }},
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }},
        "sync_state": {sync_state}
    }}""",
    "Folders.copy": """{{
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }}
    }}""",
    "Folders.update": """{{
        "can_non_owners_invite": {can_non_owners_invite},
        "can_non_owners_view_collaborators": {can_non_owners_view_collaborators},
        "collections": [
            {{
                "id": {collections_id}
            }}
        ],
        "description": {description},
        "folder_upload_email": {{
            "access": {folder_upload_email_access}
        }},
        "is_collaboration_restricted_to_enterprise": {is_collaboration_restricted_to_enterprise},
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }},
        "shared_link": {{
            "access": {shared_link_access},
            "password": {shared_link_password},
            "permissions": {{
                "can_download": {shared_link_permissions_can_download}
            }},
            "unshared_at": {shared_link_unshared_at}
        }},
        "sync_state": {sync_state},
        "tags": {tags}
    }}""",
    "Folders.restore": """{{
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }}
    }}""",
    "Groups.create": """{{
        "description": {description},
        "external_sync_identifier": {external_sync_identifier},
        "invitability_level": {invitability_level},
        "member_viewability_level": {member_viewability_level},
        "name": {name},
        "provenance": {provenance}
    }}""",
    "Groups.update": """{{
        "description": {description},
        "external_sync_identifier": {external_sync_identifier},
        "invitability_level": {invitability_level},
        "member_viewability_level": {member_viewability_level},
        "name": {name},
        "provenance": {provenance}
    }}""",
    "GroupMemberships.add": """{{
        "configurable_permissions": {configurable_permissions},
        "group": {{
            "id": {group_id}
        }},
        "role": {role},
        "user": {{
            "id": {user_id}
        }}
    }}""",
    "GroupMemberships.update": """{{
        "configurable_permissions": {configurable_permissions},
        "role": {role}
    }}""",
    "Invites.create": """{{
        "actionable_by": {{
            "login": {actionable_by_login}
        }},
        "enterprise": {{
            "id": {enterprise_id}
        }}
    }}""",
    "Metadata.Template.create": """{{
        "copyInstanceOnItemCopy": {copy_instance_on_item_copy},
        "displayName": {display_name},
        "fields": {fields},
        "hidden": {hidden},
        "scope": {scope},
        "templateKey": {template_key}
    }}""",
    "Metadata.Template.update": """{items}""",
    "Metadata.CascadePolicies.create": """{{
        "folder_id": {folder_id},
        "scope": {scope},
        "templateKey": {template_key}
    }}""",
    "Metadata.CascadePolicies.enforcement": """{{
        "conflict_resolution": {conflict_resolution}
    }}""",
    "Tasks.create": """{{
        "action": {action},
        "completion_rule": {completion_rule},
        "due_at": {due_at},
        "item": {{
            "id": {item_id},
            "type": {item_type}
        }},
        "message": {message}
    }}""",
    "Tasks.update": """{{
        "action": {action},
        "completion_rule": {completion_rule},
        "due_at": {due_at},
        "message": {message}
    }}""",
    "Users.create": """{{
        "address": {address},
        "can_see_managed_users": {can_see_managed_users},
        "external_app_user_id": {external_app_user_id},
        "is_exempt_from_device_limits": {is_exempt_from_device_limits},
        "is_exempt_from_login_verification": {is_exempt_from_login_verification},
        "is_external_collab_restricted": {is_external_collab_restricted},
        "is_platform_access_only": {is_platform_access_only},
        "is_sync_enabled": {is_sync_enabled},
        "job_title": {job_title},
        "language": {language},
        "login": {login},
        "name": {name},
        "phone": {phone},
        "role": {role},
        "space_amount": {space_amount},
        "status": {status},
        "timezone": {timezone},
        "tracking_codes": {tracking_codes}
    }}""",
    "Users.update": """{{
        "address": {address},
        "can_see_managed_users": {can_see_managed_users},
        "enterprise": {enterprise},
        "is_exempt_from_device_limits": {is_exempt_from_device_limits},
        "is_exempt_from_login_verification": {is_exempt_from_login_verification},
        "is_external_collab_restricted": {is_external_collab_restricted},
        "is_password_reset_required": {is_password_reset_required},
        "is_sync_enabled": {is_sync_enabled},
        "job_title": {job_title},
        "language": {language},
        "login": {login},
        "name": {name},
        "notification_email": {{
            "email": {notification_email_email}
        }},
        "notify": {notify},
        "phone": {phone},
        "role": {role},
        "space_amount": {space_amount},
        "status": {status},
        "timezone": {timezone},
        "tracking_codes": {tracking_codes}
    }}""",
    "Versions.restoration": """{{
        "id": {file_version_id},
        "type": {type}
    }}""",
    "Versions.upload": """{{
        "attributes": {{
            "content_modified_at": {content_modified_at}
        }}
    }}""",
    "UploadSessions.create": """{{
        "file_name": {file_name},
        "file_size": {file_size},
        "folder_id": {folder_id}
    }}""",
    "UploadSessions.create_exists": """{{
        "file_name": {file_name},
        "file_size": {file_size}
    }}""",
    "UploadSessions.commit": """{{
        "parts": {parts}
    }}""",
    "Webhooks.create": """{{
        "address": {address},
        "target": {{
            "id": {target_id},
            "type": {target_type}
        }},
        "triggers": {triggers}
    }}""",
    "Webhooks.update": """{{
        "address": {address},
        "target": {{
            "id": {target_id},
            "type": {target_type}
        }},
        "triggers": {triggers}
    }}""",
    "WebLinks.create": """{{
        "description": {description},
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }},
        "url": {url}
    }}""",
    "WebLinks.update": """{{
        "description": {description},
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }},
        "url": {url}
    }}""",
    "WebLinks.restore": """{{
        "name": {name},
        "parent": {{
            "id": {parent_id}
        }}
    }}"""
}
