# Chat GRF Talk

Bem-vindo ao  Chat GRF Talk , um aplicativo de chat inspirado no WhatsApp, com backend desenvolvido em Django . Este projeto visa proporcionar uma experiência de comunicação em tempo real, segura e eficiente.

## Funcionalidades

* **Mensagens em Tempo Real** : Envie e receba mensagens instantaneamente.
* **Autenticação de Usuário** : Cadastro e login seguros para proteger suas conversas.
* **Grupos de Chat** : Crie e participe de grupos para conversas em equipe.
* **Notificações** : Receba alertas para novas mensagens e atividades.

## Tecnologias Utilizadas

* **Django** : Framework web de alto nível para o backend.
* **Django** Rest Framework
* **Django Channels** : Gerenciamento de WebSockets para comunicação em tempo real.
* **Redis** : Broker de mensagens para suporte a WebSockets.
* **MySql**: Banco de dados relacional para armazenamento de dados.
* **HTML5 & CSS3** : Estrutura e estilo da interface do usuário.
* **Next.js**: Funcionalidades dinâmicas no frontend.

## Instalação

1. **Clone o repositório** :
   ```bash
   git clone [https://github.com/seu-usuario/chatzap.git](https://github.com/seu-usuario/chatzap.git)
   cd chatzap

```

```

1. **Crie um ambiente virtual e ative-o** :
   ```bash
   python3 -m venv venv
   source venv/bin/activate

```

```

1. **Instale as dependências** :
   ```bash
   pip install -r requirements.txt

```

```

1. **Configure o banco de dados** :

* Certifique-se de que o PostgreSQL esteja instalado e em execução.
* Crie um banco de dados chamado `chatzap`.
* Atualize as configurações de banco de dados em `settings.py` com suas credenciais.

1. **Aplique as migrações** :
   ```bash
   python manage.py migrate

```

```

1. **Inicie o servidor Redis** :
   ```bash
   redis-server

```

```

1. **Execute o servidor de desenvolvimento** :
   ```bash
   python manage.py runserver

```

```

1. **Acesse o aplicativo** :
   Abra seu navegador e vá para `http://127.0.0.1:8000`.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](https://chatgpt.com/c/LICENSE).

---

Pronto para revolucionar a comunicação? Então, mãos à obra! O ChatZap está esperando por você.
