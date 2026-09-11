import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ContextTypes

# ========== آپ کی سیٹنگ ==========
BOT_TOKEN = os.getenv("BOT_TOKEN")  
CHANNEL_ID = os.getenv("CHANNEL_ID") 
ADMIN_ID = int(os.getenv("ADMIN_ID")) 

CHANNEL_LINK = "https://t.me/XAUUSDPAINDSIGNELS_5"  # 👈 آپ کا چینل لنک
CHANNEL_NAME = "Jordan Forex Traders"               # 👈 آپ کا چینل نام
# =================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # بوٹ پر /start کریں تو 2 بٹن ملیں
    keyboard = [
        [InlineKeyboardButton("🚀 Jordan Free Signal 🚀", url=CHANNEL_LINK)],
        [InlineKeyboardButton("📊 View Gold Signal 📊", url=CHANNEL_LINK)]
    ]
    text = f"""*Welcome to {CHANNEL_NAME}*

Get FREE XAUUSD Gold Signals Daily.

Choose below: 👇
"""
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def send_ad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # صرف آپ ہی ایڈ پوسٹ کر سکتے ہیں
    if update.message.from_user.id == ADMIN_ID:
        
        # پروفیشنل بورڈ فارمیٹ
        ad_text = f"""━━━━━━━━━━━━━━
📢 *{CHANNEL_NAME}* 📢
━━━━━━━━━━━━━━

{update.message.text}

━━━━━━━━━━━━━━
🎯 *FREE GOLD SIGNALS DAILY*
━━━━━━━━━━━━━━
"""
        # اب 2 بٹن ہوں گے اور دونوں سیدھا چینل پر لے جائیں گے
        keyboard = [
            [InlineKeyboardButton("🚀 Jordan Free Signal 🚀", url=CHANNEL_LINK)],
            [InlineKeyboardButton("📊 View Gold Signal 📊", url=CHANNEL_LINK)]
        ]
        
        await context.bot.send_message(
            chat_id=CHANNEL_ID, 
            text=ad_text, 
            reply_markup=InlineKeyboardMarkup(keyboard), 
            parse_mode='Markdown',
            disable_web_page_preview=True
        )
        await update.message.reply_text("✅ Ad Posted with 2 Buttons!")
    
    else:
        await update.message.reply_text("❌ Only Admin can post ads.")

# ===== بوٹ چلائیں =====
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_ad))

print(f"{CHANNEL_NAME} Ad Bot is Running...")
app.run_polling()
