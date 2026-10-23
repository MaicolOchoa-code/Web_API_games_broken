# Respuestas del parcial

1. ¿Qué error encontraste en la validación de `stock`?

El stock permitía valores desde 0. Lo corregí cambiando ge=0 por ge=1, para que solo acepte valores entre 1 y 50.

2. ¿Qué hacía que un juego pareciera creado pero no quedara persistido?

Faltaba ejecutar session.commit() después de agregar el juego a la sesión. Con commit() se guardan los cambios en SQLite

3. ¿Qué problema tenía el endpoint que lista juegos?

El endpoint utilizaba response_model=GameResponse, que representa un solo juego. Lo corregí usando response_model=list[GameResponse], porque devuelve una lista de juegos.

4. ¿Cómo solucionaste la consulta de un ID inexistente?

Agregué una condición para comprobar si el juego existe. Si no existe, la API devuelve un error 404 con el mensaje Game not found.

5. ¿Por qué DELETE podía responder correctamente y aun así no eliminar el registro de SQLite?

Porque faltaba ejecutar session.commit() después de session.delete(game). El commit guarda la eliminación en la base de datos.