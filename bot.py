import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ContextTypes

# ===== آپ کی سیٹنگ یہاں لگی ہوئی ہے =====
BOT_TOKEN = os.getenv("BOT_TOKEN")  
CHANNEL_ID = os.getenv("CHANNEL_ID") 
ADMIN_ID = int(os.getenv("ADMIN_ID")) 

CHANNEL_LINK = "https://t.me/XAUUSDPAINDSIGNELS_5"  # آپ کا چینل لنک
CHANNEL_NAME = "Jordan Forex Traders"               # آپ کا چینل نام
# =========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # جب کوئی /start کرے تو سیدھا چینل کا بٹن آئے
    keyboard = [[InlineKeyboardButton(f"🚀 JOIN {CHANNEL_NAME} 🚀", url=CHANNEL_LINK)]]
    welcome_text = f"""*Welcome to {CHANNEL_NAME}*

Click the button below to join our channel for FREE Forex Signals.
"""
    await update.message.reply_text(welcome_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def send_ad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # صرف Admin ہی ایڈ پوسٹ کر سکے گا
    if update.message.from_user.id == ADMIN_ID:
        # یہ پروفیشنل بورڈ فارمیٹ ہے
        ad_text = f"""━━━━━━━━━━━━━━━━━━━━
📢 *{CHANNEL_NAME}* 📢
━━━━━━━━━━━━━━━━━━━━

{update.message.text}

━━━━━━━━━━━━━━━━━━━━
👇 *CLICK BELOW TO JOIN* 👇
━━━━━━━━━━━━━━━━━━━━
"""
        # بٹن سیدھا چینل پر لے جائے گا
        keyboard = [[InlineKeyboardButton(f"🚀 JOIN {CHANNEL_NAME} NOW 🚀", url=CHANNEL_LINK)]]
        
        await context.bot.send_message(
            chat_id=CHANNEL_ID, 
            text=ad_text, 
            reply_markup=InlineKeyboardMarkup(keyboard), 
            parse_mode='Markdown'
        )
        await update.message.reply_text("✅ Ad Posted Successfully in Channel!")
    
    else:
        await update.message.reply_text("❌ Sorry, Only Admin can post ads.")

# ===== بوٹ سٹارٹ =====
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_ad))

print(f"{CHANNEL_NAME} Pro Ad Bot is Running...")
app.run_polling()
