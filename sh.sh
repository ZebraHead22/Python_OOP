#!/bin/bash

echo "🔧 Очистка macOS — старт"
echo "Потребуется пароль администратора"

# Запрос sudo один раз
sudo -v

echo "— Очистка пользовательских кэшей"
rm -rf ~/Library/Caches/*

echo "— Очистка системных кэшей"
sudo rm -rf /Library/Caches/*

echo "— Очистка логов"
sudo rm -rf /private/var/log/*
rm -rf ~/Library/Logs/*

echo "— Очистка DNS-кэша"
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

echo "— Пересборка Launch Services"
sudo /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
    -kill -r -domain local -domain system -domain user

echo "— Очистка неиспользуемой памяти"
sudo purge 2>/dev/null

echo "— Завершение фоновых индексаторов (временно)"
sudo mdutil -a -i off
sleep 2
sudo mdutil -a -i on

echo "✅ Готово. Рекомендуется перезагрузить Mac."
