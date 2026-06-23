from astrbot.api import AstrBot, MessageEvent, register
from astrbot.api.message_components import At, Plain

@register("astrbot_plugin_gjqyou", "oldgirl", "群趣味互动插件", "1.0.0")
class GroupFunPlugin:
    def __init__(self, astrbot: AstrBot):
        self.astrbot = astrbot
        self.cmd_map = {
            "拍": "{at}，拍死你。",
            "踢": "{at}，踢飞你。",
            "丢": "直接把{at}丢进垃圾桶。",
            "千年杀": "使出全力一击无敌千年杀，{at}被贯穿。"
        }

    async def activate(self):
        self.astrbot.logger.info("[astrbot_plugin_gjqyou] 互动插件加载完成，指令：拍/踢/丢/千年杀 @群友")

    async def deactivate(self):
        self.astrbot.logger.info("[astrbot_plugin_gjqyou] 互动插件已卸载")

    async def on_message(self, event: MessageEvent):
        if not event.is_group():
            return

        plain_text = ""
        target_at = None
        for component in event.message:
            if isinstance(component, Plain):
                plain_text += component.text.strip()
            elif isinstance(component, At):
                target_at = component

        if target_at is None:
            return

        hit_cmd = None
        for cmd_key in self.cmd_map:
            if plain_text.startswith(cmd_key):
                hit_cmd = cmd_key
                break
        if hit_cmd is None:
            return

        reply_content = self.cmd_map[hit_cmd].format(at=target_at)
        await event.reply(reply_content)