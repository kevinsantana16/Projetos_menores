# Cliente e Servidor TCP Simples

Este projeto contém um exemplo simples de cliente e servidor TCP que enviam e recebem 16 octetos (bytes).

## Descrição

O código implementa um servidor TCP que escuta por conexões em uma porta específica e um cliente TCP que se conecta a este servidor e troca mensagens. O servidor aceita conexões, recebe uma mensagem de 16 octetos do cliente e responde com uma mensagem de confirmação. O cliente envia uma mensagem de 16 octetos ao servidor e espera a resposta.

## Estrutura do Código

O código é composto por duas funções principais:

- `servidor(interface, port)`: Configura e inicia o servidor TCP.
- `cliente(host, port)`: Configura e inicia o cliente TCP.

Além disso, há uma função auxiliar:

- `recvall(sock, length)`: Garante que a quantidade especificada de bytes seja recebida.

