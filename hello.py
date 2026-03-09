async def on_request(context):
    return Response(
        "¡Hola Mundo desde Python en Cloudflare! 🐍",
        headers={"Content-Type": "text/plain; charset=utf-8"}
    )
