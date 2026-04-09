import chardet
from config import EMOJIS, DEFAULT_EMOJI_ID
import json


def update_task_emojis():
    try:
        # Загружаем JSON
        with open('task_state.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        tasks = data.get('tasks', {})
        updated_count = 0

        print("🔄 Обновляем sender_emoji_id...")

        for task_id, task_data in tasks.items():
            sender_id = str(task_data.get('sender_id', ''))

            # Получаем нужный эмодзи
            emoji_id = EMOJIS.get(sender_id, DEFAULT_EMOJI_ID)

            # Обновляем, если не совпадает
            if task_data.get('sender_emoji_id') != emoji_id:
                task_data['sender_emoji_id'] = emoji_id
                updated_count += 1
                print(f"✅ Задача {task_id}: {sender_id} → {emoji_id}")

        # Сохраняем
        with open('task_state.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"\n🎉 Обновлено задач: {updated_count}")
        print("📁 task_state.json сохранен!")

    except FileNotFoundError:
        print("❌ task_state.json не найден!")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

update_task_emojis()
