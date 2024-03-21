# Coloca el código de tu juego en este archivo.

define Narrador = Character('Narrador')
define jsdragon = Character('jsdragon', color="#FFFF00")

label start:
   play music "audio/bgm_Boss1.mp3" fadein 1.0 volume 0.4
   scene bg dungeon at top
   Narrador  "Ante ti, tienes al imponente dragón Javascript, esa mierda se traga todo lo que le eches, así que espero que tengas un buen plan para derrotarlo"

   show jsdragon joke at top
   Narrador "Empiezas con el Ak-47, un fusil de asalto standart Ruso de sobras conocido, recuerda que su cargador es de 30 balas y tiene 2 modos de fuego, semi y auto."
   jsdragon "Ni siquiera Midudev puede ayudarte ahora!"
   jsdragon "Preparate para una interpretación horrible de tu muerte!"

   scene bg dungeon at top
   play music "audio/bgm_sadend.mp3" fadein 1.0 volume 0.5
   Narrador "Esto me da mucha vergüenza de admitir pero parece que el dragón JavaScript al final no ha aparecido por algún error en el código, gracias por jugar..."
   Narrador "De veras que no sabemos que ha ocurrido, debe ser algo del override, las funciones puede que no hayan quedado claras..."
   Narrador "Desde luego algo ha salido mal"
   Narrador "Muchas gracias por jugar a Dragons With Ak-47 1.0 "
   Narrador "Me van a despedir..."


#show jsdragon joke 
#scene bg dungeon
#play music "audio/Kamaz.mp3" fadein 1.0 volume 0.5
 
