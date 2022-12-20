## Logging en Python

La libreria logging de Python es un módulo que se utiliza para registrar eventos ocurridos en una aplicación o sistema. Estos eventos pueden ser de diversos tipos, tales como errores, advertencias, mensajes informativos, etc.

El propósito de utilizar la libreria logging es el de poder llevar un registro de estos eventos y tener una visión más clara de lo que está ocurriendo en la aplicación o sistema. Esto puede ser muy útil para depurar problemas, para entender cómo se está utilizando la aplicación y para tomar decisiones sobre cómo mejorarla.

La libreria logging proporciona una interfaz sencilla y consistente para registrar eventos de manera que sea fácil de configurar y utilizar en Python. Permite especificar diferentes niveles de severidad para los eventos registrados (por ejemplo, "debug", "warning", "error", etc.), y permite configurar dónde se deben escribir los mensajes de registro (por ejemplo, en un archivo, en la consola, en una base de datos, etc.). También proporciona una serie de herramientas útiles para formatear y filtrar los mensajes de registro de manera que sea más fácil de entender y analizar.

En resumen, la libreria logging es una herramienta muy útil para cualquier aplicación de Python que necesite llevar un registro de eventos ocurridos durante su ejecución.

Los niveles de severidad utilizados en la libreria logging de Python se utilizan para indicar la importancia de un mensaje de registro. Los niveles más comunes son:

**DEBUG**: Mensajes de depuración y detalles técnicos que pueden ser útiles para depurar problemas.

**INFO**: Mensajes informativos que indican que la aplicación está funcionando correctamente.

**WARNING**: Mensajes de advertencia que indican que algo puede estar mal, pero que la aplicación puede continuar funcionando.

**ERROR**: Mensajes de error que indican que algo ha fallado y que la aplicación puede tener problemas para funcionar correctamente.

**CRITICAL**: Mensajes críticos que indican un fallo grave que puede impedir que la aplicación funcione correctamente.

Los niveles se utilizan para filtrar los mensajes de registro y mostrar solo aquellos que son relevantes para el problema que se está tratando de resolver. 
Por ejemplo, si se está depurando un problema, es posible que se desee ver todos los mensajes de DEBUG y INFO, pero ignorar los mensajes de WARNING, ERROR y CRITICAL. 
Por otro lado, si se está buscando problemas graves, es posible que se desee ver solo los mensajes de ERROR y CRITICAL.

https://docs.python.org/es/3/howto/logging.html