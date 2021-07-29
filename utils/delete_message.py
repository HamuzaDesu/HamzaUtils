import asyncio

async def delete_message(message, ctx, time):
    await asyncio.sleep(time)

    await ctx.message.delete()
    await message.delete()