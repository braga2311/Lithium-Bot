# Lithium Bot

## Visão Geral
O Lithium Bot é um bot multifuncional para Discord desenvolvido em Python utilizando a biblioteca `discord.py`. Ele oferece uma ampla variedade de comandos organizados em categorias como administração, utilidades, jogos, brincadeiras e geração de dados fictícios para testes.

## Estrutura do Projeto

```
lithium-bot/
├── bot.py                # Ponto de entrada principal
├── config.py             # Configurações do bot
├── commands/
│   ├── admin.py          # Comandos de administração
│   ├── brincadeiras.py   # Comandos de interação divertida
│   ├── consultas.py      # Comandos de consulta pública
│   ├── imagens.py        # Comandos relacionados a imagens
│   ├── jogos.py          # Comandos de jogos simples
│   ├── jogos-azar.py     # Comandos de jogos de azar
│   ├── menu.py           # Menu de ajuda organizado
│   ├── utilidades.py     # Comandos utilitários
│   └── gerar-dados-falsos.py # Geradores
```

## Requisitos Técnicos

- Python 3.8 ou superior
- Bibliotecas principais:
  - discord.py (2.3.2 ou superior)
  - requests (para comandos de consulta)
- Variáveis de ambiente necessárias:
  - `DISCORD_TOKEN`: Token de autenticação do bot
  - `BOT_OWNER_ID`: ID do dono do bot (opcional)

## Funcionalidades Principais

### 1. Administração
- Moderação avançada (kick, ban, mute, purge)
- Gerenciamento de canais (lock, unlock, slowmode)
- Gerenciamento de cargos e nicknames
- Sistema de votação integrado
- Visualização de informações do servidor e usuários

### 2. Utilidades
- Visualização de avatares e informações de usuários
- Sistema de lembretes temporizados
- Geração de convites para o servidor
- Criação de QR Codes

### 3. Jogos e Diversão
- Jogos de azar (roleta russa, blackjack, loteria)
- Comandos de interação (beijo, tapa, ship)
- Gerador de memes e imagens aleatórias
- Sistema de escolha aleatória

### 4. Consultas Públicas
- Validação de CPF/CNPJ
- Consulta de CEP, DDD e informações geográficas
- Verificação de dados de cartões (BIN)
- Cotação de moedas em tempo real

### 5. Geração de Dados Fictícios
- Geradores de documentos para testes:
  - CPF válido formatado
  - Número de CNH com dígitos verificadores
  - CEP válido
  - Título de eleitor

## Configuração

1. Clone o repositório:
```bash
git clone https://github.com/braga2311/Lithium-Bot.git
cd lithium-bot
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
export DISCORD_TOKEN="seu_token_aqui"
export BOT_OWNER_ID="seu_id_discord"
```

4. Execute o bot:
```bash
python bot.py
```

## Comandos Disponíveis

O bot possui um sistema de menu integrado (!menu) que organiza todos os comandos em categorias. Os principais comandos incluem:

### Administração
- `!ping` - Verifica a latência do bot
- `!expulsar @usuário` - Expulsa um membro
- `!banir @usuário` - Bane um membro
- `!limpar [n]` - Limpa mensagens
- `!slowmode [s]` - Ativa slowmode

### Utilidades
- `!avatar @usuário` - Mostra o avatar
- `!userinfo @usuário` - Informações do usuário
- `!serverinfo` - Informações do servidor
- `!lembrete [min] [msg]` - Define lembrete
- `!qr [texto]` - Gera QR Code

### Jogos
- `!roleta` - Roleta russa
- `!blackjack` - Jogo simplificado
- `!loteria` - Números da sorte
- `!coinflip` - Cara ou coroa
- `!dados [qtd]` - Rola dados

### Diversão
- `!beijo @usuário` - Manda beijo
- `!tapa @usuário` - Dá tapa virtual
- `!ship @user1 @user2` - Compatibilidade
- `!meme` - Meme aleatório
- `!gato` - Foto de gato

## Considerações de Segurança

1. **Permissões**: O bot requer apenas as permissões necessárias para cada funcionalidade.
2. **Dados Fictícios**: Os documentos gerados são apenas para testes e não devem ser usados para fins ilícitos.
3. **Logs**: Recomenda-se implementar um sistema de logs para auditoria de comandos administrativos.
4. **Atualizações**: Mantenha o bot e suas dependências sempre atualizadas.

## Roadmap Futuro

- Implementar sistema de economia com moeda virtual
- Adicionar mais jogos multiplayer
- Integração com APIs de clima e notícias
- Sistema de tickets para suporte
- Comandos de música melhorados

## Suporte

Para suporte técnico ou relatório de bugs, entre em contato com os desenvolvedores: [bragasupport](https://discord.gg/e6MbPGT7)
---

**Nota**: Esta documentação foi gerada com base no código fonte atual e está sujeita a atualizações conforme o desenvolvimento do bot evolui.
##
