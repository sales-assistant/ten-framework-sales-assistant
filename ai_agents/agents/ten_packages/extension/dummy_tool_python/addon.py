#
#
# Agora Real Time Engagement
# Created by Tomas Liu in 2024-08.
# Copyright (c) 2024 Agora IO. All rights reserved.
#
#
from ten_runtime import (
    Addon,
    register_addon_as_extension,
    TenEnv,
)


@register_addon_as_extension("dummy_tool_python")
class DummyToolExtensionAddon(Addon):

    def on_create_instance(self, ten_env: TenEnv, name: str, context) -> None:
        from .extension import DummyToolExtension

        ten_env.log_info("DummyToolExtensionAddon on_create_instance")
        ten_env.on_create_instance_done(DummyToolExtension(name), context)
