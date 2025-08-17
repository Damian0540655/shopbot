from keep_alive import keep_alive
keep_alive()

import csv
import os
import re
import time
from datetime import datetime
from uuid import uuid4
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler

TOKEN = "8458947832:AAHhGXiD2bxdVomhqv8M-7fs7d3naTXz4Co"
ADMIN_USER_ID = 7645912530
ORDERS_CSV = "orders.csv"

PRICE = {"dns": 5, "iphone": 10, "ipad": 5}
CHOOSING_PRODUCT, ASK_UDID, CHOOSING_PAY, ASK_CODE = range(4)

def ensure_csv():
    if not os.path.exists(ORDERS_CSV):
        with open(ORDERS_CSV, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["order_id","user_id","username","product","price_eur","udid","payment_method","code_masked","status","created_at","updated_at"])

def start(update: Update, context: CallbackContext):
    ensure_csv()
    kb = [
        [InlineKeyboardButton("🛡️ Anti-Revoke DNS — 5€", callback_data="dns")],
        [InlineKeyboardButton("📱 iPhone Certificate — 10€", callback_data="iphone")],
        [InlineKeyboardButton("📲 iPad Certificate — 5€", callback_data="ipad")],
    ]
    update.message.reply_text("Welcome! Choose a product:", reply_markup=InlineKeyboardMarkup(kb))

def help_cmd(update: Update, context: CallbackContext):
    update.message.reply_text("Use /start to open the shop. Orders will be confirmed by admin.")

def main():
    ensure_csv()
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_cmd))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
