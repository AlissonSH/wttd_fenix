# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie im virtualenv com Python 3.9
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:AlissonSH/wttd_fenix.git wttd-fenix
cd wttd-fenix
python -m venv .wttd-fenix
source .wttd-fenix/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

Segue em anexo o tutorial do desenvolvedor https://github.com/mconrado

Vou deixar aqui um guia rápido para migrar suas aplicações Django para plataforma PythonAnywhere (Anaconda 🐍 ).

Como disse é um guia rápido e não tão profundo, baseado na doc do próprio PythonAnywhere.

#### Ideal para: 
- Quem assim como eu ficou órfão do Heroku depois das mudanças e quer continuar seus estudos do projeto da Morena/Eventex.
- Para quem quer testar a plataforma e já tem um projeto Django.

#### Pequenos requisitos: 
- Seu projeto em dia.
- Projeto commitado no GitHub.
- Existência do requirements.txt para contemplar as dependências do projeto.
- Conta criada no PythonAnywhere.com.

### 1️⃣ Subindo o seu código para PythonAnywhere: 
- Na aba Console e em Start New Console clique em Bash e clone seu repositório:

```console
git clone https://github.com/seu-usuario/projeto-django-a-clonar.git
```

Ainda no Bash e dentro do diretório raiz do seu projeto crie a venv:

```console
mkvirtualenv --python=/usr/bin/python3.9 wttd-virtualenv
```

- python3.9 = substitua pela versão que você usa na venv do seu projeto.
- wttd-virtualenv = aqui serve para nomear sua venv então usei este nome como exemplo, mas guarde este nome pois vamos precisar.

Certifique que seu console tenha entrado na venv criada, caso não, dê o activate e ele deve parecer algo assim: (mysite-virtualenv)$

Finalize instalando as dependências:

```console
pip install -r requirements.txt
```

Este processo pode demorar um pouco. mconrado AP

### 2️⃣ Criando sua Web app e configurando o arquivo WSGI

Saindo da Bash e voltando no painel do PythonAnywhere clique no item Web do menu superior a direita, na próxima página clique em Manual Configuration (including virtualenvs).

Aqui lembra do nome da venv que eu pedi para guardar? Então é aqui que vamos usar.

No setor de Virtualenv, clique no link do endereço da venv e ele se tornará um campo editável, edite e logo ele deve parecer com isso:

```console
/home/nome-do-seu-user/.virtualenvs/nome-da-sua-venv
```

No item Code certifique-se que os itens estejam configurados da seguinte forma:

```console
Source Code: /home/nome-do-seu-user/pasta-raiz-do-projeto (aqui deve apontar onde está o manage.py)
```

```console
Working directory: /home/nome-do-seu-user/pasta-raiz-do-projeto/pasta-da-app-principal (aqui deve apontar onde está o settings.py)
```

```console
  
WSGI configuration file: /var/www/nome-do-seu-user_pythonanywhere_com_wsgi.py
```

```console
Python version: a versão do Python que você tem rodado o seu projeto e que foi pedido para instalar na venv
```

Agora precisamos configurar o o arquivo WSGI e para isso clique nesta mesma seção Code no link do arquivo

```console   
/var/www/nome-do-seu-user_pythonanywhere_com_wsgi.py
```

Ao abrir o arquivo altere as seguintes linhas e caso estejam comentadas, remova o comentário:

```console
path = '/home/nome-do-seu-user/pasta-raiz-do-projeto'

os.environ['DJANGO_SETTINGS_MODULE'] = 'nome-da-sua-app-principal.settings'
```

Aqui no meu caso ficou assim:

```console
os.environ['DJANGO_SETTINGS_MODULE'] = 'eventex.settings' (*lembrando do nome da pasta onde contem o settings.py)
```

Clique no botão Save para salvar este arquivo.

### 3️⃣ Configurando as variáveis de ambiente e rodando o migrate.

Nota: Aqui estou levando em conta que assim como no projeto Eventex você esteja usando:

- Decouple para leitura das variáveis de ambiente.
  - Gunicorn para contornar o serviço de arquivos estáticos.
  - Django secret key generator.

Antes de fazer o migrate do banco é preciso configurar as variáveis de ambiente e para isso existe algumas formas de se fazer isso.
Aqui vou focar só em uma:
Abra o console de preferência com virtualenv ativo, na aba Web existe um atalho direto para abrir um console com a venv já ativa, clique em Start a console in this virtualenv.

Gere a secret key pelo Django secret key generator:

```console
python contrib/secret_gen.py
```

Copie a hash gerada.

Crie um arquivo chamado .env com o seguinte conteúdo:

Aqui vale um adendo: se você usa serviço de envio de e-mail na sua app utilizando as variáveis de ambiente é interessante já colar as configs neste arquivo.
Neste caso seu arquivo deve se parecer com isso:

```console
SECRET_KEY=cole aqui a hash gerada
DEBUG=False
ALLOWED_HOSTS=nome-do-seu-user.pythonanywhere.com

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=endereco-smtp-do-seu-provedor-de-email (ex: Gmail = smtp.gmail.com)
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu-email
EMAIL_HOST_PASSWORD=senha-do-email****
```

Outra dica: na hash que você colou da SECRET_KEY remova caracteres como "()/&" que possam estar dentro da mesma.
Isso porque no passo a frente pode gerar algum erro, e eu não consegui contornar o mesmo.

Feito todo passo até aqui, salve esse arquivo .env.

De volta no console precisamos registrar estas configs na venv com o seguinte comando:

```console
echo 'set -a; source ~/pasta-raiz-do-projeto/.env; set +a' >> ~/.virtualenvs/nome-da-sua-virtual/bin/postactivate
```
### 3️⃣ Continuação...

Se tudo deu certo verifique se as variáveis de ambiente estão registradas, dando um echo na mesma como exemplo abaixo:

```console
echo $SECRET_KEY
```
A saída deverá ser o valor que você preencheu no .env

Rode as migrações do banco:

```console
python manage.py migrate
```

### 4️⃣ Rodando collectstatic e configurando a rota para os arquivos estáticos.

Ainda na bash/console é preciso rodar o collectstatic para gerar os arquivos estáticos na pasta configurada do projeto.

```console
python manage.py collectstatic
```

Se tudo ocorreu bem até aqui, volte para o menu Web e em Static files adicione a rota dos arquivos estáticos.

Onde cada campo deverá ter seu respectivo valor assim como:

Na coluna URL clique em Enter URL e adicione:

```console
/static/
```

Na coluna Directory clique Enter Path e adicione:

```console
/home/seu-usuario/pasta-raiz-do-projeto/staticfiles/
```

Lembrando: aqui usei os valores para quem acompanhou o projeto Eventex, caso seja um projeto pessoal e diferente fique atento as suas configurações e diretórios dos arquivos estáticos da forma como está no seu projeto.

Para finalizar nesta mesma seção Web vá até o topo da página e clique no botão em verde:

#### Reload seu-usuario.pythonanywhere.com

Se tudo saiu pelos conformes você pode acessar o endereço:

```console
seu-usuario.pythonanywhere.com
```

Dica final: se ao acessar apresentar algum erro, você pode verificar o log no menu Web > Log Files > e acessar Error log e descer até o final da página para ver o que há de errado e tentar corrigir.
