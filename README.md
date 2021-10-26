# Management-Sistem

## História e Objetivo : 
O projeto  tem como objetivo ser uma aplicação para gestão de produtos, venda e compra de produtos e serviços, bem como a inteligência de armazenamento. O sistema hoje é feito em Django e Bootstrap e tem implementações diversas que ainda estão sendo construidas
## Principais Caracteristicas :
- Design Responsivo 
- Formulários Tabulados (django-cripsy-forms)
- Fácil Entendimento e Adaptação
- Fácil Escalabilidade (Qualquer um pode contribuir com extensões, widgets or comportamentos diversos)
## Principais Funcionalidades :
- Administração Personalizada (Filtros, Aparência, ações e etc personalizáveis)
- Registro, organização e controle de armazenamento dos produtos
- Registro e controle de serviços
- Controle e registro de vendas de serviços e produtos (Por diversos tipos de usuários)
- Controle e registro de compras de produtos (Somente com autorização prévia)
- Dashboard para controle e análise de dados
- Controle de divulgação externa da plataforma

### Em construção :

O projeto iniciou sendo uma maneira de estudos, e hoje esta tomando novas proporções, por isso esta sendo revisto as bases e refatorado para que possa ser usado em diferentes plataformas, ***não esta em processo de produção***

## Como Inicializar :

Caso você não tenha o repositório em seu computador, basta clona-lo na pasta que deseja :
```bash
git clone https://github.com/Chuckpy/Management-Sistem.git
```
Feito isso, basta acessar seu âmbiente virtual, caso não tenha um âmbiente virtual, basta criar um com o código:
```bash
python3 -v venv venv
```
Se você ja tem o âmbiente, pode acessar no seu linux com :
```bash
source venv/bin/activate
```
Agora dentro do seu âmbiente, basta fazer as migrações e iniciar o projeto com os seguintes comandos : 
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
Feito tudo corretamente, você pode acessar o sistema administrativo com um "superusuario", criado facilmente com o comando :

```bash
python3 manage.py createsuperuser
```

## Como contribuir com o projeto :

O projeto foi imaginado inicialmente para ser open source, portanto, caso queira apoiar o projeto codando conosco, sinta-se a vontade.
Veja os relatórios e onde pode ajudar em [Questões](https://github.com/Chuckpy/Management-Sistem/issues)


