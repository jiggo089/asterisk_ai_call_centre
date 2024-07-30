 # [incoming]
exten => xxxxxxxxx,1,NoOp(Incoming call from ${CALLERID(num)})
 same => n,Answer()
 same => n,Playback(/var/lib/asterisk/sounds/gpt/hello_menu_wav) ; Приветственное сообщение
 same => n,Set(TIMEOUT(digit)=5) ; Установка тайм-аута для ввода цифр
 same => n,Set(TIMEOUT(response)=10)
 same => n,Background(en/one-moment-please) ; Сообщение, объясняющее варианты меню (предполагается, что вы используете стандартные фразы, такие как "press 1 for ...")
 same => n,Background(en/beep) ; Дополнительные инструкции

 same => n,WaitExten() ; Ожидание ввода от пользователя

exten => 1,1,NoOp(User pressed 1)
 same => n,Playback(/var/lib/asterisk/sounds/gpt/1_doc_choice_wav) ; Воспроизведение подтверждения выбора
 same => n,AGI(/var/lib/asterisk/agi-bin/record_and_hangup.py)
 same => n,Playback(/var/lib/asterisk/sounds/gpt/wait_wav)
 same => n,AGI(/var/lib/asterisk/agi-bin/gpt1_doc.py)
 same => n,Playback(/var/lib/asterisk/sounds/gpt/tts_menu_wav)
 same => n,Hangup()

exten => 2,1,NoOp(User pressed 2)
 same => n,Playback(/var/lib/asterisk/sounds/gpt/2_record_check_wav) ; Воспроизведение подтверждения выбора
 same => n,AGI(/var/lib/asterisk/agi-bin/record_and_hangup.py)
 same => n,Playback(/var/lib/asterisk/sounds/gpt/wait_wav)
 same => n,AGI(/var/lib/asterisk/agi-bin/gpt2_record.py)
 same => n,Playback(/var/lib/asterisk/sounds/gpt/tts_menu_wav)
 same => n,Hangup()

exten => i,1,NoOp(Invalid option)
 same => n,Playback(en/invalid) ; Воспроизведение сообщения "неверный ввод"
 same => n,Goto(incoming,xxxxxxxxx,1) ; Возврат в начало меню

exten => t,1,NoOp(Timeout)
 same => n,Playback(en/timeout) ; Воспроизведение сообщения "тайм-аут"
 same => n,Goto(incoming,xxxxxxxx,1) ; Возврат в начало меню
